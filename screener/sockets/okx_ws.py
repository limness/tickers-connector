import asyncio
import json
import websockets
from loguru import logger
import constants
import global_vars


class OKXSocket:

    msg = {
        "op": "subscribe",
        "args": [
            {
                "channel": "index-tickers",
                "instId": "..."
            }
        ]
    }

    async def create_connection(self):
        websocket_resource_url = f"wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999"
        async with websockets.connect(websocket_resource_url) as ws:
            logger.info(f"Connection with OKX feed has been created!")
            d = 0 / 0
            for ticker in constants.okx_tickers:
                self.msg["args"][0]["instId"] = ticker
                await ws.send(json.dumps(self.msg))
            await self.consumer_handler(ws)

    async def consumer_handler(self, ws):
        async for msg in ws:
            ticker = json.loads(msg)
            logger.debug(f"Message OKX {msg}")

            if "data" in ticker:
                ticker_name = constants.okx_tickers[ticker["data"][0]["instId"]]
                global_vars.tickers[ticker_name] = float(ticker["data"][0]["idxPx"])

        await asyncio.sleep(5.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(OKXSocket().create_connection())
