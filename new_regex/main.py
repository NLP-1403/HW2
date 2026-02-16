"""
Custom Regex Pattern Database Manager

This module provides a SQLite-based system for storing and managing custom
regular expression patterns. Users can define their own named patterns and
test messages against them for flexible text matching capabilities.

Database Schema:
    Table: message_patterns
    - id (Integer): Primary key
    - name (String): Unique pattern identifier
    - regex (String): Regular expression pattern

Functions:
    add_regex(name, regex): Store a new pattern (prevents duplicates)
    check_message_patterns(message): Test message against all stored patterns
    check_custom_regex(message, custom_regex): Validate a custom regex on text

Example:
    >>> from new_regex.main import add_regex, check_message_patterns
    >>> add_regex("postal_code", r"\d{10}")
    >>> matches = check_message_patterns("کد پستی: 1234567890")
    >>> print(matches)  # {'postal_code': '1234567890'}
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import re

engine = create_engine('sqlite:///new_regex/message_patterns.db')
Base = declarative_base()


class MessagePattern(Base):
    __tablename__ = 'message_patterns'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    regex = Column(String)


Base.metadata.create_all(engine)


def add_regex(name, regex):
    Session = sessionmaker(bind=engine)
    session = Session()
    status = True
    try:
        new_pattern = MessagePattern(name=name, regex=regex)
        session.add(new_pattern)
        session.commit()
    except Exception as ignore:
        if "UNIQUE constraint failed" in str(ignore):
            status = False
    finally:
        session.close()
    return status


def check_message_patterns(message):
    Session = sessionmaker(bind=engine)
    session = Session()
    patterns = session.query(MessagePattern).all()
    matches = {}
    for pattern in patterns:
        if match := re.search(pattern.regex, message):
            matches[pattern.name] = match.group()
    session.close()
    return matches


def check_custom_regex(message, custom_regex):
    match = re.search(custom_regex, message)
    return bool(match)
