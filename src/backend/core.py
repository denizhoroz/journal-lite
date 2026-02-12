from datetime import datetime

from src.backend.repository import Repository

class Core:
    def __init__(self):
        self.repo = Repository()

    def add_entry(self, entry_date, tab_name: str, content: str): 
        self.repo.add_entry(entry_date, tab_name, content)

    def get_entry_by_tab(self, entry_date, tab_name: str):
        result = self.repo.get_entry_by_tab(entry_date, tab_name)

        if result != None:
            return result
        else:
            return ""

    def get_all_entries_by_date(self, entry_date):
        result = self.repo.get_all_entries_by_date(entry_date)

        if result != None:
            return result
        else:
            return ""

    def add_tab(self): pass # unused

    def delete_tab(self, entry_date, tab_name: str):
        self.repo.delete_tab(entry_date, tab_name)

    def _get_current_date(self):
        pass

    def _get_tabs_in_date(self, entry_date): return self.repo.get_tabs(entry_date)

    def add_event(self, event_date, event):
        self.repo.add_event(event_date, event)

    def delete_event(self, event_date, event):
        self.repo.delete_event(event_date, event)

    def get_events_by_date(self, event_date): return self.repo.get_events_by_date(event_date)