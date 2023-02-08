import global_vars
import constants
import requests


def init_tickers() -> None:
    """
    Initialize allowed tickers from Binance API
    :return: Nothing
    """
    try:
        response = requests.get("https://api4.binance.com/api/v1/ticker/price")
        tickers = response.json()

        for ticker in tickers:
            if ticker["symbol"] not in constants.binance_tickers:
                continue
            global_vars.tickers[constants.binance_tickers[ticker["symbol"]]] = float(ticker["price"])

    except Exception as ex:
        print(f"Something is going wrong {ex}")
