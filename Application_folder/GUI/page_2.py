"""
Made: 01-14-2023
"""

# Create the second page
self.page2 = QWidget()
self.page2Layout = QFormLayout()
self.page2Layout.addRow("Job:", QLineEdit())
self.page2Layout.addRow("Department:", QLineEdit())
self.page2.setLayout(self.page2Layout)
