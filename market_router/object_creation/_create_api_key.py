import os
from loguru import logger

from market_router import utils as api_call

_USER_VARIABLES = ["USERNAME", "FULLNAME", "EMAIL", "PASSWORD"]


def create_api_key():
    user_data = _load_user_details()

    login_info = api_call.login_user(user_data)

    api_key = api_call.create_api_key(login_info)

    logger.info(f"API key created: {api_key}")


def _load_user_details():
    user_data = {}
    for variable in _USER_VARIABLES:
        value = os.getenv(f"MARKET_ROUTER_{variable}")
        if value is None:
            raise ValueError(f"Environment variable 'MARKET_ROUTER_{variable}' is not set")
        user_data[variable.lower()] = value
    return user_data
