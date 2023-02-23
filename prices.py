from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def price(
    coin: str, currency: str
):  # Connects to API and retrieves information. Returns information ready for output

    with open("./json/apidata.json") as apidata:  # Load API key before connection
        config = json.load(apidata)

    URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"  # Points to the API interface
    parameters = {
        "symbol": coin,
        "convert": currency,
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": config.get(
            "apikey"
        ),  # Gets your API key from your json file
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(
            URL,
            params=parameters,
        )
        data = json.loads(response.text)

        symbol = data["data"][coin][0]["symbol"]

        price = data["data"][coin][0]["quote"][currency][
            "price"
        ]  # gets price from nested dict
        price_float = float(price)
        price_for_prnt = f"{price_float:.6}"

        change1day = data["data"][coin][0]["quote"][currency]["percent_change_24h"]

    except (
        ConnectionError,
        Timeout,
        TooManyRedirects,
        Exception,
    ) as e:
        print(e)

    finally:
        return f"{symbol} £ {price_for_prnt}\n24HR% change {change1day}"
