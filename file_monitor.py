import os
import hashlib
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from email_alerts import send_email_alert  # Import the email alert function

# Function to Hash Files Using SHA256
def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None

# File Monitoring Event Handler (Watchdog)
class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, file_list):
        self.file_list = file_list

    def on_modified(self, event):
        if event.src_path in self.file_list:
            print(f"File modified: {event.src_path}")
            current_hash = hash_file(event.src_path)
            if current_hash != self.file_list[event.src_path]:
                print(f"Warning: {event.src_path} has been altered!")
                send_email_alert(event.src_path)  # Send an email alert
                self.file_list[event.src_path] = current_hash
                self.update_file_list()

    def on_deleted(self, event):
        if event.src_path in self.file_list:
            print(f"File deleted: {event.src_path}")
            send_email_alert(event.src_path)  # Send an email alert for deletion
            del self.file_list[event.src_path]
            self.update_file_list()

    def update_file_list(self):
        with open('files_to_monitor.json', 'w') as f:
            json.dump(self.file_list, f, indent=4)
        print("File list updated!")

# Load the File List from JSON
def load_file_list(file_list_path='files_to_monitor.json'):
    if os.path.exists(file_list_path):
        with open(file_list_path, 'r') as f:
            return json.load(f)
    else:
        print(f"{file_list_path} does not exist. Creating a new file.")
        return {}

# Add a New File to Monitor
def add_file_to_monitor(file_path, file_list_path='files_to_monitor.json'):
    file_list = load_file_list(file_list_path)
    if file_path not in file_list:
        file_list[file_path] = hash_file(file_path)
        with open(file_list_path, 'w') as f:
            json.dump(file_list, f, indent=4)
        print(f"Added {file_path} to monitoring list.")

# Function to start monitoring files
def start_file_monitoring():
    file_list = load_file_list()

    event_handler = FileMonitorHandler(file_list)
    observer = Observer()

    # Monitor the directory where the files are located
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        print("Monitoring started. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Keep the observer running
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
