from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import re

engine = create_engine('sqlite:///message_patterns.db')
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
    try:
        new_pattern = MessagePattern(name=name, regex=regex)
        session.add(new_pattern)
        session.commit()
    except Exception as ignore:
        pass
    finally:
        session.close()


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
    return bool(re.match(custom_regex, message))


# Example usage:
add_regex('Email', r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
add_regex('Iranian Phone Number', r'\+?98[0-9]{10}')
add_regex('Address', r'\b(?:neighborhood|street|alley|plaque)\b')

message = "Please contact me at john.doe@example.com or +989123456789. I live on 123 Elm Street."
print("Matches found:", check_message_patterns(message))

custom_regex = r'^[A-Za-z\s]+$'
print("Matches custom regex:", check_custom_regex("Hello World", custom_regex))
