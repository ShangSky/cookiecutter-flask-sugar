from typing import Any, Type, cast

from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as _Session
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    config.DB_URI, pool_recycle=config.POOL_RECYCLE, pool_pre_ping=config.POOL_PRE_PING
)
Base: Any = declarative_base(engine)
Session = cast(Type[_Session], sessionmaker(engine))

redis = Redis.from_url(
    config.REDIS_URI,
    decode_responses=True,
    encoding="utf-8",
)
