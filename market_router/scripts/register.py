import sys

from loguru import logger

from market_router import object_creation


def register_user():
    try:
        logger.info("Registering user...")

        object_creation.register_user()

        logger.info("User registered successfully")

    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        register_user()
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
