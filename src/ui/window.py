from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QPushButton,
        QLineEdit,
        QLabel,
)

class MainWindow(QMainWindow):
    def __init__(self, core):
        super().__init__()
        self.core = core

        # Set window settings
        self.setWindowTitle("Journal Lite")

        # Initialize UI
        self._build_ui()
        self._connect_signals()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        #### Build UI elements here ####

        





        ####


    def _connect_signals():
        pass