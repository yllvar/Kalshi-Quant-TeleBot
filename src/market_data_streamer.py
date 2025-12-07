#!/usr/bin/env python3
"""Enhanced market data module for Phase 3 - Kalshi trading bot."""

import logging
import time
import threading
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
import requests

logger = logging.getLogger(__name__)

@dataclass
class MarketData:
    """Structured market data container."""
    market_id: str
    title: str
    current_price: float
    previous_price: Optional[float] = None
    volume: Optional[int] = None
    open_interest: Optional[int] = None
    last_updated: datetime = None
    price_history: List[float] = None
    volatility: Optional[float] = None

    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.now()
        if self.price_history is None:
            self.price_history = []

    @property
    def price_change(self) -> Optional[float]:
        """Calculate price change from previous price."""
        if self.previous_price is None:
            return None
        return self.current_price - self.previous_price

    @property
    def price_change_pct(self) -> Optional[float]:
        """Calculate percentage price change."""
        if self.previous_price is None or self.previous_price == 0:
            return None
        return (self.price_change / self.previous_price) * 100

class MarketDataStreamer:
    """Enhanced market data streaming and management."""

    def __init__(self, api_client, update_interval: int = 30):
        """
        Initialize market data streamer.

        Args:
            api_client: Kalshi API client instance
            update_interval: Seconds between data updates
        """
        self.api_client = api_client
        self.update_interval = update_interval
        self.markets_data: Dict[str, MarketData] = {}
        self.subscribers: List[Callable] = []
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self.last_update = datetime.now()

    def add_subscriber(self, callback: Callable):
        """Add a callback to be notified of market data updates."""
        self.subscribers.append(callback)

    def remove_subscriber(self, callback: Callable):
        """Remove a subscriber callback."""
        if callback in self.subscribers:
            self.subscribers.remove(callback)

    def _notify_subscribers(self, updated_markets: List[str]):
        """Notify all subscribers of market updates."""
        for subscriber in self.subscribers:
            try:
                subscriber(updated_markets, self.markets_data)
            except Exception as e:
                logger.error(f"Error notifying subscriber: {e}")

    def start_streaming(self):
        """Start the market data streaming thread."""
        if self.running:
            logger.warning("Market data streaming already running")
            return

        self.running = True
        self.thread = threading.Thread(target=self._streaming_loop, daemon=True)
        self.thread.start()
        logger.info(f"Started market data streaming (interval: {self.update_interval}s)")

    def stop_streaming(self):
        """Stop the market data streaming."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=5)
        logger.info("Stopped market data streaming")

    def _streaming_loop(self):
        """Main streaming loop."""
        while self.running:
            try:
                self._update_market_data()
                time.sleep(self.update_interval)
            except Exception as e:
                logger.error(f"Error in streaming loop: {e}")
                time.sleep(self.update_interval)

    def _update_market_data(self):
        """Fetch and update market data."""
        try:
            # Get fresh market data from API
            raw_markets = self.api_client.get_markets()

            if not raw_markets or 'markets' not in raw_markets:
                logger.warning("No market data received from API")
                return

            updated_markets = []

            for market in raw_markets['markets'][:20]:  # Limit for performance
                market_id = market.get('id')
                if not market_id:
                    continue

                # Extract market data
                current_price = market.get('current_price')
                if current_price is None:
                    continue

                # Get or create market data object
                if market_id in self.markets_data:
                    market_data = self.markets_data[market_id]
                    market_data.previous_price = market_data.current_price
                    market_data.current_price = current_price
                    market_data.last_updated = datetime.now()

                    # Update price history (keep last 100 points)
                    market_data.price_history.append(current_price)
                    if len(market_data.price_history) > 100:
                        market_data.price_history.pop(0)

                else:
                    # Create new market data object
                    market_data = MarketData(
                        market_id=market_id,
                        title=market.get('title', ''),
                        current_price=current_price,
                        volume=market.get('volume'),
                        open_interest=market.get('open_interest'),
                        price_history=[current_price]
                    )
                    self.markets_data[market_id] = market_data

                # Calculate basic volatility (rolling std of recent prices)
                if len(market_data.price_history) > 10:
                    recent_prices = market_data.price_history[-20:]
                    if len(recent_prices) > 1:
                        returns = [recent_prices[i+1]/recent_prices[i] - 1
                                 for i in range(len(recent_prices)-1)]
                        market_data.volatility = float(np.std(returns) * np.sqrt(252))  # Annualized

                updated_markets.append(market_id)

            self.last_update = datetime.now()

            # Notify subscribers if we have updates
            if updated_markets:
                self._notify_subscribers(updated_markets)

        except Exception as e:
            logger.error(f"Error updating market data: {e}")

    def get_market_data(self, market_id: str) -> Optional[MarketData]:
        """Get current data for a specific market."""
        return self.markets_data.get(market_id)

    def get_all_markets_data(self) -> Dict[str, MarketData]:
        """Get data for all tracked markets."""
        return self.markets_data.copy()

    def get_top_movers(self, limit: int = 5) -> List[MarketData]:
        """Get markets with largest price movements."""
        markets = list(self.markets_data.values())

        # Filter markets with price change data
        movers = [m for m in markets if m.price_change_pct is not None]

        # Sort by absolute price change percentage
        movers.sort(key=lambda m: abs(m.price_change_pct), reverse=True)

        return movers[:limit]

    def get_high_volatility_markets(self, limit: int = 5) -> List[MarketData]:
        """Get markets with highest volatility."""
        markets = list(self.markets_data.values())

        # Filter markets with volatility data
        volatile = [m for m in markets if m.volatility is not None]

        # Sort by volatility descending
        volatile.sort(key=lambda m: m.volatility, reverse=True)

        return volatile[:limit]

    def get_market_summary(self) -> Dict[str, Any]:
        """Get overall market summary statistics."""
        if not self.markets_data:
            return {'total_markets': 0}

        markets = list(self.markets_data.values())

        # Calculate summary statistics
        avg_price = np.mean([m.current_price for m in markets])
        avg_volatility = np.mean([m.volatility for m in markets if m.volatility])

        # Count movers
        gainers = sum(1 for m in markets if m.price_change_pct and m.price_change_pct > 0)
        losers = sum(1 for m in markets if m.price_change_pct and m.price_change_pct < 0)

        return {
            'total_markets': len(markets),
            'average_price': float(avg_price),
            'average_volatility': float(avg_volatility) if not np.isnan(avg_volatility) else None,
            'gainers': gainers,
            'losers': losers,
            'unchanged': len(markets) - gainers - losers,
            'last_update': self.last_update.isoformat(),
            'update_interval': self.update_interval
        }
