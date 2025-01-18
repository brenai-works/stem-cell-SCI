import sys

from loguru import logger

from market_router import object_creation


def submit_generated_reward(instance_id: str = None, reward: int = None):
    try:
        logger.info("Submitting generated reward")

        object_creation.send_reward(instance_id=instance_id, gen_reward=reward)

        logger.info("Finished submitting generated reward")

    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        submit_generated_reward()
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
