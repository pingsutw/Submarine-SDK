import time
from sqlalchemy import (
    Column, String, Float, ForeignKey,
    BigInteger, PrimaryKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

RunStatusTypes = [
    "SCHEDULED",
    "FAILED",
    "FINISHED",
    "RUNNING",
]

class SqlMetric(Base):
    __tablename__ = 'metrics'

    key = Column(String(250))
    """
    Metric key: `String` (limit 250 characters). Part of *Primary Key* for ``metrics`` table.
    """
    value = Column(Float, nullable=False)
    """
    Metric value: `Float`. Defined as *Non-null* in schema.
    """
    worker_index = Column(String(250), nullable=False)
    """
    Param worker_index: `String` (limit 250 characters). Defined as *Non-null* in schema.
    """
    timestamp = Column(BigInteger, default=lambda: int(time.time()))
    """
    Timestamp recorded for this metric entry: `BigInteger`. Part of *Primary Key* for
                                               ``metrics`` table.
    """
    run_uuid = Column(String(32), ForeignKey('runs.run_uuid'))
    """
    Run UUID to which this metric belongs to: Part of *Primary Key* for ``metrics`` table.
                                              *Foreign Key* into ``runs`` table.
    """

    __table_args__ = (
        PrimaryKeyConstraint('key', 'timestamp',  'worker_index', 'run_uuid', name='metric_pk'),
    )

    def __repr__(self):
        return '<SqlMetric({}, {}, {})>'.format(self.key, self.value, self.timestamp)


class SqlParam(Base):
    __tablename__ = 'params'

    key = Column(String(250))
    """
    Param key: `String` (limit 250 characters). Part of *Primary Key* for ``params`` table.
    """
    value = Column(String(250), nullable=False)
    """
    Param value: `String` (limit 250 characters). Defined as *Non-null* in schema.
    """
    worker_index = Column(String(250), nullable=False)
    """
    Param worker_index: `String` (limit 250 characters). Defined as *Non-null* in schema.
    """
    run_uuid = Column(String(32), ForeignKey('runs.run_uuid'))
    """
    Run UUID to which this metric belongs to: Part of *Primary Key* for ``params`` table.
                                              *Foreign Key* into ``runs`` table.
    """

    __table_args__ = (
        PrimaryKeyConstraint('key', 'worker_index', 'run_uuid', name='param_pk'),
    )

    def __repr__(self):
        return '<SqlParam({}, {})>'.format(self.key, self.value)






