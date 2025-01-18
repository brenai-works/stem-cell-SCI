import sys

from loguru import logger

from market_router import object_creation


def create_instance():
    try:
        logger.info("Creating instance...")

        instance_id = object_creation.create_instance()

        logger.info(f"Instance created successfully, instance_id: {instance_id}")

        return instance_id

    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        create_instance()
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
