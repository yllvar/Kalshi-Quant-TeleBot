#!/usr/bin/env python3
"""Helper CLI for surfacing live Kalshi data to the Node interface."""
from __future__ import annotations

import argparse
import json
import sys
import time
from typing import Any, Dict, List

from kalshi_api import KalshiAPI


def _cents_to_dollars(value: Any) -> float | None:
    try:
        return round(float(value) / 100, 2)
    except (TypeError, ValueError):
        return None


def fetch_balance(api: KalshiAPI) -> Dict[str, Any]:
    raw = api.get_account_balance() or {}

    summary = {
        "available": _cents_to_dollars(
            raw.get("available_cash")
            or raw.get("available_balance")
            or raw.get("cash_balance")
        ),
        "total_equity": _cents_to_dollars(
            raw.get("portfolio_value") or raw.get("equity") or raw.get("total_equity")
        ),
        "unrealized_pnl": _cents_to_dollars(
            raw.get("unrealized_pnl") or raw.get("unrealized_pl")
        ),
        "realized_pnl": _cents_to_dollars(
            raw.get("realized_pnl") or raw.get("realized_pl")
        ),
        "timestamp": raw.get("timestamp") or raw.get("time"),
    }

    return {
        "summary": summary,
        "raw": raw,
    }


def fetch_positions(api: KalshiAPI) -> Dict[str, Any]:
    response = api.get_positions() or {}
    positions = response.get("positions") or response.get("data") or []
    return {
        "positions": positions,
        "count": len(positions),
        "raw": response,
    }


def fetch_status(api: KalshiAPI) -> Dict[str, Any]:
    exchange_status = api.get_exchange_status() or {}
    balance = fetch_balance(api)
    positions = fetch_positions(api)

    # Note: Arbitrage analysis would require market data with price history
    # This is included in the main trader loop, not here for performance

    return {
        "exchange_status": exchange_status,
        "balance_summary": balance.get("summary", {}),
        "positions_count": positions.get("count", 0),
        "active_strategies": ["news_sentiment", "statistical_arbitrage", "volatility_based"],
        "risk_management": {
            "kelly_criterion_enabled": True,
            "dynamic_position_sizing": True,
            "stop_loss_protection": True,
            "take_profit_scaling": False,  # Simplified for Phase 2
            "max_position_size_pct": 10.0,
            "stop_loss_pct": 5.0
        },
        "phase3_features": {
            "real_time_market_data": True,
            "market_data_streaming": True,
            "performance_analytics": True,
            "advanced_reporting": True,
            "market_movement_tracking": True
        },
        "timestamp": time.time(),
    }


def fetch_performance(api: KalshiAPI) -> Dict[str, Any]:
    orders = api.get_orders(params={"limit": 100}) or {}
    orders_list: List[Dict[str, Any]] = orders.get("orders") or orders.get("data") or []

    filled_counts = [order.get("count") for order in orders_list if order.get("count")]
    avg_prices = [order.get("avg_price") or order.get("yes_price") for order in orders_list if order.get("avg_price") or order.get("yes_price")]

    total_trades = len(orders_list)
    total_contracts = sum(int(c) for c in filled_counts if isinstance(c, (int, float)))
    average_price = (
        round(
            sum(float(price) for price in avg_prices if isinstance(price, (int, float)))
            / len(avg_prices),
            4,
        )
        if avg_prices
        else None
    )

    return {
        "totalTrades": total_trades,
        "totalContracts": total_contracts,
        "averagePrice": average_price,
        "rawOrders": orders_list,
    }


def run(command: str) -> Dict[str, Any]:
    api = KalshiAPI()

    if command == "status":
        return fetch_status(api)
    if command == "positions":
        return fetch_positions(api)
    if command == "balance":
        return fetch_balance(api)
    if command == "performance":
        return fetch_performance(api)

    raise ValueError(f"Unsupported command: {command}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Expose bot state via CLI")
    parser.add_argument(
        "command",
        choices=["status", "positions", "balance", "performance"],
        help="State command to execute",
    )
    args = parser.parse_args()

    try:
        payload = run(args.command)
        print(json.dumps(payload, default=str))
    except Exception as exc:  # pylint: disable=broad-except
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
