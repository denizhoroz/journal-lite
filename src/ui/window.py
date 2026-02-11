from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QHBoxLayout,
        QPlainTextEdit,
        QLabel,
        QListWidget,
        QAbstractItemView,
        QCalendarWidget,
)

from PySide6.QtGui import (
    Qt,
    QFont,
)

from PySide6.QtCore import (
    QDate,
)

class MainWindow(QMainWindow):
    def __init__(self, core):
        super().__init__()
        self.core = core

        # Set window settings
        self.setWindowTitle("Journal Lite")
        self.resize(1200, 800)

        # Initialize UI
        self._build_ui()
        self._connect_signals()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        #### Build UI elements here ####

        ## 1 - Navigation Area ##
        
        # Set area config
        nav_area = QWidget()
        nav_area.setFixedWidth(150)
        nav_layout = QVBoxLayout()
        
        # Add widgets
        self.title = QLabel("Journal Lite")
        nav_layout.addWidget(self.title)

        self.tabs = QListWidget()
        self.tabs.addItems(["Item 1", "Item 2", "Item 3"]) # testing
        nav_layout.addWidget(self.tabs)
        
        # Add layout
        nav_area.setLayout(nav_layout)
        main_layout.addWidget(nav_area)

        ## 2 - Entry Area ##

        # Set area config
        entry_area = QWidget()
        entry_area.setMinimumWidth(500)
        entry_layout = QVBoxLayout()

        # Add widgets
        self.current_day = QLabel("11 February 2026")
        entry_layout.addWidget(self.current_day)

        self.entry_edit = QPlainTextEdit()
        self.entry_edit.setPlaceholderText("Write anything here...")
        entry_layout.addWidget(self.entry_edit)
        
        # Add layout 
        entry_area.setLayout(entry_layout)
        main_layout.addWidget(entry_area)

        ## 3 - Timeline Area ##

        # Set area config
        time_area = QWidget()
        time_area.setFixedWidth(300)
        time_layout = QVBoxLayout()

        # Add widgets
        self.calendar = QCalendarWidget()
        self.calendar.setFixedHeight(300)
        time_layout.addWidget(self.calendar)

        self.events = QListWidget()
        self.events.addItems(["Event 1", "Event 2", "Event 3"]) # testing
        time_layout.addWidget(self.events)

        # Add layout 
        time_area.setLayout(time_layout)
        main_layout.addWidget(time_area)
        

        ####


    def _connect_signals(self):
        pass