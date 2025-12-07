import time
import logging
from config import KALSHI_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, BANKROLL, TRADE_INTERVAL_SECONDS
from kalshi_api import KalshiAPI
from trader import Trader
from notifier import Notifier
from logger import Logger

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = Logger()
    return logger

def main():
    logger = setup_logging()
    logger.info("Starting Kalshi Advanced Trading Bot with Phase 3 features")

    try:
        api = KalshiAPI(KALSHI_API_KEY)
        notifier = Notifier(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
        trader = Trader(api, notifier, logger, BANKROLL)

        # Start market data streaming (Phase 3 feature)
        trader.market_data_streamer.start_streaming()
        logger.info("Market data streaming started")

        while True:
            logger.info("Running trading strategy with real-time market data")
            trader.run_trading_strategy()
            time.sleep(TRADE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        logger.info("Bot shutdown requested by user")
        trader.market_data_streamer.stop_streaming()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        notifier.send_error_notification(str(e))
        trader.market_data_streamer.stop_streaming()
        raise
    finally:
        trader.market_data_streamer.stop_streaming()
        logger.info("Market data streaming stopped")

if __name__ == "__main__":
    main()
