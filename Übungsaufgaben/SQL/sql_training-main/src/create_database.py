"""Create Training Database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.item_data import test_items
from data.order_data import test_orders
from data.user_data import test_users
from models import Base

ENGINE = create_engine("sqlite:///test.db", echo=True)

Base.metadata.create_all(ENGINE)

with Session(ENGINE) as session:
    session.add_all(test_users)
    session.add_all(test_items)
    session.add_all(test_orders)
    session.commit()
