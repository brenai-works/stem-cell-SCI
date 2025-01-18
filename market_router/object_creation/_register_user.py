import os
from market_router import utils as api_call

_USER_VARIABLES = ["USERNAME", "FULLNAME", "EMAIL", "PASSWORD"]


def register_user():
    user_data = _load_user_details()

    api_call.register_user(user_data)


def _load_user_details():
    user_data = {}
    for variable in _USER_VARIABLES:
        value = os.getenv("MARKET_ROUTER_" + variable)
        if not value:
            raise ValueError(f"Environment variable MARKET_ROUTER_{variable} is not set")
        user_data[variable.lower()] = value
    return user_data
