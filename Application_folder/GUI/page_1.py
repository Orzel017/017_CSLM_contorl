"""
Made: 01-14-2023
"""

# Create the first page
self.page1 = QWidget()
self.page1Layout = QFormLayout()
self.page1Layout.addRow("Name:", QLineEdit())
self.page1Layout.addRow("Address:", QLineEdit())
self.page1.setLayout(self.page1Layout)