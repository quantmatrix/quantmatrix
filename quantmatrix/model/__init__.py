# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import datetime
import sqlalchemy.sql.expression
from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import INTEGER, TIMESTAMP, BOOLEAN
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base


@as_declarative()
class MetaModel(object):
    @declared_attr
    def __tablename__(self):
        return self.__name__

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def to_dict(self):
        return self.columnitems

    id = Column(
        INTEGER(),
        primary_key=True,
        autoincrement=True,
        comment="主键ID"
    )
    created_at = Column(
        TIMESTAMP,
        server_default=sqlalchemy.sql.expression.text("(datetime(CURRENT_TIMESTAMP,'localtime'))"),
        nullable=False,
        comment="创建时间"
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=sqlalchemy.sql.expression.text("(datetime(CURRENT_TIMESTAMP,'localtime'))"),
        nullable=False,
        onupdate=datetime.datetime.now,
        comment="修改时间"
    )
    remove = Column(
        BOOLEAN,
        server_default=sqlalchemy.sql.expression.text("FALSE"),
        nullable=False,
        comment="软删除位"
    )


ModelBase = declarative_base(cls=MetaModel)
