import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QHeaderView, QSpinBox, QLineEdit, QLabel, QAbstractItemView
)
from PyQt5.QtGui import QIcon

class ShoppingCart(QWidget):
    def __init__(self):
        super().__init__()
        
        self.items = ["Bananas", "Grapes", "Apples"]
        self.quantities = [1, 1, 1]
        
        screen = QApplication.instance().primaryScreen()
        screenGeometry = screen.geometry()
        screenWidth = screenGeometry.width()
        screenHeight = screenGeometry.height()
        windowWidth = 400
        windowHeight = 500
        x = (screenWidth - windowWidth) // 2
        y = (screenHeight - windowHeight) // 2
        self.setGeometry(x, y, windowWidth, windowHeight)
        self.setWindowTitle("Shopping Cart Manager")
        self.setWindowIcon(QIcon("shoppingcart/images/EmptyIcon.png"))
        
        self.layout = QVBoxLayout()
        self.initUI()
        self.setLayout(self.layout)
        self.setStyleSheet(self.getStyles())

    def initUI(self):
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Item", "Quantity", "Move", "Remove"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.layout.addWidget(self.table)
        
        self.updateTable()
        
        self.addItemLayout = QHBoxLayout()
        self.itemInput = QLineEdit()
        self.addButton = QPushButton("Add Item")
        
        self.itemInput.setPlaceholderText("Enter new item")
        self.addButton.clicked.connect(self.addNewItem)
        
        self.addItemLayout.addWidget(QLabel("New Item:"))
        self.addItemLayout.addWidget(self.itemInput)
        self.addItemLayout.addWidget(self.addButton)
        
        self.layout.addLayout(self.addItemLayout)
    
    def updateTable(self):
        self.table.setRowCount(len(self.items))
        for row, item in enumerate(self.items):
            self.table.setItem(row, 0, QTableWidgetItem(item))
            
            quantityBox = QSpinBox()
            quantityBox.setValue(self.quantities[row])
            quantityBox.setMinimum(1)
            quantityBox.valueChanged.connect(lambda val, r=row: self.updateQuantity(r, val))
            self.table.setCellWidget(row, 1, quantityBox)
            
            moveLayout = QHBoxLayout()
            upButton = QPushButton("▲")
            downButton = QPushButton("▼")
            upButton.clicked.connect(lambda _, r=row: self.moveItem(r, -1))
            downButton.clicked.connect(lambda _, r=row: self.moveItem(r, 1))
            moveLayout.addWidget(upButton)
            moveLayout.addWidget(downButton)
            moveWidget = QWidget()
            moveWidget.setLayout(moveLayout)
            self.table.setCellWidget(row, 2, moveWidget)
            
            removeButton = QPushButton("✖")
            removeButton.clicked.connect(lambda _, r=row: self.removeItem(r))
            self.table.setCellWidget(row, 3, removeButton)
    
    def updateQuantity(self, row, value):
        self.quantities[row] = value
    
    def moveItem(self, row, direction):
        if 0 <= row + direction < len(self.items):
            self.items[row], self.items[row + direction] = self.items[row + direction], self.items[row]
            self.quantities[row], self.quantities[row + direction] = self.quantities[row + direction], self.quantities[row]
            self.updateTable()
    
    def removeItem(self, row):
        del self.items[row]
        del self.quantities[row]
        self.updateTable()
    
    def addNewItem(self):
        newItem = self.itemInput.text().strip()
        if newItem:
            self.items.append(newItem)
            self.quantities.append(1)
            self.itemInput.clear()
            self.updateTable()

    def getStyles(self):
            return """
                QWidget {
                    background-color: #f4f4f4;
                }
                QTableWidget {
                    background-color: white;
                    border: 1px solid #ccc;
                }
                QLabel {
                    color: #333;
                }
                QPushButton {
                    border: 2px outset #ccc;
                    padding: 5px;
                    font-size: 14px;
                }
                QPushButton:pressed {
                    border: 2px inset #ccc;
                }
            """
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingCart()
    window.show()
    sys.exit(app.exec_())
