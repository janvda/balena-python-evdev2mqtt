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

        # MQTT client setup
        mqttBroker= "mqtt" if ( os.environ.get("mqtt_broker") is None ) else os.environ["mqtt_broker"]
        mqttPort  =  1883  if ( os.environ.get("mqtt_port")   is None ) else os.environ["mqtt_port"]

        mqttClient=mqtt.Client("python-evdev2mqtt")
        mqttClient.connect(mqttBroker,mqttPort)
        mqttClient.loop_start()
        
        mqttClient.publish("python-evdev2mqtt/device","service started")

        print("\nListening to the selected input device ...")
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                keyevent= evdev.categorize(event)
                keystate= "key_up" if keyevent.keystate == 0 else "key_down" if keyevent.keystate == 1 else "key_hold" if keyevent.keystate == 2 else "unknown_keystate"
                print(keyevent)
                # see https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.events.InputEvent
                mqtt_msg=json.dumps({"timestamp" : event.timestamp() ,  
                                     "device"    : { "path" : device.path, "name" : device.name, "phys" : device.phys },
                                     "keycode"   : keyevent.keycode, 
                                     "keystate"  :  keystate,
                                     "keystate_raw" : keyevent.keystate , 
                                     "scancode" : keyevent.scancode })
                mqttClient.publish("python-evdev2mqtt/str_key_event",str(evdev.categorize(event)))
                mqttClient.publish("python-evdev2mqtt/key_event",mqtt_msg)

    # all exceptions are handled !
    except Exception as error:
        print(error)

    print("sleeping 1 day...")
    time.sleep(3600*24)
