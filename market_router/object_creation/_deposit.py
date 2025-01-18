import os

from market_router import config
from market_router import utils as api_call


def deposit_funds():
    try:
        deposit_data = _load_deposit_data()

        api_key = os.getenv("MARKET_ROUTER_KEY")

        api_call.deposit(deposit_data, api_key)

    except Exception as e:
        raise e


def _load_deposit_data():
    return {"amount": config["deposit_amount"]}
