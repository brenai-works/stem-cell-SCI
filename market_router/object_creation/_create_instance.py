import os

from market_router import config
from market_router import utils as api_call

_INSTANCE_VARIABLES = [
    "messages",
    "model",
    "background",
    "max_credit_per_instance",
    "percentage_reward",
    "instance_timeout",
    "gen_reward_timeout",
]


def create_instance():
    instance = _load_instance_details()

    api_key = os.getenv("MARKET_ROUTER_KEY")

    instance_created = api_call.submit_instance(instance, api_key)

    return instance_created["id"]


def _load_instance_details():
    return {variable: config[variable] for variable in _INSTANCE_VARIABLES}
