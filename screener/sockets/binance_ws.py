import asyncio
import json
import websockets
import constants
import global_vars
from loguru import logger


class BinanceSocket:

    msg = {
        "method": "SUBSCRIBE",
        "params": [],
        "id": 1
    }

    async def create_connection(self):
        websocket_resource_url = f"wss://stream.binance.com:443/ws"
        async with websockets.connect(websocket_resource_url) as ws:
            logger.info(f"Connection with Binance feed has been created!")

            for ticker in constants.binance_tickers:
                self.msg["params"].append(ticker.lower() + "@ticker")

            await ws.send(json.dumps(self.msg))
            await self.consumer_handler(ws)

    async def consumer_handler(self, ws):
        async for msg in ws:
            ticker = json.loads(msg)
            logger.debug(f"Message Binance {msg}")

            if "s" not in ticker:
                continue

            if ticker["s"] not in constants.binance_tickers:
                continue
            ticker_name = constants.binance_tickers[ticker["s"]]
            global_vars.tickers[ticker_name] = float(ticker["c"])

            await asyncio.sleep(5.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(BinanceSocket().create_connection())
