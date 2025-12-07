#!/usr/bin/env python3
"""Advanced performance analytics module for Phase 3 - Kalshi trading bot."""

import logging
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict

logger = logging.getLogger(__name__)

@dataclass
class Trade:
    """Individual trade record."""
    trade_id: str
    market_id: str
    strategy: str
    side: str  # 'buy' or 'sell'
    quantity: int
    entry_price: float
    exit_price: Optional[float] = None
    entry_time: datetime = None
    exit_time: Optional[datetime] = None
    pnl: Optional[float] = None
    pnl_pct: Optional[float] = None
    holding_period: Optional[float] = None  # hours
    exit_reason: Optional[str] = None
    confidence: Optional[float] = None

    def __post_init__(self):
        if self.entry_time is None:
            self.entry_time = datetime.now()

    @property
    def is_closed(self) -> bool:
        """Check if trade is closed."""
        return self.exit_price is not None

    def close_trade(self, exit_price: float, exit_reason: str = 'manual'):
        """Close the trade and calculate P&L."""
        self.exit_price = exit_price
        self.exit_time = datetime.now()
        self.exit_reason = exit_reason

        # Calculate P&L
        if self.side.lower() == 'buy':
            self.pnl = (exit_price - self.entry_price) * self.quantity
        else:  # sell/short
            self.pnl = (self.entry_price - exit_price) * self.quantity

        # Calculate percentage return
        entry_value = self.entry_price * self.quantity
        if entry_value != 0:
            self.pnl_pct = (self.pnl / entry_value) * 100

        # Calculate holding period
        if self.exit_time and self.entry_time:
            self.holding_period = (self.exit_time - self.entry_time).total_seconds() / 3600

