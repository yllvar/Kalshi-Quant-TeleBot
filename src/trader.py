import pandas as pd
import numpy as np
import logging
from config import BANKROLL, NEWS_SENTIMENT_THRESHOLD, STAT_ARBITRAGE_THRESHOLD, VOLATILITY_THRESHOLD, MAX_POSITION_SIZE_PERCENTAGE, STOP_LOSS_PERCENTAGE
from news_analyzer import NewsSentimentAnalyzer

class Trader:
    def __init__(self, api, notifier, logger, bankroll):
        self.api = api
        self.notifier = notifier
        self.logger = logger
        self.bankroll = bankroll
        self.current_positions = {}
        self.news_analyzer = NewsSentimentAnalyzer()

    def analyze_market(self, market_data):
        # Enhanced analysis with news sentiment
        return self._make_trade_decision(market_data)

    def _make_trade_decision(self, market_data):
        """
        Enhanced trade decision making with news sentiment analysis
        """
        trade_decision = None

        # Get news sentiment analysis
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

                        self.logger.info(f"News sentiment trade decision: {action} {event_id} "
                                       f"at {current_price} (sentiment: {sentiment_decision['sentiment_score']:.3f})")

        except Exception as e:
            self.logger.error(f"Error in news sentiment analysis: {e}")

        return trade_decision

    def execute_trade(self, trade_decision):
        if not trade_decision:
            self.logger.info("No trade decision to execute.")
            return

        event_id = trade_decision['event_id']
        action = trade_decision['action']
        quantity = trade_decision['quantity']
        price = trade_decision['price']

        # Risk Management: Position Sizing
        max_trade_value = self.bankroll * MAX_POSITION_SIZE_PERCENTAGE
        if (quantity * price) > max_trade_value:
            self.logger.warning(f"Trade value ({quantity * price}) exceeds max position size ({max_trade_value}). Adjusting quantity.")
            quantity = int(max_trade_value / price)
            if quantity == 0:
                self.logger.warning("Adjusted quantity is zero. Skipping trade.")
                return

        try:
            if action == 'buy':
                self.logger.info(f"Executing buy trade for event {event_id} at price {price} for {quantity} units.")
                # Simulate API call
                # self.api.buy_contract(event_id, quantity, price)
                self.current_positions[event_id] = self.current_positions.get(event_id, 0) + quantity
                self.notifier.send_trade_notification(f"Bought {quantity} units of {event_id} at {price}.")
            elif action == 'sell':
                self.logger.info(f"Executing sell trade for event {event_id} at price {price} for {quantity} units.")
                # Simulate API call
                # self.api.sell_contract(event_id, quantity, price)
                self.current_positions[event_id] = self.current_positions.get(event_id, 0) - quantity
                self.notifier.send_trade_notification(f"Sold {quantity} units of {event_id} at {price}.")

            # Risk Management: Stop-Loss (simplified, would need real-time price monitoring)
            if event_id in self.current_positions and self.current_positions[event_id] > 0:
                # This is a very simplified stop-loss. In a real bot, you'd monitor the price
                # and compare it to the entry price. For now, just a placeholder.
                pass

        except Exception as e:
            self.logger.error(f"Error executing trade for {event_id}: {e}")
            self.notifier.send_error_notification(f"Trade execution error for {event_id}: {e}")

    # Placeholder methods for future strategies - will be implemented in Phase 1
    def _news_sentiment_analysis(self, news_data):
        """
        Placeholder for news sentiment analysis - now handled by NewsSentimentAnalyzer
        This method is kept for backward compatibility but delegates to the new analyzer
        """
        self.logger.info("News sentiment analysis now handled by NewsSentimentAnalyzer")
        return 0.7  # Default positive sentiment

    def _statistical_arbitrage(self, related_market_data):
        """
        Placeholder for statistical arbitrage - to be implemented in Phase 1.2
        """
        self.logger.info("Statistical arbitrage analysis - placeholder implementation")
        return None

    def _volatility_analysis(self, historical_prices):
        """
        Placeholder for volatility analysis - to be implemented in Phase 1.3
        """
        self.logger.info("Volatility analysis - placeholder implementation")
        return None

    def run_trading_strategy(self):
        """
        Main trading strategy orchestration
        """
        self.logger.info("Running enhanced trading strategy with news sentiment analysis")

        # Get market data from API
        market_data = self.api.fetch_market_data()
        if not market_data:
            self.logger.info("No market data available")
            return

        # Run news sentiment analysis (primary strategy for Phase 1)
        trade_decision = self._make_trade_decision(market_data)

        if trade_decision:
            self.logger.info(f"Executing trade based on strategy: {trade_decision.get('strategy', 'unknown')}")
            self.execute_trade(trade_decision)
        else:
            self.logger.info("No profitable trade opportunities found")


