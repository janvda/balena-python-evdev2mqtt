#empty file
import evdev, time, os
import paho.mqtt.client as mqtt

if __name__ == '__main__':
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print("All connected input devices:")
    device_cnt=0
    for device in devices:
        device_cnt += 1
        print(" ", device_cnt , ": path=[", device.path,"], name=[", device.name, "], phys=[",device.phys,"]",sep='')
    if "input_device" in os.environ:
        device = evdev.InputDevice(os.environ["input_device"])
        print("\nListening to device:",end='\n  ')
        print(device)
        device.capabilities(verbose=True)
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                print(evdev.categorize(event))
    else:
        print("Environment variable input_device is not set !")
    print("sleeping 1 day...")
    time.sleep(3600*24)
