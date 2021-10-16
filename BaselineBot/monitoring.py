import asyncio
from datetime import datetime
from tinkoff.investments import (
    CandleEvent,
    CandleResolution,
    TinkoffInvestmentsStreamingClient,
)

client = TinkoffInvestmentsStreamingClient(token="TOKEN")


@client.events.candles("BBG009S39JX6", CandleResolution.MIN_1)
async def on_candle(candle: CandleEvent, server_time: datetime):
    print(candle, server_time)


asyncio.run(client.run())
