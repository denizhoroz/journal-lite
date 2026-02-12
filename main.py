import sys
from PySide6.QtWidgets import QApplication

from src.ui.window import MainWindow
from src.backend.core import Core
from src.backend.database import engine
from src.backend.models import Base

def main():
    # Connect to database
    Base.metadata.create_all(engine)

    # Create application instance
    app = QApplication(sys.argv)

    # Initialize backend and UI
    core = Core()
    window = MainWindow(core)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()