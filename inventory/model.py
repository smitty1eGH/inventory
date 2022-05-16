import logging
import uuid

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

log = logging.getLogger(__name__)

# CREATE TYPE user_level_enum        AS ENUM ('admin'  , 'standard')
# CREATE TYPE order_item_status_enum AS ENUM ('ordered', 'received', 'cancelled')

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
    user_level = Column(String)


                CREATE TABLE IF NOT EXISTS items (
                    item_id UUID PRIMARY KEY,
                    user_id UUID REFERENCES users,
                    item_name TEXT NOT NULL,
                    item_category TEXT
                )


                CREATE TABLE IF NOT EXISTS orders (
                    order_id UUID PRIMARY KEY,
                    user_id UUID REFERENCES users,
                    order_created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
                    order_locked BOOLEAN NOT NULL DEFAULT FALSE,
                    order_note TEXT DEFAULT ''
                )


                CREATE TABLE IF NOT EXISTS sales (
                    sale_id UUID PRIMARY KEY,
                    user_id UUID REFERENCES users,
                    sale_created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
                    sale_customer TEXT DEFAULT '',
                    sale_paid BOOLEAN NOT NULL DEFAULT FALSE,
                    sale_delivered BOOLEAN NOT NULL DEFAULT FALSE
                )


                CREATE TABLE IF NOT EXISTS order_items (
                    order_id UUID REFERENCES orders ON DELETE CASCADE,
                    item_id UUID REFERENCES items,
                    quantity INT NOT NULL,
                    status order_item_status_enum NOT NULL DEFAULT 'ordered',
                    PRIMARY KEY (order_id, item_id)
                )


                CREATE TABLE IF NOT EXISTS sale_items (
                    sale_id UUID REFERENCES sales ON DELETE CASCADE,
                    item_id UUID REFERENCES items,
                    quantity INT NOT NULL,
                    PRIMARY KEY (sale_id, item_id)
                )


                CREATE TABLE IF NOT EXISTS samples (
                    sample_id UUID PRIMARY KEY,
                    item_id UUID REFERENCES items,
                    quantity INT NOT NULL,
                    sample_used BOOLEAN NOT NULL DEFAULT FALSE
                )


