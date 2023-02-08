from sockets import binance_ws, okx_ws
from typing import Any


class FeedFactory:

    feeds = {
        "Binance": binance_ws.BinanceSocket,
        "OKX": okx_ws.OKXSocket,
    }

    def create(self, feed_name: str = "Binance") -> Any:
        return self.feeds[feed_name]()
