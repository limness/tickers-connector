import asyncio
import traceback

import global_vars
import constants
import requests
from feeds_factory import FeedFactory
from loguru import logger


def init_tickers() -> None:
    """
    Initialize allowed tickers from Binance API
    :return: Nothing
    """
    try:
        response = requests.get("https://aws.okx.com/api/v5/market/tickers?instType=SPOT")
        tickers = response.json()["data"]

        for ticker in tickers:
            if ticker["instId"] not in constants.okx_tickers:
                continue
            okx_ticker = constants.okx_tickers[ticker["instId"]]
            global_vars.tickers[okx_ticker] = float(ticker["last"])

    except Exception as ex:
        logger.exception(f"Something is going wrong")


async def init_connections() -> None:

    feed_factory = FeedFactory()

    # get list of feeds without OKX
    feeds = list(feed_factory.feeds.keys())

    # define the name of the feed that will
    # be connected to in the beginning "OKX"
    feed_queue_name = feeds[0]

    while True:
        feed = feed_factory.create(feed_queue_name)
        try:
            # open new connection
            await feed.create_connection()
        except Exception as ex:
            logger.exception(f"Something is going wrong with `{feed_queue_name}` feed, "
                             f"connecting to next feed...")

            # Switching to the next feed, something happened to the previous one
            feed_queue_name = feeds[feeds.index(feed_queue_name) - 1]
            await asyncio.sleep(0.5)
