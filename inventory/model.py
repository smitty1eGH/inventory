import enum
import logging
import typing
import uuid

from sqlalchemy import Column, DateTime, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
log = logging.getLogger(__name__)

class UserLevelEnum(enum.Enum):
    admin : str = 'admin'
    standard : str = 'standard'

class OrderItemStatusEnum(enum.Enum):
    ordered : str = 'ordered'
    received : str = 'received'
    cancelled : str = 'cancelled'

class Flags(Base):
    __tablename__ = "flags"
    flag_name = Column(String, primary_key=True)
    flag_text = Column(String)
    flag_int = Column(Integer)
    flag_timestamp = Column(DateTime)

# INSERT INTO flags (flag_name, flag_int) VALUES (%s, %s)', ['db_version', 1])

class Users(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True)
    user_email = Column(String)
    user_level = Column(Enum(UserLevelEnum()),default=UserLevelEnum.standard)
    children0 = relationship("Items")
    children1 = relationship("Orders")
    children2 = relationship("Sales")


class Items(Base):
    __tablename__ = "items"
    item_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    item_name = Column(String)
    item_category = Column(String)


class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    order_created_at  = Column(DateTime)
    order_locked = Column(Boolean, default=False)
    order_note = Column(String)


class Sales(Base):
    __tablename__ = "sales"
    sale_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    sale_created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
    sale_customer TEXT DEFAULT '',
    sale_paid BOOLEAN NOT NULL DEFAULT FALSE,
    sale_delivered BOOLEAN NOT NULL DEFAULT FALSE


class OrderItems(Base):
    __tablename__ = "order_items"
    order_id UUID REFERENCES orders ON DELETE CASCADE,
    item_id UUID REFERENCES items,
    quantity INT NOT NULL,
    status order_item_status_enum NOT NULL DEFAULT 'ordered',
    PRIMARY KEY (order_id, item_id)


class SaleItems(Base):
    __tablename__ = "sale_items"
    sale_id UUID REFERENCES sales ON DELETE CASCADE,
    item_id UUID REFERENCES items,
    quantity INT NOT NULL,
    PRIMARY KEY (sale_id, item_id)


class Samples(Base):
    __tablename__ = "samples"
    sample_id UUID PRIMARY KEY,
    item_id UUID REFERENCES items,
    quantity INT NOT NULL,
    sample_used BOOLEAN NOT NULL DEFAULT FALSE


