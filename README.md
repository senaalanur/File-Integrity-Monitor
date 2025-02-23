# File Integrity Monitor

## Overview

The File Integrity Monitor is a powerful tool designed to track specified files for modifications and deletions, ensuring the security and integrity of important files. When a change is detected, the program promptly sends an email alert, allowing users to take immediate action. This project is particularly useful for security-conscious users, businesses, and IT administrators who need to safeguard critical files from unauthorized changes.

## Purpose & Importance

In today's digital world, file integrity is crucial for maintaining data security. Unauthorized modifications, accidental deletions, or malicious alterations can lead to serious consequences, such as data breaches or system failures. The File Integrity Monitor addresses these concerns by continuously tracking file changes and notifying users instantly, helping prevent data loss and unauthorized access.

### Features

* Real-time File Monitoring: Tracks changes, deletions, and modifications of specified files.

* Email Alerts: Sends notifications when a file is altered or removed.

* User-Friendly GUI: Built with PyQt5 for an intuitive and accessible interface.

* Customizable Monitoring: Allows users to add, remove, and manage files easily.

* Cross-Platform Compatibility: Designed to work on Windows, Linux, and macOS.

* Logging System: Maintains a log of all detected file changes and notifications.

### Code Breakdown

1. Graphical User Interface (GUI)

   File: gui.py

* Provides an interactive PyQt5-based UI.

* Users can select files for monitoring.

* Includes buttons to start and stop monitoring.

2. File Monitoring System

   File: file_monitor.py

* Uses Watchdog to detect file modifications and deletions.

* Hashes files to identify unauthorized changes.

* Stores monitored file information in a JSON file (files_to_monitor.json).

3. Email Alert System

   File: email_alerts.py

* Sends email notifications using Flask-Mail.

* Runs within a Flask application context to ensure email delivery.

* Notifies users immediately of any detected file changes.

4. Configuration File

   File: files_to_monitor.json
 
* Stores the list of monitored files along with their corresponding hashes.

Achievements

* Real-Time Email Notifications: Successfully implemented an automated email alert system for file modifications and deletions.
* User-Friendly Interface: Designed an accessible GUI to simplify file monitoring.
* Data Security Enhancement: Provides an extra layer of security for critical files.

### Next Steps

1- Enhanced Testing & Validation: Test for multiple scenarios such as monitoring multiple files, handling large file sets, and ensuring stability across different OS platforms.

2- User Preference Settings: Enable users to configure recipient email addresses and alert preferences within the application.

3- Advanced Logging: Implement a logging feature to store records of file changes and email notifications.

4- Improved GUI Features: Add real-time status updates, file removal options, and alert customization directly from the UI.

5- Cross-Platform Optimization: Ensure compatibility and smooth operation on Windows, Linux, and macOS.

#### Contribution 

Contributions are welcome! If you'd like to enhance this project, feel free to fork the repository, make modifications, and submit a pull request.

#### Additional Resources

Flask-Mail Documentation - https://flask-mail.readthedocs.io/en/latest/

Watchdog Documentation - https://watchdog.readthedocs.io/en/latest/

PyQt5 Documentation - https://watchdog.readthedocs.io/en/latest/

#### This project is open-source and available under the MIT License. Feel free to customize and improve it to suit your needs! ###