class PerformanceAnalytics:
    """Advanced performance analytics and reporting."""

    def __init__(self):
        self.trades: List[Trade] = []
        self.daily_pnl: Dict[str, float] = defaultdict(float)
        self.strategy_performance: Dict[str, Dict[str, Any]] = defaultdict(dict)

    def record_trade(self, trade: Trade):
        """Record a new trade."""
        self.trades.append(trade)
        logger.info(f"Recorded trade: {trade.strategy} {trade.side} {trade.quantity} "
                   f"units of {trade.market_id} at ${trade.entry_price:.2f}")

    def close_trade(self, trade_id: str, exit_price: float, exit_reason: str = 'manual'):
        """Close an existing trade."""
        for trade in self.trades:
            if trade.trade_id == trade_id and not trade.is_closed:
                trade.close_trade(exit_price, exit_reason)

                # Update daily P&L
                date_key = trade.exit_time.strftime('%Y-%m-%d')
                self.daily_pnl[date_key] += trade.pnl

                logger.info(f"Closed trade {trade_id}: P&L ${trade.pnl:.2f} ({trade.pnl_pct:.2f}%)")
                return True

        logger.warning(f"Trade {trade_id} not found or already closed")
        return False

    def get_trade_statistics(self) -> Dict[str, Any]:
        """Get comprehensive trade statistics."""
        if not self.trades:
            return {'total_trades': 0}

        closed_trades = [t for t in self.trades if t.is_closed]

        if not closed_trades:
            return {
                'total_trades': len(self.trades),
                'open_trades': len(self.trades),
                'closed_trades': 0
            }

        # Basic counts
        winning_trades = [t for t in closed_trades if t.pnl > 0]
        losing_trades = [t for t in closed_trades if t.pnl <= 0]

        # Profit/Loss statistics
        total_pnl = sum(t.pnl for t in closed_trades)
        total_return_pct = sum(t.pnl_pct for t in closed_trades)

        # Win rate
        win_rate = len(winning_trades) / len(closed_trades)

        # Average P&L
        avg_win = np.mean([t.pnl for t in winning_trades]) if winning_trades else 0
        avg_loss = np.mean([t.pnl for t in losing_trades]) if losing_trades else 0

        # Profit factor
        total_wins = sum(t.pnl for t in winning_trades)
        total_losses = abs(sum(t.pnl for t in losing_trades))
        profit_factor = total_wins / total_losses if total_losses > 0 else float('inf')

        # Sharpe ratio (simplified)
        daily_returns = list(self.daily_pnl.values())
        if len(daily_returns) > 1:
            avg_daily_return = np.mean(daily_returns)
            daily_volatility = np.std(daily_returns)
            sharpe_ratio = (avg_daily_return / daily_volatility) * np.sqrt(252) if daily_volatility > 0 else 0
        else:
            sharpe_ratio = 0

        # Maximum drawdown
        cumulative_pnl = np.cumsum([t.pnl for t in closed_trades])
        running_max = np.maximum.accumulate(cumulative_pnl)
        drawdown = running_max - cumulative_pnl
        max_drawdown = np.max(drawdown) if len(drawdown) > 0 else 0

        # Holding period analysis
        holding_periods = [t.holding_period for t in closed_trades if t.holding_period]
        avg_holding_period = np.mean(holding_periods) if holding_periods else 0

        return {
            'total_trades': len(self.trades),
            'open_trades': len(self.trades) - len(closed_trades),
            'closed_trades': len(closed_trades),
            'winning_trades': len(winning_trades),
            'losing_trades': len(losing_trades),
            'win_rate': win_rate,
            'total_pnl': total_pnl,
            'total_return_pct': total_return_pct,
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'profit_factor': profit_factor,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'avg_holding_period_hours': avg_holding_period,
            'best_trade': max([t.pnl for t in closed_trades]) if closed_trades else 0,
            'worst_trade': min([t.pnl for t in closed_trades]) if closed_trades else 0
        }

    def get_strategy_performance(self) -> Dict[str, Dict[str, Any]]:
        """Get performance breakdown by strategy."""
        strategy_stats = defaultdict(lambda: {
            'total_trades': 0,
            'winning_trades': 0,
            'total_pnl': 0.0,
            'win_rate': 0.0,
            'avg_pnl': 0.0,
            'best_trade': 0.0,
            'worst_trade': 0.0
        })

        closed_trades = [t for t in self.trades if t.is_closed]

        for trade in closed_trades:
            strategy = trade.strategy
            strategy_stats[strategy]['total_trades'] += 1
            strategy_stats[strategy]['total_pnl'] += trade.pnl

            if trade.pnl > 0:
                strategy_stats[strategy]['winning_trades'] += 1

            strategy_stats[strategy]['best_trade'] = max(
                strategy_stats[strategy]['best_trade'], trade.pnl
            )
            strategy_stats[strategy]['worst_trade'] = min(
                strategy_stats[strategy]['worst_trade'], trade.pnl
            )

        # Calculate derived metrics
        for strategy, stats in strategy_stats.items():
            if stats['total_trades'] > 0:
                stats['win_rate'] = stats['winning_trades'] / stats['total_trades']
                stats['avg_pnl'] = stats['total_pnl'] / stats['total_trades']

        return dict(strategy_stats)

    def get_market_performance(self) -> Dict[str, Dict[str, Any]]:
        """Get performance breakdown by market."""
        market_stats = defaultdict(lambda: {
            'total_trades': 0,
            'total_pnl': 0.0,
            'win_rate': 0.0,
            'avg_pnl': 0.0
        })

        closed_trades = [t for t in self.trades if t.is_closed]

        for trade in closed_trades:
            market = trade.market_id
            market_stats[market]['total_trades'] += 1
            market_stats[market]['total_pnl'] += trade.pnl

        # Calculate win rates and averages
        for market, stats in market_stats.items():
            winning_trades = sum(1 for t in closed_trades
                               if t.market_id == market and t.pnl > 0)
            if stats['total_trades'] > 0:
                stats['win_rate'] = winning_trades / stats['total_trades']
                stats['avg_pnl'] = stats['total_pnl'] / stats['total_trades']

        return dict(market_stats)

    def get_time_based_performance(self, period: str = 'daily') -> Dict[str, Dict[str, Any]]:
        """
        Get performance metrics by time period.

        Args:
            period: 'daily', 'weekly', or 'monthly'
        """
        closed_trades = [t for t in self.trades if t.is_closed and t.exit_time]

        if not closed_trades:
            return {}

        # Group trades by time period
        time_groups = defaultdict(list)

        for trade in closed_trades:
            if period == 'daily':
                key = trade.exit_time.strftime('%Y-%m-%d')
            elif period == 'weekly':
                key = trade.exit_time.strftime('%Y-%W')
            elif period == 'monthly':
                key = trade.exit_time.strftime('%Y-%m')
            else:
                key = trade.exit_time.strftime('%Y-%m-%d')

            time_groups[key].append(trade)

        # Calculate metrics for each time period
        performance = {}
        for time_key, trades in time_groups.items():
            pnl = sum(t.pnl for t in trades)
            winning_trades = sum(1 for t in trades if t.pnl > 0)

            performance[time_key] = {
                'total_pnl': pnl,
                'trade_count': len(trades),
                'win_rate': winning_trades / len(trades) if trades else 0,
                'avg_pnl': pnl / len(trades) if trades else 0
            }

        return performance

    def get_risk_adjusted_metrics(self) -> Dict[str, float]:
        """Calculate risk-adjusted performance metrics."""
        closed_trades = [t for t in self.trades if t.is_closed]

        if len(closed_trades) < 2:
            return {'error': 'Need at least 2 closed trades for risk metrics'}

        # Extract returns
        returns = np.array([t.pnl_pct for t in closed_trades if t.pnl_pct])

        if len(returns) < 2:
            return {'error': 'Insufficient return data'}

        # Sortino Ratio (downside deviation)
        target_return = 0  # Risk-free rate proxy
        downside_returns = returns[returns < target_return]
        if len(downside_returns) > 0:
            downside_deviation = np.std(downside_returns)
            avg_return = np.mean(returns)
            sortino_ratio = (avg_return - target_return) / downside_deviation
        else:
            sortino_ratio = float('inf')  # No downside risk

        # Calmar Ratio (return vs max drawdown)
        stats = self.get_trade_statistics()
        max_drawdown = abs(stats.get('max_drawdown', 0))
        total_return = stats.get('total_return_pct', 0)

        calmar_ratio = total_return / max_drawdown if max_drawdown > 0 else float('inf')

        # Omega Ratio (probability weighted returns)
        threshold = 0  # Minimum acceptable return
        gains = returns[returns > threshold]
        losses = returns[returns <= threshold]

        omega_ratio = (np.sum(gains - threshold) /
                      abs(np.sum(losses - threshold))) if len(losses) > 0 else float('inf')

        return {
            'sortino_ratio': sortino_ratio,
            'calmar_ratio': calmar_ratio,
            'omega_ratio': omega_ratio,
            'sharpe_ratio': stats.get('sharpe_ratio', 0),
            'max_drawdown': max_drawdown,
            'total_return': total_return
        }

    def generate_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report."""
        return {
            'overall_statistics': self.get_trade_statistics(),
            'strategy_breakdown': self.get_strategy_performance(),
            'market_breakdown': self.get_market_performance(),
            'daily_performance': self.get_time_based_performance('daily'),
            'risk_adjusted_metrics': self.get_risk_adjusted_metrics(),
            'report_generated': datetime.now().isoformat(),
            'total_tracked_trades': len(self.trades)
        }

    def export_trades_to_csv(self, filename: str):
        """Export all trades to CSV file."""
        if not self.trades:
            logger.warning("No trades to export")
            return

        trade_data = []
        for trade in self.trades:
            trade_dict = asdict(trade)
            # Convert datetime objects to strings
            if trade_dict['entry_time']:
                trade_dict['entry_time'] = trade_dict['entry_time'].isoformat()
            if trade_dict['exit_time']:
                trade_dict['exit_time'] = trade_dict['exit_time'].isoformat()
            trade_data.append(trade_dict)

        df = pd.DataFrame(trade_data)
        df.to_csv(filename, index=False)
        logger.info(f"Exported {len(trade_data)} trades to {filename}")
