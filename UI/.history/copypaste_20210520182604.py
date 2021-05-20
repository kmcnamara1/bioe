import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Table(QTableWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setRowCount(10)
        self.setColumnCount(10)
        # etc.

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            self.copied_cells = sorted(self.selectedIndexes())
        elif event.key() == Qt.Key_V and (event.modifiers() & Qt.ControlModifier):
            r = self.currentRow() - self.copied_cells[0].row()
            c = self.currentColumn() - self.copied_cells[0].column()
            for cell in self.copied_cells:
                self.setItem(cell.row() + r, cell.column() + c, QTableWidgetItem(cell.data()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Table()
    gui.show()
    sys.exit(app.exec_())
