import pandas as pd
import numpy as np
import logging
import time
from typing import List
from config import BANKROLL, NEWS_SENTIMENT_THRESHOLD, STAT_ARBITRAGE_THRESHOLD, VOLATILITY_THRESHOLD, MAX_POSITION_SIZE_PERCENTAGE, STOP_LOSS_PERCENTAGE
from news_analyzer import NewsSentimentAnalyzer
from arbitrage_analyzer import StatisticalArbitrageAnalyzer
from volatility_analyzer import VolatilityAnalyzer
from risk_manager import RiskManager
from market_data_streamer import MarketDataStreamer
from performance_analytics import PerformanceAnalytics, Trade

class Trader:
    def __init__(self, api, notifier, logger, bankroll):
        self.api = api
        self.notifier = notifier
        self.logger = logger
        self.bankroll = bankroll
        self.current_positions = {}
        self.news_analyzer = NewsSentimentAnalyzer()
        self.arbitrage_analyzer = StatisticalArbitrageAnalyzer()
        self.volatility_analyzer = VolatilityAnalyzer()
        self.risk_manager = RiskManager(bankroll)

        # Phase 3: Enhanced market data and performance tracking
        self.market_data_streamer = MarketDataStreamer(api, update_interval=60)  # Update every minute
        self.performance_analytics = PerformanceAnalytics()

        # Subscribe to market data updates for real-time monitoring
        self.market_data_streamer.add_subscriber(self._on_market_data_update)

    def _on_market_data_update(self, updated_markets: List[str], all_market_data: Dict[str, Any]):
        """Handle real-time market data updates."""
        # Check for stop-loss triggers on open positions
        current_prices = {market_id: data.current_price
                         for market_id, data in all_market_data.items()}

        self.check_positions_for_risk_management(current_prices)

        # Log significant market movements
        for market_id in updated_markets:
            if market_id in all_market_data:
                market_data = all_market_data[market_id]
                if market_data.price_change_pct and abs(market_data.price_change_pct) > 2.0:
                    self.logger.info(f"Market movement: {market_data.title} "
                                   f"changed {market_data.price_change_pct:.2f}% "
                                   f"to ${market_data.current_price:.2f}")

    def analyze_market(self, market_data):
        # Enhanced analysis with news sentiment
        return self._make_trade_decision(market_data)

    def _make_trade_decision(self, market_data):
        """
        Enhanced trade decision making with multiple strategies
        Priority: News Sentiment → Statistical Arbitrage → Volatility Analysis
        """
        trade_decision = None

        # Strategy 1: News Sentiment Analysis
        try:
            sentiment_analysis = self.news_analyzer.get_market_relevant_news()
            sentiment_decision = self.news_analyzer.should_trade_based_on_sentiment(
                sentiment_analysis, NEWS_SENTIMENT_THRESHOLD
            )

            if sentiment_decision['should_trade']:
                self.logger.info(f"News sentiment signal: {sentiment_decision['reason']}")

                # Find suitable market to trade based on sentiment
                if market_data and 'markets' in market_data and market_data['markets']:
                    market = market_data['markets'][0]  # Simple selection - could be enhanced
                    event_id = market.get('id')
                    current_price = market.get('current_price')

                    if event_id and current_price:
                        action = 'buy' if sentiment_decision['direction'] == 'long' else 'sell'
                        quantity = 1  # Base quantity - will be adjusted by risk management

                        trade_decision = {
                            'event_id': event_id,
                            'action': action,
                            'quantity': quantity,
                            'price': current_price,
                            'strategy': 'news_sentiment',
                            'sentiment_score': sentiment_decision['sentiment_score'],
                            'confidence': sentiment_decision['confidence']
                        }

                        # Apply basic risk management to position sizing
                        position_size_fraction = self.risk_manager.calculate_position_size_kelly(sentiment_decision['confidence'])
                        position_value = self.risk_manager.current_bankroll * position_size_fraction
                        trade_decision['quantity'] = max(1, int(position_value / current_price))

                        self.logger.info(f"News sentiment trade decision: {action} {event_id} "
                                       f"at {current_price} (sentiment: {sentiment_decision['sentiment_score']:.3f})")

        except Exception as e:
            self.logger.error(f"Error in news sentiment analysis: {e}")

        # Strategy 2: Statistical Arbitrage (if no sentiment signal)
        if not trade_decision:
            try:
                arbitrage_opportunities = self._statistical_arbitrage(market_data)
                if arbitrage_opportunities:
                    # Take the highest confidence opportunity
                    best_opportunity = arbitrage_opportunities[0]
                    execution_decision = self.arbitrage_analyzer.should_execute_arbitrage(
                        best_opportunity, risk_tolerance=0.7
                    )

                    if execution_decision['should_execute']:
                        self.logger.info(f"Arbitrage signal: {execution_decision['reason']}")

                        # For simplicity, focus on one side of the arbitrage pair
                        market1 = execution_decision['market1']

                        if best_opportunity['signal'] == 'LONG_SPREAD':
                            event_id = market1['id']
                            action = 'buy'
                        else:  # SHORT_SPREAD
                            event_id = market1['id']
                            action = 'sell'

                        # Basic risk management
                        position_size_fraction = self.risk_manager.calculate_position_size_kelly(execution_decision['confidence'])
                        position_value = self.risk_manager.current_bankroll * position_size_fraction
                        quantity = max(1, int(position_value / market1['current_price']))

                        trade_decision = {
                            'event_id': event_id,
                            'action': action,
                            'quantity': quantity,
                            'price': market1['current_price'],
                            'strategy': 'statistical_arbitrage',
                            'z_score': best_opportunity['z_score'],
                            'confidence': execution_decision['confidence'],
                            'arbitrage_pair': [market1['id'], market2['id']]
                        }

                        self.logger.info(f"Arbitrage trade decision: {action} {event_id} "
                                       f"(z-score: {best_opportunity['z_score']:.3f})")

            except Exception as e:
                self.logger.error(f"Error in statistical arbitrage: {e}")

        # Strategy 3: Volatility Analysis (if no other signals)
        if not trade_decision:
            try:
                volatility_decision = self._volatility_analysis(market_data)
                if volatility_decision and volatility_decision.get('should_trade'):
                    self.logger.info(f"Volatility signal: {volatility_decision['reason']}")

                    # Find market for volatility-based trade
                    if market_data and 'markets' in market_data and market_data['markets']:
                        market = market_data['markets'][0]  # Could be enhanced to select based on volatility
                        event_id = market.get('id')
                        current_price = market.get('current_price')

                        if event_id and current_price and volatility_decision.get('direction'):
                            action = 'buy' if volatility_decision['direction'] == 'long' else 'sell'

                            # Basic risk management
                            position_size_fraction = self.risk_manager.calculate_position_size_kelly(volatility_decision['confidence'])
                            position_value = self.risk_manager.current_bankroll * position_size_fraction
                            quantity = max(1, int(position_value / current_price))

                            trade_decision = {
                                'event_id': event_id,
                                'action': action,
                                'quantity': quantity,
                                'price': current_price,
                                'strategy': 'volatility_based',
                                'volatility_regime': volatility_decision.get('volatility_regime'),
                                'confidence': volatility_decision['confidence'],
                                'signal_type': volatility_decision.get('signal_type')
                            }

                            self.logger.info(f"Volatility trade decision: {action} {event_id} "
                                           f"(regime: {volatility_decision.get('volatility_regime')})")

            except Exception as e:
                self.logger.error(f"Error in volatility analysis: {e}")

        return trade_decision

    def execute_trade(self, trade_decision):
        """
        Execute trade with basic risk management
        """
        if not trade_decision:
            self.logger.info("No trade decision to execute.")
            return

        event_id = trade_decision['event_id']
        action = trade_decision['action']
        quantity = trade_decision['quantity']
        price = trade_decision['price']
        strategy = trade_decision.get('strategy', 'unknown')

        try:
            # Validate position size
            position_value = quantity * price
            if not self.risk_manager.validate_position_size(position_value):
                self.logger.warning(f"Position size ${position_value:.2f} exceeds risk limits")
                return

            self.logger.info(f"Executing {strategy} trade: {action} {quantity} units of {event_id} "
                           f"at ${price:.2f}")

            # Generate unique trade ID
            trade_id = f"{strategy}_{event_id}_{int(time.time())}"

            # Execute the trade via API (placeholder for now)
            if action.lower() == 'buy':
                self.logger.info(f"BUY ORDER: {quantity} units of {event_id} at ${price:.2f}")
            elif action.lower() == 'sell':
                self.logger.info(f"SELL ORDER: {quantity} units of {event_id} at ${price:.2f}")

            # Record trade in performance analytics
            trade = Trade(
                trade_id=trade_id,
                market_id=event_id,
                strategy=strategy,
                side=action.lower(),
                quantity=quantity,
                entry_price=price,
                confidence=trade_decision.get('confidence', 0.5)
            )
            self.performance_analytics.record_trade(trade)

            # Store position locally for basic tracking
            self.current_positions[event_id] = {
                'quantity': quantity,
                'entry_price': price,
                'type': 'long' if action.lower() == 'buy' else 'short',
                'strategy': strategy,
                'stop_loss_price': self.risk_manager.calculate_stop_loss_price(
                    price, action.lower() == 'buy'
                ),
                'trade_id': trade_id
            }

            # Send notification
            self.notifier.send_trade_notification(
                f"{strategy.upper()}: {action.upper()} {quantity} units of {event_id} at ${price:.2f}"
            )

        except Exception as e:
            self.logger.error(f"Error executing {strategy} trade for {event_id}: {e}")
            self.notifier.send_error_notification(f"Trade execution error for {event_id}: {e}")

    def check_positions_for_risk_management(self, current_prices: Dict[str, float]):
        """
        Check all open positions for stop-loss triggers.
        """
        positions_to_close = []

        for market_id, position in self.current_positions.items():
            current_price = current_prices.get(market_id, position['entry_price'])

            # Check stop-loss
            if self.risk_manager.check_stop_loss_trigger(
                position['entry_price'], current_price, position['type'] == 'long'
            ):
                positions_to_close.append({
                    'market_id': market_id,
                    'exit_price': current_price,
                    'reason': 'stop_loss_triggered'
                })

        # Close positions that hit stop-loss
        for close_info in positions_to_close:
            self.close_position_simple(close_info['market_id'],
                                     close_info['exit_price'],
                                     close_info['reason'])

    def close_position_simple(self, market_id: str, exit_price: float, reason: str):
        """
        Close a position with simple P&L calculation.
        """
        if market_id not in self.current_positions:
            return

        position = self.current_positions[market_id]

        # Calculate P&L
        entry_price = position['entry_price']
        quantity = position['quantity']

        if position['type'] == 'long':
            pnl = (exit_price - entry_price) * quantity
        else:  # short
            pnl = (entry_price - exit_price) * quantity

        # Update bankroll
        self.risk_manager.current_bankroll += pnl

        # Record trade closure in performance analytics
        trade_id = position.get('trade_id')
        if trade_id:
            self.performance_analytics.close_trade(trade_id, exit_price, reason)

        # Remove from positions
        del self.current_positions[market_id]

        # Send notification
        self.notifier.send_trade_notification(
            f"RISK MANAGEMENT: Closed {market_id} at ${exit_price:.2f}, P&L: ${pnl:.2f} ({reason})"
        )

        self.logger.info(f"Closed position {market_id}: P&L ${pnl:.2f}, reason: {reason}")

    def get_portfolio_status(self):
        """
        Get portfolio status with basic risk metrics.
        """
        return self.risk_manager.get_portfolio_status()


