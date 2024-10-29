# USB COM Port Monitor
This Python script continuously monitors USB COM ports and displays a notification whenever a new port is detected. It runs in the background without opening a console window.

## Features
- _Real-time Monitoring_: Continuously checks for new USB COM ports.
- _System Tray Icon_: Displays an icon in the system tray.
- _Notifications_: Shows a popup notification when a new COM port is detected.
- _Silent Execution_: Runs without opening a console window.

## Requirements
- Python 3.x
- `pyserial` library
- `pystray` library
- `Pillow` library

## Installation
Install the required libraries:
- `pip install pyserial pystray Pillow`

Save the script as monitor_ports.pyw to ensure it runs without a console window.

## Usage
Run the script by double-clicking monitor_ports.pyw.
The script will start monitoring USB COM ports and display notifications for new ports.
If you are under Windows 11 you just have to launch usb_monitor.exe directly and try to connect a USB COM device

## License
This project is licensed under the MIT License.
