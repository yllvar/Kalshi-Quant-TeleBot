import os

def _get_env(name, default):
    return os.environ.get(name, default)

KALSHI_API_KEY = _get_env("KALSHI_API_KEY", "your_kalshi_api_key")
KALSHI_API_BASE_URL = _get_env("KALSHI_API_BASE_URL", "https://api.elections.kalshi.com/trade-api/v2")
TELEGRAM_BOT_TOKEN = _get_env("TELEGRAM_BOT_TOKEN", "your_telegram_bot_token")
TELEGRAM_CHAT_ID = _get_env("TELEGRAM_CHAT_ID", "your_chat_id")

# News API Configuration
NEWS_API_KEY = _get_env("NEWS_API_KEY", "your_news_api_key")
NEWS_API_BASE_URL = "https://newsapi.org/v2"

BANKROLL = 1000
RISK_FACTOR = 1.0
VOLATILITY_PENALTY = True
MIN_DATA_POINTS = 10
TRADE_INTERVAL_SECONDS = 300

# Logging configuration
LOG_FILE_PATH = "trading_bot.log"
LOG_LEVEL = "INFO"

# Error handling settings
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5

# Notification settings
ENABLE_NOTIFICATIONS = True
NOTIFICATION_THRESHOLD = 0.05  # Notify if profit/loss exceeds this percentage

# Advanced Strategy Parameters
NEWS_SENTIMENT_THRESHOLD = 0.6  # Threshold for positive sentiment to trigger a trade
STAT_ARBITRAGE_THRESHOLD = 0.05 # Price deviation for statistical arbitrage
VOLATILITY_THRESHOLD = 0.1     # Volatility threshold for trading

# Risk Management Parameters
MAX_POSITION_SIZE_PERCENTAGE = 0.10 # Max percentage of bankroll to commit to a single trade
STOP_LOSS_PERCENTAGE = 0.05         # Percentage loss at which to close a position


