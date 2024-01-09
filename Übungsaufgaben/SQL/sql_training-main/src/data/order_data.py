"""Example Users for Database"""
from datetime import datetime

from models import Order

test_orders = [
    Order(
        date=datetime(1990, 5, 15, 4, 5, 12, 123),
        user_id=1,
    ),
]
