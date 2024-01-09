"""Models for database"""

from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """SQL Alchemy Base class"""


class User(Base):
    """SQL Alchemy User class"""

    __tablename__ = "user_account"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[datetime]

    orders: Mapped[List["Order"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Item(Base):
    """SQL Alchemy User class"""

    __tablename__ = "item"

    item_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    stock: Mapped[int]
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"))
    orders: Mapped["Order"] = relationship(back_populates="items")


class Order(Base):
    """SQL Alchemy User class"""

    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))
    user: Mapped["User"] = relationship(back_populates="orders")

    items: Mapped[List["Item"]] = relationship(
        back_populates="orders", cascade="all, delete-orphan"
    )
