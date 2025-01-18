import os

from market_router import config
from market_router import utils as api_call


def send_reward(instance_id: str = None, gen_reward: int = None):
    try:
        if not gen_reward:
            gen_reward_data = _load_gen_reward_data()
        else:
            gen_reward_data = {"gen_reward": gen_reward}

        if not instance_id:
            instance_id = os.getenv("INSTANCE_ID")

        api_key = os.getenv("MARKET_ROUTER_KEY")

        api_call.send_reward(gen_reward_data, instance_id, api_key)

    except Exception as e:
        raise e


def _load_gen_reward_data():
    return {"gen_reward": config["gen_reward"]}
