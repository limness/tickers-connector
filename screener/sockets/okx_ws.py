import asyncio
import json
import websockets
from loguru import logger


class OKXSocket:

    msg = {
        "op": "subscribe",
        "args": [
            {
                "channel": "tickers",
                "instType": "SPOT",
                "instId": "BTC-USDT"
            }
        ]
    }

    async def create_connection(self):
        websocket_resource_url = f"wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999"
        async with websockets.connect(websocket_resource_url) as ws:
            logger.info(f"Connection with OKX feed has been created!")
            await ws.send(json.dumps(self.msg))
            await self.consumer_handler(ws)

    async def consumer_handler(self, ws):
        async for msg in ws:
            print(msg)
            logger.debug(f"Message OKX")
            # todo: logics
            # tickers = json.loads(msg)
            await asyncio.sleep(5.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(OKXSocket().create_connection())
