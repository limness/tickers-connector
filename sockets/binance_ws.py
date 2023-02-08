import asyncio
import json
import websockets


class BinanceSocket:

    msg = {
        "method": "SUBSCRIBE",
        "params": ["!ticker@arr"],
        "id": 1
    }

    async def create_connection(self):
        websocket_resource_url = f"wss://stream.binance.com:9443/ws/!ticker@arr"
        async with websockets.connect(websocket_resource_url) as ws:
            await ws.send(json.dumps(self.msg))
            await self.consumer_handler(ws)

    async def consumer_handler(self, ws):
        async for msg in ws:
            print(msg)
            # todo: logics
            # tickers = json.loads(msg)
            await asyncio.sleep(5.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(BinanceSocket().create_connection())
