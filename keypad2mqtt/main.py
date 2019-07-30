#empty file
import evdev

if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)
    sleep(68000)
