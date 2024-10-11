import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from file_monitor import add_file_to_monitor, start_file_monitoring

class FileMonitorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("File Integrity Monitor")
        self.layout = QVBoxLayout()

        self.add_file_btn = QPushButton("Add File to Monitor", self)
        self.add_file_btn.clicked.connect(self.add_file)

        self.start_monitor_btn = QPushButton("Start Monitoring", self)
        self.start_monitor_btn.clicked.connect(self.start_monitor)

        self.layout.addWidget(self.add_file_btn)
        self.layout.addWidget(self.start_monitor_btn)
        self.setLayout(self.layout)

    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            add_file_to_monitor(file_path)
            print(f"Added {file_path} to monitor")

    def start_monitor(self):
        print("Monitoring started...")
        start_file_monitoring()  # Call function to start monitoring

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = FileMonitorGUI()
    gui.show()
    sys.exit(app.exec_())
