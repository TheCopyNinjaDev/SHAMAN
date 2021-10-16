import asyncio
from datetime import datetime

from tinkoff.investments import (
    CandleEvent,
    CandleResolution,
    OperationType,
    TinkoffInvestmentsRESTClient,
    TinkoffInvestmentsStreamingClient,
)

streaming = TinkoffInvestmentsStreamingClient("TOKEN")
rest = TinkoffInvestmentsRESTClient("TOKEN")


@streaming.events.candles("BBG000B9XRY4", CandleResolution.MIN_1)
async def buy_apple(candle: CandleEvent, server_time: datetime):
    if candle.c > 350:
        await rest.orders.create_market_order(
            figi="BBG000B9XRY4",
            lots=1,
            operation=OperationType.BUY,
            broker_account_id=123,
        )


asyncio.run(streaming.run())
