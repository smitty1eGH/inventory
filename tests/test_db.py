import pytest
from pytest_sqlalchemy import engine, connection

from inventory.model import (
    Base,
    Samples,
    SaleItems,
    OrderItems,
    Sales,
    Orders,
    Items,
    Users,
    Flags,
    OrderItemStatusEnum,
    UserLevelEnum,
)


@pytest.fixture(scope="session")
def sqlalchemy_connect_url():
    # return 'postgresql://scott:tiger@localhost:5432/mydatabase'
    return "sqlite:///:memory:"


@pytest.fixture
def conn(connection):
    assert connection
    return conn


def test_create_schema(engine):
    Base.metadata.create_all(engine)
    assert len([t for t in Base.metadata.tables.keys()]) == 8
