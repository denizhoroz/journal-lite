from sqlalchemy import Column, Integer, Date, Text, String
from .database import Base

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    tab_name = Column(String(100), nullable=False)
    entry = Column(Text, nullable=False)

class JournalEvent(Base):
    __tablename__ = "journal_events"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    event = Column(Text, nullable=False)