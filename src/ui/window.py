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
        QPushButton,
        QCheckBox,
        QSizePolicy,
)

from PySide6.QtGui import (
    Qt,
    QFont,
)

from PySide6.QtCore import (
    QDate,
)

from src.ui.popup_windows import (
    AddItem,
    RemoveItem, 
    DeleteItemWarning,
) 

class MainWindow(QMainWindow):

    

    def __init__(self, core):
        super().__init__()
        self.core = core

        self.DEFAULT_TAB = "General"
        self.is_autosaving = True

        # Set window settings
        self.setWindowTitle("Journal Lite")
        self.resize(1200, 800)

        # Initialize UI
        self._build_ui()
        self._apply_styling()
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
        self.tabs.addItems(["General"])
        self.tabs.setCurrentRow(0)
        nav_layout.addWidget(self.tabs)

        button_area = QHBoxLayout()
        self.add_tab_button = QPushButton("Add Tab")
        button_area.addWidget(self.add_tab_button)
        self.del_tab_button = QPushButton("Delete Tab")
        button_area.addWidget(self.del_tab_button)
        nav_layout.addLayout(button_area)
        
        # Add layout
        nav_area.setLayout(nav_layout)
        main_layout.addWidget(nav_area)

        ## 2 - Entry Area ##

        # Set area config
        entry_area = QWidget()
        entry_area.setMinimumWidth(500)
        entry_layout = QVBoxLayout()

        # Add widgets
        self.current_day_label = QLabel() 
        # self.current_day.setText("11 February 2026") # testing
        entry_layout.addWidget(self.current_day_label)

        self.entry_edit = QPlainTextEdit()
        self.entry_edit.setPlaceholderText("Write anything here...")
        entry_layout.addWidget(self.entry_edit)
        push_entry_area = QHBoxLayout()
        self.push_entry_button = QPushButton("Push Entry")
        self.push_entry_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        push_entry_area.addWidget(self.push_entry_button)
        self.autosave_option = QCheckBox("Autosave")
        
        push_entry_area.addWidget(self.autosave_option)
        entry_layout.addLayout(push_entry_area)
        
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
        self.calendar.setSelectedDate(QDate.currentDate())
        time_layout.addWidget(self.calendar)

        self.events = QListWidget()
        # self.events.addItems(["Event 1", "Event 2", "Event 3"]) # testing
        time_layout.addWidget(self.events)

        event_button_area = QHBoxLayout()
        self.add_event_button = QPushButton("Add Event")
        event_button_area.addWidget(self.add_event_button)
        self.del_event_button = QPushButton("Delete Event")
        event_button_area.addWidget(self.del_event_button)
        time_layout.addLayout(event_button_area)

        # Add layout 
        time_area.setLayout(time_layout)
        main_layout.addWidget(time_area)

        ####

        ## Set initial UI appearance
        self.current_day_label.setText(self.calendar.selectedDate().toString())
        self.push_entry_button.setEnabled(False)
        self.autosave_option.setChecked(True)
        self._on_date_changed()

    def _apply_styling(self):
        stylesheet = self._load_stylesheet("src/ui/style.qss")
        self.setStyleSheet(stylesheet)

    def _load_stylesheet(self, path):
        with open(path, "r") as f:
            return f.read()

    def _connect_signals(self):
        self.push_entry_button.clicked.connect(self._on_entry_button_clicked)
        self.calendar.selectionChanged.connect(self._on_date_changed)
        self.autosave_option.toggled.connect(self._on_autosave_changed)
        self.entry_edit.textChanged.connect(self._on_entry_edit_changed)
        self.add_tab_button.clicked.connect(self._on_add_tab_clicked)
        self.del_tab_button.clicked.connect(self._on_del_tab_clicked)
        self.tabs.currentItemChanged.connect(self._on_tab_changed)

    def _on_date_changed(self):
        # Block tab change signals
        self.tabs.blockSignals(True)

        selected_date = self.calendar.selectedDate().toString()

        # Change date label
        self.current_day_label.setText(selected_date)

        # Update tabs
        self.tabs.clear()
        all_entries = self.core.get_all_entries_by_date(self._get_calendar_date())
        for entry in all_entries:
            self._add_item(self.tabs, entry.tab_name)

        # If no general tab add it
        if len(all_entries) == 0:
            self._add_item(self.tabs, self.DEFAULT_TAB)

        self.tabs.setCurrentRow(0)

        # Unblock tab change signals
        self.tabs.blockSignals(False)
        self._on_tab_changed()
        

    def _on_entry_button_clicked(self): self.core.add_entry(*self._get_entry())
    def _get_calendar_date(self): return self.calendar.selectedDate().toPython()
    def _get_selected_tab(self): return self.tabs.currentItem().text()
    def _get_entry_content(self): return self.entry_edit.toPlainText()
    def _get_entry(self): return (self._get_calendar_date(), self._get_selected_tab(), self._get_entry_content())
    
    def _on_autosave_changed(self, checked):
        self.is_autosaving = checked
        self.push_entry_button.setEnabled(not self.is_autosaving)

    def _on_entry_edit_changed(self): 
        if not self.is_autosaving: return
        print("Autosaving is not working right this moment") # testing
        # self.core.add_entry(*self._get_entry())

    def _on_add_tab_clicked(self):
        dialog = AddItem()
        result = dialog.exec_()

        if result:
            tab_name = result
            self._add_item(self.tabs, tab_name)
            self.core.add_entry(self._get_calendar_date(), tab_name, "")
        else:
            return

    def _on_del_tab_clicked(self):
        selected_item = self.tabs.currentItem()

        if selected_item.text().lower() == "general":
            popup = DeleteItemWarning()
            popup.exec()
        else:
            popup = RemoveItem()
            result = popup.exec_()
            if result:
                self.core.delete_tab(self._get_calendar_date(), self._get_selected_tab())
                self._remove_item(self.tabs, selected_item)
            else:
                return

    def _remove_item(self, list, selected_item): list.takeItem(list.row(selected_item))
    def _add_item(self, list, tab_name: str): list.addItem(tab_name)

    def _on_tab_changed(self):
        # Change tab entry
        current_entry = self.core.get_entry_by_tab(self._get_calendar_date(), self._get_selected_tab())
        if current_entry == "":
            self.entry_edit.setPlainText(current_entry)
        else:
            self.entry_edit.setPlainText(current_entry.entry)