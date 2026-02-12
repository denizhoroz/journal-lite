from PySide6.QtWidgets import (
    QMessageBox, 
)

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