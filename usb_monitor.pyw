import serial.tools.list_ports
import time
from threading import Thread
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import win32com.client
import subprocess
import os

def get_device_info(port):
    wmi = win32com.client.GetObject("winmgmts:")
    for device in wmi.InstancesOf("Win32_SerialPort"):
        if device.DeviceID == port:
            return device.Name, device.Description
    return None, None

def create_image():
    # Create an image with a simple drawing
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill='black')
    return image

# Funzione per creare l'icona della system tray da un file ICO
def create_icon_from_file(icon_path):
    return Image.open(icon_path)

def open_device_manager(icon, item):
    subprocess.run('devmgmt.msc', shell=True)

def notify_new_port(port, serial, manufacturer, description):
    icon.notify(f'New COM detected: {port}\nSerial: {serial}\nManufacturer: {manufacturer}', title=description)

def monitor_ports():
    previous_ports = set(serial.tools.list_ports.comports())
    while True:
        current_ports = set(serial.tools.list_ports.comports())
        new_ports = current_ports - previous_ports
        if new_ports:
            for port in new_ports:
                notify_new_port(port.device,  port.serial_number,  port.manufacturer,  port.description)
                # print(f"{port.description=}")
                # print(f"{port.device=}")
                # print(f"{port.hwid=}")
                # print(f"{port.interface=}")
                # print(f"{port.location=}")
                # print(f"{port.manufacturer=}")
                # print(f"{port.name=}")
                # print(f"{port.pid=}")
                # print(f"{port.product=}")
                # print(f"{port.serial_number=}")
                # print(f"{port.vid=}")
        previous_ports = current_ports
        time.sleep(1)

icon_file   =   os.path.join    ( os.path.dirname(os.path.abspath(__file__)), 'usb_monitor.ico' )

if os.path.exists( icon_file ):
    icon_img    =   create_icon_from_file   ( icon_file )
else:
    icon_img    =   create_image()

icon = Icon('USB Monitor', icon_img, 'USB Monitor v.0.3', menu=Menu(MenuItem('Open device manager', open_device_manager),  MenuItem('Quit', lambda: icon.stop())))

def run_icon():
    icon.run()

if __name__ == '__main__':
    Thread(target=monitor_ports, daemon=True).start()
    run_icon()
