import sys

from loguru import logger

from market_router import object_creation


def create_api_key():
    try:
        logger.info("Creating API key...")

        object_creation.create_api_key()

        logger.info("API key created successfully")

    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        create_api_key()
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
