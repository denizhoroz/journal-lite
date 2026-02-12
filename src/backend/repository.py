from datetime import date
from .database import SessionLocal
from .models import JournalEntry, JournalEvent

class Repository:

    # JournalEntry
    def add_entry(self, entry_date, tab_name: str, content: str):
        with SessionLocal() as session:
            existing = (
                session.query(JournalEntry)
                .filter(
                    JournalEntry.date == entry_date,
                    JournalEntry.tab_name == tab_name
                )
                .first()
            )

            if existing:
                # Overwrite content
                existing.entry = content
            else:
                # Create new entry
                entry = JournalEntry(
                    date=entry_date,
                    tab_name=tab_name,
                    entry=content
                )
                session.add(entry)

            session.commit()

    def get_entry_by_tab(self, entry_date, tab_name: str):
        with SessionLocal() as session:
            return (
                session.query(JournalEntry)
                .filter(
                    JournalEntry.date == entry_date,
                    JournalEntry.tab_name == tab_name
                )
                .first()
            )
        
    def get_all_entries_by_date(self, entry_date):
        with SessionLocal() as session:
            return (
                session.query(JournalEntry)
                .filter(
                    JournalEntry.date == entry_date
                )
                .all()
            )

    def delete_entry(self, entry_id: int):
        with SessionLocal() as session:
            entry = session.get(JournalEntry, entry_id)
            if entry:
                session.delete(entry)
                session.commit()

    def delete_tab(self, entry_date, tab_name):
        with SessionLocal() as session:
            entry = (
                session.query(JournalEntry)
                .filter(
                    JournalEntry.date == entry_date,
                    JournalEntry.tab_name == tab_name
                )
                .first()
            )
            if entry:
                session.delete(entry)
                session.commit()

    # JournalEvent
    def add_event(self, event_date: date, event: str):
        with SessionLocal() as session:
            event = JournalEvent(
                date=event_date,
                event=event
            )
            session.add(event)
            session.commit()

    def delete_event(self, event_date: date, event: str):
        with SessionLocal() as session:
            entry = (
                session.query(JournalEvent)
                .filter(
                    JournalEvent.date == event_date,
                    JournalEvent.event == event
                )
                .first()
            )
            if entry:
                session.delete(entry)
                session.commit()

    def get_events_by_date(self, event_date: date):
        with SessionLocal() as session:
            return (
                session.query(JournalEvent)
                .filter(JournalEvent.date == event_date)
                .all()
            )