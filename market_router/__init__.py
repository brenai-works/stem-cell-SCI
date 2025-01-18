"""Top level package."""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

# Paths module
BASEPATH = Path(__file__).parent.absolute()
WORKDIR = Path(__file__).parent.parent.absolute()

load_dotenv(dotenv_path=WORKDIR / ".env")
DATA_DIR = WORKDIR / "data"
MARKET_DIR = DATA_DIR / "markets"
CONFIG_DIR = WORKDIR / "config"

API_URL = os.getenv("API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")

# Load config
with open(CONFIG_DIR / "config.yaml", "r") as f:
    config = yaml.safe_load(f)
