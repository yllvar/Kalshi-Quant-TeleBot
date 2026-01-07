# Kalshi Advanced Quantitative Trading Bot


## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Telegram Bot Interface](#telegram-bot-interface)
8. [Trading Strategies](#trading-strategies)
9. [Risk Management](#risk-management)
10. [API Documentation](#api-documentation)
11. [Development](#development)
12. [Testing](#testing)
13. [Deployment](#deployment)
14. [Troubleshooting](#troubleshooting)
15. [Contributing](#contributing)
16. [License](#license)

## Overview

The Kalshi Advanced Quantitative Trading Bot is a professional-grade automated trading system designed specifically for event-based markets on the Kalshi platform. This bot leverages advanced quantitative strategies, machine learning techniques, and real-time data analysis to identify profitable trading opportunities while maintaining robust risk management protocols.

Built with a modular architecture, the system combines Python-based trading algorithms with a JavaScript Telegram bot interface for dynamic monitoring and interaction. The bot is designed to operate continuously, making data-driven decisions based on news sentiment analysis, statistical arbitrage opportunities, and volatility patterns in event-based markets.

### Key Differentiators

Unlike traditional stock trading bots, this system is specifically optimized for event-based markets where outcomes are binary and time-sensitive. The bot excels at processing real-time information, analyzing market sentiment, and identifying mispricings in prediction markets. The integration of a sophisticated Telegram interface allows for real-time monitoring, manual intervention, and comprehensive performance tracking.

### Current Implementation Status 🚧

**✅ COMPLETED FEATURES:**
- **Telegram Bot Interface**: All commands implemented with real-time data
- **Kalshi API Integration**: Full API connectivity with error handling
- **Node.js Interface Server**: REST API and WebSocket support
- **Railway Deployment**: Production hosting with 24/7 uptime
- **Basic Trading Infrastructure**: Logging, notifications, configuration

**✅ PHASE 1 COMPLETE:**
- **News Sentiment Strategy**: NLP-powered trading signals
- **Statistical Arbitrage**: Cointegration-based opportunities  
- **Volatility Trading**: GARCH-based volatility analysis

**✅ PHASE 2 COMPLETE:**
- **Kelly Criterion**: Optimal position sizing
- **Stop-Loss Protection**: Automatic loss prevention
- **Risk Metrics**: Sharpe ratio, max drawdown, win rate

**✅ PHASE 3 COMPLETE:**
- **Real-Time Market Data**: Streaming with movement alerts
- **Advanced Performance Analytics**: Trade-by-trade P&L tracking
- **Strategy Backtesting**: Performance attribution & benchmarking

**✅ PHASE 4 COMPLETE:**
- **Dynamic Settings Management**: Real-time parameter adjustment
- **Real-Time Dashboard**: Live P&L updates and position monitoring
- **Advanced Reporting**: Detailed trade logs and strategy breakdowns

**🏆 FULLY FEATURED ENTERPRISE-GRADE QUANTITATIVE TRADING SYSTEM**

**🎉 ALL PHASES COMPLETE - Enterprise-Grade Trading Bot Ready!**

📋 **For detailed implementation roadmap, see:** [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md)

## Features

### Core Trading Capabilities
- **Advanced Quantitative Strategies**: Implementation of multiple sophisticated trading algorithms including news sentiment analysis, statistical arbitrage, and volatility-based trading
- **Real-time Market Monitoring**: Continuous monitoring of Kalshi markets with sub-second response times
- **Intelligent Position Sizing**: Dynamic position sizing based on confidence levels, market volatility, and available capital
- **Comprehensive Risk Management**: Multi-layered risk controls including stop-losses, position limits, and exposure management
- **Event Correlation Analysis**: Identification and exploitation of relationships between related events

### Technology Stack
- **Python Backend**: High-performance trading engine with pandas, numpy, and scikit-learn integration
- **JavaScript Telegram Interface**: Real-time monitoring and control via Telegram bot with rich interactive features
- **WebSocket Communication**: Real-time data streaming between components
- **RESTful API**: Comprehensive API for external integrations and monitoring
- **Modular Architecture**: Easily extensible design for adding new strategies and features

### Monitoring and Control
- **Real-time Performance Metrics**: Live tracking of P&L, win rates, Sharpe ratios, and other key performance indicators
- **Interactive Telegram Bot**: Full-featured bot interface for monitoring positions, executing commands, and receiving alerts
- **Comprehensive Logging**: Detailed logging of all trading activities, errors, and system events
- **Alert System**: Configurable alerts for significant events, errors, and performance milestones

## Architecture

The system follows a microservices architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Kalshi Trading Bot System                    │
├─────────────────────────────────────────────────────────────────┤
│  Telegram Bot UI (JavaScript)                                  │
│  ├── Interactive Commands                                      │
│  ├── Real-time Notifications                                   │
│  ├── Performance Monitoring                                    │
│  └── Configuration Management                                  │
├─────────────────────────────────────────────────────────────────┤
│  Bot Interface Layer (Node.js)                                 │
│  ├── WebSocket Server                                          │
│  ├── REST API                                                  │
│  ├── Process Management                                        │
│  └── Real-time Communication                                   │
├─────────────────────────────────────────────────────────────────┤
│  Core Trading Engine (Python)                                  │
│  ├── Strategy Execution Module                                 │
│  ├── Risk Management Module                                    │
│  ├── Data Ingestion Module                                     │
│  ├── Trade Execution Module                                    │
│  └── Logging & Monitoring                                      │
├─────────────────────────────────────────────────────────────────┤
│  External Integrations                                         │
│  ├── Kalshi API                                                │
│  ├── News Data Sources                                         │
│  ├── Social Media Feeds                                        │
│  └── Market Data Providers                                     │
└─────────────────────────────────────────────────────────────────┘
```

### Component Descriptions

**Trading Engine (Python)**: The core of the system, responsible for strategy execution, risk management, and trade execution. Built with high-performance libraries for numerical computing and data analysis.

**Bot Interface Layer (Node.js)**: Provides communication bridge between the Python trading engine and external interfaces. Handles WebSocket connections, REST API endpoints, and process management.

**Telegram Bot UI (JavaScript)**: User-facing interface providing real-time monitoring, control capabilities, and alert management through Telegram's messaging platform.

**Data Ingestion**: Handles collection and preprocessing of market data, news feeds, and other relevant information sources required for trading decisions.

## Installation

### Prerequisites

Before installing the Kalshi Trading Bot, ensure your system meets the following requirements:

- **Operating System**: Linux (Ubuntu 20.04+ recommended), macOS 10.15+, or Windows 10+ with WSL2
- **Python**: Version 3.8 or higher
- **Node.js**: Version 16.0 or higher
- **Memory**: Minimum 4GB RAM (8GB recommended for optimal performance)
- **Storage**: At least 2GB free disk space
- **Network**: Stable internet connection with low latency

### System Dependencies

Install required system packages:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip nodejs npm git curl

# macOS (using Homebrew)
brew install python3 node git

# Verify installations
python3 --version
node --version
npm --version
```

### Clone Repository

```bash
git clone https://github.com/LoQiseaking69/kalshi-trading-bot.git
cd kalshi-trading-bot
```

### Python Environment Setup

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv kalshi_env

# Activate virtual environment
# On Linux/macOS:
source kalshi_env/bin/activate
# On Windows:
kalshi_env\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### Node.js Dependencies

Install JavaScript dependencies for the Telegram bot interface:

```bash
cd telegram_ui
npm install
cd ..
```

### Verify Installation

Run the installation verification script:

```bash
python3 -c "import pandas, numpy, requests; print('Python dependencies installed successfully')"
cd telegram_ui && node -e "console.log('Node.js dependencies installed successfully')" && cd ..
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory based on the provided template:

```bash
cp telegram_ui/.env.example .env
```

Edit the `.env` file with your specific configuration:

```env
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here

# Kalshi API Configuration
KALSHI_API_KEY=your_kalshi_api_key_here
KALSHI_API_BASE_URL=https://api.elections.kalshi.com/trade-api/v2

# Trading Configuration
BANKROLL=1000
TRADE_INTERVAL_SECONDS=60
MAX_POSITION_SIZE_PERCENTAGE=0.10
STOP_LOSS_PERCENTAGE=0.05
NEWS_SENTIMENT_THRESHOLD=0.6
STAT_ARBITRAGE_THRESHOLD=0.05
VOLATILITY_THRESHOLD=0.1
```

### Obtaining API Keys

#### Kalshi API Key
1. Visit [Kalshi.com](https://kalshi.com) and create an account
2. Navigate to your account settings
3. Generate an API key in the developer section
4. Copy the API key to your `.env` file

#### Telegram Bot Token
1. Open Telegram and search for @BotFather
2. Send `/newbot` command and follow the instructions
3. Choose a name and username for your bot
4. Copy the provided token to your `.env` file
5. To get your chat ID, send a message to your bot and visit:
   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`

### Configuration Parameters

The system supports extensive configuration through the `src/config.py` file:

```python
# Trading Parameters
BANKROLL = 1000                    # Initial trading capital
TRADE_INTERVAL_SECONDS = 60        # Time between trading cycles
MAX_POSITION_SIZE_PERCENTAGE = 0.10 # Maximum position size as % of bankroll
STOP_LOSS_PERCENTAGE = 0.05        # Stop loss threshold

# Strategy Parameters
NEWS_SENTIMENT_THRESHOLD = 0.6     # Minimum sentiment score for trades
STAT_ARBITRAGE_THRESHOLD = 0.05    # Price deviation threshold for arbitrage
VOLATILITY_THRESHOLD = 0.1         # Volatility threshold for trading

# Risk Management
MAX_DAILY_LOSS = 0.02              # Maximum daily loss as % of bankroll
MAX_OPEN_POSITIONS = 10            # Maximum number of concurrent positions
CORRELATION_LIMIT = 0.7            # Maximum correlation between positions
```

## Usage

### Starting the Trading Bot

#### Method 1: Full System Startup

Start both the Python trading engine and Telegram bot interface:

```bash
# Start the bot interface (this will manage the Python bot)
cd telegram_ui
npm start
```

#### Method 2: Manual Component Startup

Start components individually for development or debugging:

```bash
# Terminal 1: Start Python trading engine
python3 src/main.py

# Terminal 2: Start Telegram bot interface
cd telegram_ui
node telegram_bot.js

# Terminal 3: Start bot interface API
node bot_interface.js
```

### Basic Operations

Once the system is running, you can interact with it through Telegram:

1. **Start the bot**: Send `/start` to your Telegram bot
2. **Check status**: Use `/status` to see current bot status
3. **View positions**: Send `/positions` to see open positions
4. **Check balance**: Use `/balance` to view account information
5. **Start trading**: Send `/start_trading` to begin automated trading
6. **Stop trading**: Use `/stop_trading` to halt trading operations

### Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Initialize bot and show main menu | `/start` |
| `/status` | Display current bot status | `/status` |
| `/positions` | Show all open positions | `/positions` |
| `/balance` | Display account balance and P&L | `/balance` |
| `/start_trading` | Begin automated trading | `/start_trading` |
| `/stop_trading` | Stop all trading activities | `/stop_trading` |
| `/performance` | Show performance metrics | `/performance` |
| `/settings` | View and modify configuration | `/settings` |
| `/help` | Display help information | `/help` |

### Monitoring and Alerts

The system provides comprehensive monitoring capabilities:

- **Real-time Notifications**: Receive instant alerts for trades, errors, and significant events
- **Performance Tracking**: Monitor key metrics including P&L, win rate, and Sharpe ratio
- **Position Management**: Track all open positions with real-time P&L updates
- **Risk Monitoring**: Alerts for risk limit breaches and unusual market conditions

## Telegram Bot Interface

The Telegram bot interface provides a sophisticated control panel for monitoring and managing the trading bot. The interface is designed for both novice and experienced traders, offering intuitive commands alongside advanced configuration options.

### Interactive Features

#### Main Menu
The bot provides an interactive main menu with quick access buttons:
- 📊 Status: Current bot status and health
- 💰 Balance: Account balance and P&L information
- 📈 Positions: All open positions with real-time updates
- 📊 Performance: Detailed performance metrics
- ▶️ Start Trading: Begin automated trading
- ⏹️ Stop Trading: Stop all trading activities
- ⚙️ Settings: Configuration management
- ❓ Help: Comprehensive help documentation

#### Real-time Notifications

The bot sends automatic notifications for:
- **Trade Executions**: Detailed information about each trade including event, action, quantity, and price
- **Performance Milestones**: Alerts when reaching profit/loss thresholds
- **Risk Events**: Notifications when risk limits are approached or breached
- **System Events**: Bot startup, shutdown, and error conditions
- **Market Opportunities**: Alerts for high-confidence trading opportunities

#### Advanced Commands

Beyond basic commands, the bot supports advanced functionality:
- **Configuration Management**: Modify trading parameters in real-time
- **Manual Trading**: Execute manual trades through the interface
- **Strategy Control**: Enable/disable specific trading strategies
- **Risk Adjustment**: Modify risk parameters based on market conditions

### Customization Options

The Telegram interface can be customized to match individual preferences:
- **Alert Frequency**: Configure how often to receive updates
- **Notification Types**: Choose which events trigger notifications
- **Display Format**: Customize how information is presented
- **Language Settings**: Support for multiple languages (extensible)

## Trading Strategies

The bot implements multiple sophisticated trading strategies, each designed to exploit different market inefficiencies and opportunities in event-based markets.

### News Sentiment Analysis Strategy

This strategy leverages Natural Language Processing (NLP) to analyze news articles, social media posts, and other textual data sources to gauge market sentiment and predict event outcomes.

#### Methodology
The strategy operates through several key phases:

**Data Collection**: The system continuously monitors multiple news sources, including major news outlets, financial news services, and relevant social media feeds. Data is collected in real-time using RSS feeds, APIs, and web scraping techniques where appropriate.

**Text Preprocessing**: Raw text data undergoes extensive preprocessing including tokenization, stop word removal, stemming, and normalization. The system also handles multiple languages and can process various text formats.

**Sentiment Analysis**: Advanced NLP models, including pre-trained transformer models and custom-trained classifiers, analyze the sentiment of collected text. The system generates sentiment scores ranging from -1 (extremely negative) to +1 (extremely positive).

**Event Correlation**: Sentiment scores are correlated with specific events listed on Kalshi. The system maintains a mapping between keywords, entities, and events to ensure accurate attribution of sentiment to relevant markets.

**Signal Generation**: When sentiment scores exceed predefined thresholds and show statistical significance, the system generates trading signals. The strength of the signal is proportional to the sentiment score and the confidence level of the analysis.

#### Implementation Details
```python
def analyze_news_sentiment(self, news_data, event_keywords):
    """
    Analyze sentiment of news data related to specific events
    """
    sentiment_scores = []
    for article in news_data:
        # Preprocess text
        cleaned_text = self.preprocess_text(article['content'])
        
        # Check relevance to event
        relevance_score = self.calculate_relevance(cleaned_text, event_keywords)
        
        if relevance_score > self.relevance_threshold:
            # Analyze sentiment
            sentiment = self.sentiment_model.predict(cleaned_text)
            weighted_sentiment = sentiment * relevance_score
            sentiment_scores.append(weighted_sentiment)
    
    # Aggregate sentiment scores
    if sentiment_scores:
        avg_sentiment = np.mean(sentiment_scores)
        confidence = self.calculate_confidence(sentiment_scores)
        return avg_sentiment, confidence
    
    return 0, 0
```

### Statistical Arbitrage Strategy

Statistical arbitrage exploits pricing discrepancies between related events or contracts. This strategy is particularly effective in prediction markets where multiple contracts may be related to the same underlying phenomenon.

#### Core Concepts
The strategy identifies situations where the combined probabilities of related events don't sum to 100%, or where correlated events show pricing inconsistencies that can be exploited through simultaneous long and short positions.

**Correlation Analysis**: The system continuously analyzes historical price movements between different event contracts to identify strong correlations. Events that typically move together (positive correlation) or in opposite directions (negative correlation) are flagged for arbitrage opportunities.

**Price Relationship Modeling**: Using statistical techniques such as cointegration analysis and regression modeling, the system establishes expected price relationships between correlated events. When actual prices deviate significantly from these expected relationships, arbitrage opportunities are identified.

**Risk-Neutral Arbitrage**: The strategy attempts to construct risk-neutral portfolios by taking offsetting positions in related contracts. This approach aims to profit from price convergence while minimizing exposure to the actual event outcomes.

#### Example Implementation
Consider two related political events: "Candidate A wins primary" and "Candidate A wins general election." The probability of winning the general election cannot exceed the probability of winning the primary. If market prices suggest otherwise, an arbitrage opportunity exists.

```python
def identify_arbitrage_opportunity(self, primary_contract, general_contract):
    """
    Identify arbitrage opportunities between related political contracts
    """
    primary_prob = primary_contract.yes_price / (primary_contract.yes_price + primary_contract.no_price)
    general_prob = general_contract.yes_price / (general_contract.yes_price + general_contract.no_price)
    
    # General election probability should not exceed primary probability
    if general_prob > primary_prob + self.arbitrage_threshold:
        # Arbitrage opportunity: sell general election, buy primary
        return {
            'action': 'arbitrage',
            'long_contract': primary_contract,
            'short_contract': general_contract,
            'expected_profit': (general_prob - primary_prob) * self.position_size,
            'confidence': self.calculate_arbitrage_confidence(primary_contract, general_contract)
        }
    
    return None
```

### Volatility-Based Strategy

This strategy capitalizes on volatility patterns in event contract prices, identifying opportunities when volatility is unusually high or low relative to historical norms.

#### Volatility Measurement
The system calculates multiple volatility metrics:
- **Historical Volatility**: Standard deviation of price changes over various time periods
- **Implied Volatility**: Derived from option-like characteristics of event contracts
- **Realized Volatility**: Actual price movements compared to expected movements

#### Trading Logic
High volatility periods often present opportunities to sell overpriced contracts, while low volatility periods may offer chances to buy underpriced contracts before significant price movements.

**Mean Reversion**: When volatility is extremely high, the strategy may take positions expecting prices to revert to historical means.

**Momentum Trading**: During periods of sustained directional movement with increasing volatility, the strategy may take positions in the direction of the trend.

**Volatility Breakouts**: The system identifies periods of low volatility followed by sudden increases, often indicating significant new information entering the market.

## Risk Management

Comprehensive risk management is fundamental to the bot's design, incorporating multiple layers of protection to preserve capital and ensure sustainable trading operations.

### Position Sizing

The bot employs sophisticated position sizing algorithms that consider multiple factors:

**Kelly Criterion Implementation**: The system uses a modified Kelly Criterion to determine optimal position sizes based on the estimated probability of success and potential payoffs. This mathematical approach maximizes long-term growth while controlling risk.

```python
def calculate_kelly_position_size(self, win_probability, win_amount, loss_amount):
    """
    Calculate optimal position size using Kelly Criterion
    """
    if win_probability <= 0 or win_probability >= 1:
        return 0
    
    # Kelly fraction = (bp - q) / b
    # where b = odds received on the wager
    # p = probability of winning
    # q = probability of losing (1 - p)
    
    b = win_amount / abs(loss_amount)
    kelly_fraction = (win_probability * b - (1 - win_probability)) / b
    
    # Apply conservative scaling factor
    conservative_fraction = kelly_fraction * self.kelly_scaling_factor
    
    # Ensure position size doesn't exceed maximum limits
    max_position = self.bankroll * self.max_position_percentage
    optimal_position = min(conservative_fraction * self.bankroll, max_position)
    
    return max(0, optimal_position)
```

**Volatility Adjustment**: Position sizes are adjusted based on market volatility. During high volatility periods, position sizes are reduced to account for increased uncertainty.

**Correlation Adjustment**: When multiple positions are correlated, the system reduces individual position sizes to maintain overall portfolio risk within acceptable limits.

### Stop-Loss Mechanisms

The bot implements multiple types of stop-loss mechanisms:

**Fixed Percentage Stop-Loss**: Positions are automatically closed when losses exceed a predetermined percentage of the entry price.

**Trailing Stop-Loss**: For profitable positions, the stop-loss level is adjusted upward as the position becomes more profitable, locking in gains while allowing for continued upside.

**Time-Based Stop-Loss**: Positions may be closed based on time decay, particularly important for event contracts with specific expiration dates.

**Volatility-Adjusted Stop-Loss**: Stop-loss levels are adjusted based on current market volatility, providing wider stops during volatile periods and tighter stops during calm markets.

### Portfolio-Level Risk Controls

**Maximum Daily Loss**: The system will halt trading if daily losses exceed a predetermined threshold, preventing catastrophic losses during adverse market conditions.

**Concentration Limits**: No single event or category of events can represent more than a specified percentage of the total portfolio.

**Correlation Monitoring**: The system continuously monitors correlations between positions and adjusts exposure when correlations become too high.

**Drawdown Protection**: If the portfolio experiences a significant drawdown, the system may reduce position sizes or temporarily halt trading to preserve capital.

### Dynamic Risk Adjustment

Risk parameters are not static but adjust based on:
- **Market Conditions**: Risk tolerance increases during stable markets and decreases during volatile periods
- **Performance History**: Recent performance affects risk appetite, with successful periods allowing for slightly increased risk
- **Event Characteristics**: Different types of events (political, economic, weather) may warrant different risk approaches
- **Time to Expiration**: Risk parameters adjust based on how much time remains until event resolution

## API Documentation

The bot provides a comprehensive RESTful API for external integrations, monitoring, and control. The API follows standard REST conventions and returns JSON responses.

### Base URL
```
http://localhost:3001/api
```

### Authentication
Currently, the API uses IP-based authentication for local access. For production deployments, implement proper authentication mechanisms such as API keys or OAuth.

### Endpoints

#### GET /health
Returns the health status of the bot system.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "pythonBot": "running"
}
```

#### GET /status
Returns detailed status information about the trading bot.

**Response:**
```json
{
  "trading": true,
  "lastUpdate": "2024-01-15T10:30:00Z",
  "uptime": "2h 34m",
  "apiConnected": true,
  "activeStrategies": ["News Sentiment", "Statistical Arbitrage"],
  "tradesCount": 12
}
```

#### GET /positions
Returns all current open positions.

**Response:**
```json
[
  {
    "eventName": "Presidential Election 2024",
    "eventId": "PRES2024",
    "quantity": 100,
    "entryPrice": 0.65,
    "currentPrice": 0.72,
    "pnl": 7.00,
    "timestamp": "2024-01-15T10:30:00Z"
  }
]
```

#### GET /balance
Returns account balance and P&L information.

**Response:**
```json
{
  "available": 1250.75,
  "totalEquity": 1348.25,
  "unrealizedPnL": 5.00,
  "todayPnL": 15.30,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### GET /performance
Returns detailed performance metrics.

**Response:**
```json
{
  "totalReturn": 12.5,
  "sharpeRatio": 1.8,
  "maxDrawdown": 3.2,
  "winRate": 68.5,
  "totalTrades": 156,
  "avgTrade": 2.45,
  "bestTrade": 25.80,
  "worstTrade": -8.20,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### POST /start-trading
Starts the automated trading system.

**Response:**
```json
{
  "success": true,
  "message": "Trading started successfully"
}
```

#### POST /stop-trading
Stops the automated trading system.

**Response:**
```json
{
  "success": true,
  "message": "Trading stopped successfully"
}
```

#### GET /config
Returns current bot configuration.

**Response:**
```json
{
  "maxPositionSize": 0.10,
  "stopLoss": 0.05,
  "newsSentimentThreshold": 0.6,
  "statArbitrageThreshold": 0.05,
  "volatilityThreshold": 0.1,
  "tradeInterval": 60
}
```

#### POST /config
Updates bot configuration.

**Request Body:**
```json
{
  "maxPositionSize": 0.15,
  "stopLoss": 0.04
}
```

**Response:**
```json
{
  "success": true,
  "message": "Configuration updated successfully"
}
```

### WebSocket API

The system also provides real-time updates via WebSocket connections at `ws://localhost:3001`.

#### Connection
```javascript
const ws = new WebSocket('ws://localhost:3001');

ws.on('open', () => {
  // Send subscription message
  ws.send(JSON.stringify({ type: 'subscribe' }));
});

ws.on('message', (data) => {
  const message = JSON.parse(data);
  console.log('Received:', message);
});
```

#### Message Types
- `status`: Bot status updates
- `trade_executed`: Trade execution notifications
- `bot_output`: Python bot output logs
- `bot_error`: Error messages
- `config_updated`: Configuration change notifications

## Development

### Development Environment Setup

For development work, set up the environment with additional tools:

```bash
# Install development dependencies
pip install -r requirements-dev.txt
cd telegram_ui && npm install --include=dev

# Install pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/
cd telegram_ui && npm test
```

### Code Structure

```
kalshi-trading-bot/
├── src/                          # Python trading engine
│   ├── main.py                   # Main entry point
│   ├── config.py                 # Configuration management
│   ├── kalshi_api.py            # Kalshi API interface
│   ├── trader.py                # Core trading logic
│   ├── strategies/              # Trading strategies
│   │   ├── sentiment_strategy.py
│   │   ├── arbitrage_strategy.py
│   │   └── volatility_strategy.py
│   ├── risk_management.py       # Risk management module
│   ├── data_ingestion.py        # Data collection and processing
│   ├── notifier.py              # Notification system
│   ├── logger.py                # Logging configuration
│   └── utils.py                 # Utility functions
├── telegram_ui/                 # Telegram bot interface
│   ├── telegram_bot.js          # Main Telegram bot
│   ├── bot_interface.js         # API and WebSocket server
│   ├── package.json             # Node.js dependencies
│   └── .env.example             # Environment variables template
├── tests/                       # Test suite
│   ├── test_trader.py
│   ├── test_strategies.py
│   └── test_risk_management.py
├── docs/                        # Additional documentation
├── requirements.txt             # Python dependencies
├── requirements-dev.txt         # Development dependencies
└── README.md                    # This file
```

### Adding New Strategies

To add a new trading strategy:

1. Create a new file in `src/strategies/`
2. Implement the strategy class with required methods
3. Register the strategy in `src/trader.py`
4. Add configuration parameters to `src/config.py`
5. Write tests in `tests/`

Example strategy template:
```python
class NewStrategy:
    def __init__(self, config):
        self.config = config
    
    def analyze(self, market_data):
        """Analyze market data and return trading signals"""
        pass
    
    def generate_signals(self, analysis_result):
        """Generate specific trading signals"""
        pass
```

### Testing

The project includes comprehensive test suites:

```bash
# Run Python tests
python -m pytest tests/ -v

# Run JavaScript tests
cd telegram_ui && npm test

# Run integration tests
python -m pytest tests/integration/ -v

# Generate coverage report
python -m pytest tests/ --cov=src --cov-report=html
```

### Code Quality

The project maintains high code quality standards:
- **Linting**: flake8 for Python, ESLint for JavaScript
- **Formatting**: Black for Python, Prettier for JavaScript
- **Type Checking**: mypy for Python
- **Pre-commit Hooks**: Automated code quality checks

## Testing

### Unit Tests

Unit tests cover individual components and functions:

```bash
# Test trading strategies
python -m pytest tests/test_strategies.py

# Test risk management
python -m pytest tests/test_risk_management.py

# Test API interface
python -m pytest tests/test_api.py
```

### Integration Tests

Integration tests verify component interactions:

```bash
# Test full trading workflow
python -m pytest tests/integration/test_trading_workflow.py

# Test Telegram bot integration
python -m pytest tests/integration/test_telegram_integration.py
```

### Performance Tests

Performance tests ensure the system meets latency and throughput requirements:

```bash
# Test trading engine performance
python -m pytest tests/performance/test_trading_performance.py

# Test API response times
python -m pytest tests/performance/test_api_performance.py
```

### Backtesting

The system includes backtesting capabilities for strategy validation:

```python
from src.backtesting import Backtester

# Initialize backtester
backtester = Backtester(
    start_date='2023-01-01',
    end_date='2023-12-31',
    initial_capital=10000
)

# Run backtest
results = backtester.run_strategy('sentiment_strategy')
print(f"Total Return: {results.total_return:.2%}")
print(f"Sharpe Ratio: {results.sharpe_ratio:.2f}")
print(f"Max Drawdown: {results.max_drawdown:.2%}")
```

## Deployment

### Production Deployment

For production deployment, follow these steps:

#### 1. Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install python3 python3-pip nodejs npm nginx supervisor

# Create application user
sudo useradd -m -s /bin/bash kalshi-bot
sudo su - kalshi-bot
```

#### 2. Application Deployment
```bash
# Clone repository
git clone https://github.com/your-username/kalshi-trading-bot.git
cd kalshi-trading-bot

# Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up Node.js environment
cd telegram_ui
npm install --production
cd ..

# Configure environment
cp telegram_ui/.env.example .env
# Edit .env with production values
```

#### 3. Process Management
Create supervisor configuration:

```ini
# /etc/supervisor/conf.d/kalshi-bot.conf
[program:kalshi-trading-bot]
command=/home/kalshi-bot/kalshi-trading-bot/venv/bin/python src/main.py
directory=/home/kalshi-bot/kalshi-trading-bot
user=kalshi-bot
autostart=true
autorestart=true
stderr_logfile=/var/log/kalshi-bot/trading-bot.err.log
stdout_logfile=/var/log/kalshi-bot/trading-bot.out.log

[program:kalshi-telegram-bot]
command=/usr/bin/node telegram_bot.js
directory=/home/kalshi-bot/kalshi-trading-bot/telegram_ui
user=kalshi-bot
autostart=true
autorestart=true
stderr_logfile=/var/log/kalshi-bot/telegram-bot.err.log
stdout_logfile=/var/log/kalshi-bot/telegram-bot.out.log

[program:kalshi-bot-interface]
command=/usr/bin/node bot_interface.js
directory=/home/kalshi-bot/kalshi-trading-bot/telegram_ui
user=kalshi-bot
autostart=true
autorestart=true
stderr_logfile=/var/log/kalshi-bot/bot-interface.err.log
stdout_logfile=/var/log/kalshi-bot/bot-interface.out.log
```

#### 4. Nginx Configuration
```nginx
# /etc/nginx/sites-available/kalshi-bot
server {
    listen 80;
    server_name your-domain.com;

    location /api/ {
        proxy_pass http://localhost:3001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /ws {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

#### 5. SSL Configuration
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Obtain SSL certificate
sudo certbot --nginx -d your-domain.com

# Verify auto-renewal
sudo certbot renew --dry-run
```

### Docker Deployment

For containerized deployment:

```dockerfile
# Dockerfile
FROM python:3.9-slim

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy and install Node.js dependencies
COPY telegram_ui/package*.json telegram_ui/
RUN cd telegram_ui && npm install --production

# Copy application code
COPY . .

# Expose ports
EXPOSE 3001

# Start application
CMD ["python", "src/main.py"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  kalshi-bot:
    build: .
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - KALSHI_API_KEY=${KALSHI_API_KEY}
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    restart: unless-stopped
    ports:
      - "3001:3001"
```

### Monitoring and Logging

#### Log Management
```bash
# Create log directories
sudo mkdir -p /var/log/kalshi-bot
sudo chown kalshi-bot:kalshi-bot /var/log/kalshi-bot

# Configure log rotation
sudo tee /etc/logrotate.d/kalshi-bot << EOF
/var/log/kalshi-bot/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 kalshi-bot kalshi-bot
    postrotate
        supervisorctl restart kalshi-trading-bot kalshi-telegram-bot kalshi-bot-interface
    endscript
}
EOF
```

#### Health Monitoring
Set up monitoring with tools like Prometheus and Grafana:

```python
# Add to src/monitoring.py
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Metrics
trades_total = Counter('kalshi_trades_total', 'Total number of trades')
trade_duration = Histogram('kalshi_trade_duration_seconds', 'Trade execution time')
account_balance = Gauge('kalshi_account_balance', 'Current account balance')
open_positions = Gauge('kalshi_open_positions', 'Number of open positions')

# Start metrics server
start_http_server(8000)
```

## Troubleshooting

### Common Issues

#### 1. API Connection Errors
**Symptoms**: Bot fails to connect to Kalshi API
**Solutions**:
- Verify API key is correct and active
- Check network connectivity
- Ensure API endpoints are accessible
- Review rate limiting settings

```bash
# Test API connectivity
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.elections.kalshi.com/trade-api/v2/markets
```

#### 2. Telegram Bot Not Responding
**Symptoms**: Telegram bot doesn't respond to commands
**Solutions**:
- Verify bot token is correct
- Check if bot is running
- Ensure webhook is not set (for polling mode)
- Review Telegram API limits

```bash
# Check bot status
curl https://api.telegram.org/botYOUR_BOT_TOKEN/getMe
```

#### 3. High Memory Usage
**Symptoms**: System runs out of memory
**Solutions**:
- Implement data cleanup routines
- Optimize data structures
- Add memory monitoring
- Consider increasing system memory

```python
# Add memory monitoring
import psutil
import gc

def monitor_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    print(f"Memory usage: {memory_info.rss / 1024 / 1024:.2f} MB")
    
    if memory_info.rss > 1024 * 1024 * 1024:  # 1GB
        gc.collect()  # Force garbage collection
```

#### 4. Trading Strategy Errors
**Symptoms**: Strategies produce unexpected results
**Solutions**:
- Review strategy parameters
- Check data quality
- Validate market conditions
- Run backtests to verify logic

### Debugging Tools

#### 1. Logging Configuration
```python
import logging

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)
```

#### 2. Performance Profiling
```python
import cProfile
import pstats

# Profile trading function
profiler = cProfile.Profile()
profiler.enable()

# Run trading logic
trader.run_trading_strategy()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

#### 3. Market Data Validation
```python
def validate_market_data(data):
    """Validate market data integrity"""
    required_fields = ['id', 'title', 'yes_price', 'no_price']
    
    for market in data.get('markets', []):
        for field in required_fields:
            if field not in market:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate price ranges
        if not (0 <= market['yes_price'] <= 1):
            raise ValueError(f"Invalid yes_price: {market['yes_price']}")
        
        if not (0 <= market['no_price'] <= 1):
            raise ValueError(f"Invalid no_price: {market['no_price']}")
```

### Performance Optimization

#### 1. Database Optimization
```python
# Use connection pooling
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    'postgresql://user:pass@localhost/kalshi',
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

#### 2. Caching Implementation
```python
from functools import lru_cache
import redis

# Redis cache
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@lru_cache(maxsize=1000)
def get_market_data(market_id):
    """Cache market data to reduce API calls"""
    cached_data = redis_client.get(f"market:{market_id}")
    if cached_data:
        return json.loads(cached_data)
    
    # Fetch from API
    data = api.get_market(market_id)
    redis_client.setex(f"market:{market_id}", 60, json.dumps(data))
    return data
```

#### 3. Asynchronous Processing
```python
import asyncio
import aiohttp

async def fetch_multiple_markets(market_ids):
    """Fetch multiple markets concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_market(session, market_id) for market_id in market_ids]
        results = await asyncio.gather(*tasks)
        return results

async def fetch_market(session, market_id):
    """Fetch single market data"""
    url = f"https://api.elections.kalshi.com/trade-api/v2/markets/{market_id}"
    async with session.get(url) as response:
        return await response.json()
```

## Contributing

We welcome contributions to the Kalshi Trading Bot project. Please follow these guidelines:

### Development Workflow

1. **Fork the Repository**: Create a fork of the main repository
2. **Create Feature Branch**: Create a new branch for your feature or bug fix
3. **Make Changes**: Implement your changes with appropriate tests
4. **Run Tests**: Ensure all tests pass
5. **Submit Pull Request**: Create a pull request with a clear description

### Code Standards

- **Python**: Follow PEP 8 style guidelines
- **JavaScript**: Follow ESLint configuration
- **Documentation**: Update documentation for new features
- **Tests**: Include tests for new functionality

### Contribution Areas

- **New Trading Strategies**: Implement additional quantitative strategies
- **Data Sources**: Add new data sources for analysis
- **UI Improvements**: Enhance the Telegram bot interface
- **Performance Optimization**: Improve system performance
- **Documentation**: Improve documentation and examples

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Disclaimer**: This trading bot is for educational and research purposes. Trading involves risk, and past performance does not guarantee future results. Users should thoroughly test the system and understand the risks before deploying with real capital.
