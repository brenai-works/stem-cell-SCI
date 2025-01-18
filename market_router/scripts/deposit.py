import sys

from loguru import logger

from market_router import object_creation


def deposit_funds():
    try:
        logger.info("Depositing funds to account...")

        object_creation.deposit_funds()

        logger.info("Please click the link")

    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        deposit_funds()
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
