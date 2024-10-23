import serial.tools.list_ports
import time
from threading import Thread
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

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

def notify_new_port(port):
    icon.notify(f'New COM port detected: {port}')

def monitor_ports():
    previous_ports = set(serial.tools.list_ports.comports())
    while True:
        current_ports = set(serial.tools.list_ports.comports())
        new_ports = current_ports - previous_ports
        if new_ports:
            for port in new_ports:
                notify_new_port(port.device)
        previous_ports = current_ports
        time.sleep(1)

icon = Icon('USB Monitor v.0.1', create_image(), menu=Menu(MenuItem('Quit', lambda: icon.stop())))

def run_icon():
    icon.run()

if __name__ == '__main__':
    Thread(target=monitor_ports, daemon=True).start()
    run_icon()
