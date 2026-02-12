from datetime import datetime

from src.backend.repository import Repository

class Core:
    def __init__(self):
        self.repo = Repository()

    def add_entry(self, entry_date, tab_name: str, content: str):
        """
        Params:
            entry_date: datetime
            tab_name: str
            content: str
        """
        
        self.repo.add_entry(entry_date, tab_name, content)

    def get_entry(self, entry_date, tab_name: str):
        """
        Params:
            entry_date: datetime
            tab_name: str
        """

        result = self.repo.get_entry(entry_date, tab_name)

        if result != None:
            return result.entry
        else:
            return ""

    def _get_current_date(self):
        pass