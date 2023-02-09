from sockets import binance_ws, okx_ws
from typing import Any


class FeedFactory:

    feeds = {
        # set OKX first in the dict, setting the connection priority
        "OKX": okx_ws.OKXSocket,
        # third party
        "Binance": binance_ws.BinanceSocket,
        # ...
    }

    def create(self, feed_name: str = "Binance") -> Any:
        return self.feeds[feed_name]()
