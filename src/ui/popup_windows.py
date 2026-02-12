from PySide6.QtWidgets import (
    QMessageBox, 
    QDialog,
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QLineEdit, 
    QPushButton
)

class AddItem(QDialog):
    def __init__(self, title="Add Item", message="Enter Item"):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(300, 100)
        self.text = None

        layout = QVBoxLayout()

        # Message label
        label = QLabel(message)
        layout.addWidget(label)

        # Text input
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        # Buttons
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add")
        cancel_button = QPushButton("Cancel")

        add_button.clicked.connect(self.add_clicked)
        cancel_button.clicked.connect(self.cancel_clicked)

        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def add_clicked(self):
        self.accept()
        self.text = self.input_field.text()

    def cancel_clicked(self):
        self.reject()
        self.text = None
    
    def exec_(self):
        super().exec()
        return self.text

class RemoveItem(QMessageBox):
    def __init__(self, message="Do you want to delete the selected tab?"):
        super().__init__()
        self.setWindowTitle("Remove Item")
        self.setText(message)

        # Make it behave like an alert (plays system sound)
        self.setIcon(QMessageBox.Icon.Warning)

        # Add Yes and No buttons
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.setDefaultButton(QMessageBox.StandardButton.No)

    def exec_(self):
        """Executes the message box and returns True for Yes, False for No"""
        result = super().exec()
        return result == QMessageBox.StandardButton.Yes
    
class DeleteItemWarning(QMessageBox):
    def __init__(self, message="You can't delete the default tab"):
        super().__init__()
        self.setWindowTitle("Warning")
        self.setText(message)

        self.setIcon(QMessageBox.Icon.Warning)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setDefaultButton(QMessageBox.StandardButton.Ok)