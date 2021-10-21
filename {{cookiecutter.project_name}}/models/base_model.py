from sqlalchemy import BIGINT, DATETIME, Boolean, Column, func

from common.db import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(BIGINT, primary_key=True)
    created_time = Column(
        DATETIME,
        nullable=False,
        server_default=func.now(),
        comment="创建时间",
    )
    updated_time = Column(
        DATETIME,
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )
    deleted = Column(Boolean, default=False, comment="是否删除")
