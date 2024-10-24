USB COM Port Monitor
This Python script continuously monitors USB COM ports and displays a notification whenever a new port is detected. It runs in the background without opening a console window.

Features
- Real-time Monitoring: Continuously checks for new USB COM ports.
- System Tray Icon: Displays an icon in the system tray.
- Notifications: Shows a popup notification when a new COM port is detected.
- Silent Execution: Runs without opening a console window.

Requirements
- Python 3.x
- pyserial library
- pystray library
- Pillow library

Installation
Install the required libraries:
- pip install pyserial pystray Pillow

Save the script as monitor_ports.pyw to ensure it runs without a console window.

Usage
Run the script by double-clicking monitor_ports.pyw.
The script will start monitoring USB COM ports and display notifications for new ports.

License
This project is licensed under the MIT License.
