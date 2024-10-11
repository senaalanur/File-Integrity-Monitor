# File-Integrity-Monitor

Project Overview:

The File Integrity Monitor is a tool designed to track specified files for modifications and deletions. The program sends email alerts when changes are detected, helping users ensure the integrity of their important files.

Features:

Monitors selected files for changes.
Sends email notifications on modifications or deletions.
User-friendly GUI for easy file management.

Code Review:

1. GUI: gui.py allows users to add files for monitoring and start monitoring with buttons.
 
2. Email Alerts: email_alerts.py sends alerts using a Flask application context.
  
3. File Monitoring: file_monitor.py hashes files to detect changes and manages a JSON file to keep track of monitored files.
 
4. Configuration: files_to_monitor.json keeps a list of files and their hashes.

Achievements:

Email Notification: Successfully implemented email alerts for file modifications and deletions.

User-Friendly Interface: Created a GUI that simplifies adding and monitoring files.

Next Steps:

1.Testing and Validation: Test the application for various use cases, such as adding multiple files, deleting monitored files, etc.
2.User Preferences: Allow users to customize email recipient preferences within the app.
3.Logging: Implement a system to log all file changes and email alerts.
4.Cross-Platform Compatibility: Test the application on multiple operating systems (e.g., Windows, Linux).
5,Improved GUI: Add features like displaying the current list of monitored files, allowing users to remove files from monitoring, or modify alert settings directly from the GUI.

Contributing:

Contributions are welcome! Please feel free to fork this repository and submit pull requests.

Additional Resources:

Flask Documentation = https://flask-mail.readthedocs.io/en/latest/ 
Watchdog Documentation = https://watchdog.readthedocs.io/en/latest/
PyQt5 Documentation = PyQt5 Documentation
