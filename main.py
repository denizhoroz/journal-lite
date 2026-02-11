import sys
from PySide6.QtWidgets import QApplication
from src.ui.window import MainWindow
from src.backend.core import Core

def main():
    app = QApplication(sys.argv)

    # Create backend
    core = Core()

    # Inject backend into UI
    window = MainWindow(core)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()