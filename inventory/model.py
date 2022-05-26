import datetime
import enum
import logging

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
log = logging.getLogger(__name__)

# from model import Samples, SaleItems, OrderItems, Sales, Orders, Items, Users, Flags, OrderItemStatusEnum, UserLevelEnum


class UserLevelEnum(enum.Enum):
    admin: str = "admin"
    standard: str = "standard"


class OrderItemStatusEnum(enum.Enum):
    ordered: str = "ordered"
    received: str = "received"
    cancelled: str = "cancelled"


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
    user_level = Column(Enum(UserLevelEnum), default=UserLevelEnum.standard)
    children0 = relationship("Items")
    children1 = relationship("Orders")
    children2 = relationship("Sales")


class Items(Base):
    __tablename__ = "items"
    item_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    item_name = Column(String)
    item_category = Column(String)
    children0 = relationship("OrderItems")


class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    order_created_at = Column(DateTime)
    order_locked = Column(Boolean, default=False)
    order_note = Column(String)
    children0 = relationship("OrderItems")


class Sales(Base):
    __tablename__ = "sales"
    sale_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    sale_created_at = Column(DateTime, default=datetime.datetime.now())
    sale_customer = Column(String, default="")
    sale_paid = Column(Boolean, default=False)
    sale_delivered = Column(Boolean, default=False)


class OrderItems(Base):
    __tablename__ = "order_items"
    order_id = Column(String, ForeignKey("orders.order_id"), primary_key=True)
    item_id = Column(String, ForeignKey("items.item_id"), primary_key=True)
    quantity = Column(Integer)
    status = Column(Enum(OrderItemStatusEnum), default=OrderItemStatusEnum.ordered)


class SaleItems(Base):
    __tablename__ = "sale_items"
    sale_id = Column(String, ForeignKey("sales.sale_id"), primary_key=True)
    item_id = Column(String, ForeignKey("items.item_id"), primary_key=True)
    quantity = Column(Integer)


class Samples(Base):
    __tablename__ = "samples"
    sample_id = Column(String, primary_key=True)
    item_id = Column(String, ForeignKey("items.item_id"))
    quantity = Column(Integer)
    sample_used = Column(Boolean, default=False)
