#empty file
import evdev, time, os, json
import paho.mqtt.client as mqtt

if __name__ == '__main__':
    try:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        print("All connected USB input devices:")
        device_cnt=0
        for device in devices:
            device_cnt += 1
            print(" ", device_cnt , ": path=[", device.path,"], name=[", device.name, "], phys=[",device.phys,"]",sep='')
        assert (device_cnt>0),\
               "ERROR: no USB input devices connected to the (raspberry pi) device"

        assert (os.environ.get("input_device") is not None), \
               "ERROR: Environment variable \"input_device\" is not set !"
        
        try:
            device = evdev.InputDevice(os.environ["input_device"])
            print("\nThe selected input device (by means of environment variable \"input_device\")=")
            print("  ",device)
        except Exception as error:
            print("ERROR: opening input_device (=\"",os.environ["input_device"], "\") failed",sep='')
            print("       Environment variable \"input_device\" must be equal to the path of one of the connected devices (see above)")
            raise

        print("\nThe capabilities of the selected input device =")
        print(device.capabilities(verbose=True))

        mqttClient=mqtt.Client("keypad2mqtt")
        mqttClient.connect("mqtt",1883)
        mqttClient.loop_start()
        mqttClient.publish("keypad2mqtt","service started")

        print("\nListening to the selected input device ...")
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                keyevent= evdev.categorize(event)
                print(keyevent)
                mqtt_msg=json.dumps({"key" : keyevent.key, "keystate" : keyevent.keystate , "value" : keyevent.value, "timestamp" : keyevent.timestamp })
                mqttClient.publish("keypad2mqtt/raw",str(evdev.categorize(event)))
                mqttClient.publish("keypad2mqtt/EV_KEY",mqtt_msg)

    # all exceptions are handled !
    except Exception as error:
        print(error)

    print("sleeping 1 day...")
    time.sleep(3600*24)
