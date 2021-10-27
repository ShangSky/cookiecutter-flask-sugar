from pathlib import Path

from utils.load_config import init_config

BASE_DIR = Path(__file__).resolve(strict=True).parent
config_data = init_config((BASE_DIR / "env.yaml").open())

JSON_AS_ASCII = False
DEBUG = config_data.get("DEBUG", True)
ENV = config_data.get("ENV", "dev")
DB_URI = config_data.get("DB_URI", "sqlite:///database.db")
POOL_PRE_PING = config_data.get("POOL_PRE_PING", True)
POOL_RECYCLE = config_data.get("POOL_RECYCLE", 3600)
REDIS_URI = config_data.get("REDIS_URI", "redis://localhost:6379/0")
