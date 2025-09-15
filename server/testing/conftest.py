#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def pytest_configure():
    from app import app, db
    from models import Message
    with app.app_context():
        db.create_all()
        # Add test data for PATCH tests
        test_message = Message(body="Test message", username="Test user")
        db.session.add(test_message)
        db.session.commit()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))