#empty file
import evdev, time, os

if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print("All input devices:")
    for device in devices:
        print(" path=[", device.path,"], name=[", device.name, "], phys=[",device.phys,"]",sep='')
    if "input_device" in os.environ:
        device = evdev.InputDevice(os.environ["input_device"])
        print("monitoring input:" + device)
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                print(evdev.categorize(event))
    else:
        print("Environment variable input_device is not set !")
    print("sleeping 1 day...")
    time.sleep(3600*24)
