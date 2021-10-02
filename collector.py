import asyncio
import os
from datetime import datetime

import pandas as pd
from tinkoff.investments import (
    CandleResolution,
    Environment,
    TinkoffInvestmentsRESTClient,
)
from tinkoff.investments.utils.historical_data import HistoricalData

TOKEN = "t.OSXZNWhaTPOEYpt3FoCeqSegYPNtOgocRvmL0IX4c5rTQiSGP-pJ0ZHSIpmHGd5wTF_lt9P8tdW_PTSTXRIahw"
data = []


async def get_minute_candles(ticker, start, end):
    # show 1 minute candles for AAPL in 1 year period of time
    async with TinkoffInvestmentsRESTClient(
        token=TOKEN, environment=Environment.SANDBOX
    ) as client:
        historical_data = HistoricalData(client)
        instruments = await client.market.instruments.search(ticker)
        stock_figi = instruments[0].figi
        async for candle in historical_data.iter_candles(
            figi=stock_figi,
            dt_from=start,
            dt_to=end,
            interval=CandleResolution.MIN_15,
        ):
            data.append(candle.to_dict())

ticker = 'PIKK'
start = pd.to_datetime('2020.10.01')
end = pd.to_datetime('2021.10.01')


asyncio.run(get_minute_candles(ticker, start, end))

df = pd.DataFrame(data)
os.mkdir(f'data/{ticker}')
df.to_csv(f"data/{ticker}/{str(start)[:10]} - {str(end)[:10]}.csv")
