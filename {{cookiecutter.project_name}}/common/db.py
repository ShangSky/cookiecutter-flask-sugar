from typing import Any

from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(config.DB_URI)
Base: Any = declarative_base(engine)
Session = sessionmaker(engine)

redis = Redis.from_url(
    config.REDIS_URI,
    decode_responses=True,
    encoding="utf-8",
)
