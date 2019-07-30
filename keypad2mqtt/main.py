#empty file
import evdev, time

if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print("All input devices:")
    for device in devices:
        print(" parth=[", device.path,"] name=[", device.name, "] phys=[",device.phys,"]")
    print("sleeping 1 hour...")
    time.sleep(3600)
