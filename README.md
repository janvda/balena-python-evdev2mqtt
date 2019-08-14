# Balena "python-evdev2mqtt" Application

This is a [Balena](https://www.balena.io/) application consisting of 3 docker containers.

1. `python-evdev2mqtt`: this service is sending an mqtt message whenever a key is pressed/hold/released for a specific input device connected to one of the USB ports of a raspberry pi.
1. `mqtt` : mqtt broker receiving the mqtt messages sent by the `python-evdev2mqtt` service.
1. `node-red`: this service has a dual purpose:
   1. It demonstrates that `python-evdev2mqtt`is working properly as it outputs those mqtt messages in the debug window of the node-red editor.
   1. It also demonstrates the (limited) features of the `node-red-contrib-usbhid` nodes that can also be used to receive events from those input devices connected to the USB ports of a raspberry pi.

## Rationale for this Application

The idea is to use ...

## Additional Features

1. Node-red editor can be accessed through the public device URL from the BalenaCloud dashboard.
1. It is also easy to create a [hashed password](https://nodered.org/docs/user-guide/runtime/securing-node-red) for node-red by running the command "`node-red-admin hash-pw`" in a terminal window for the `node-red` service.

## Hardware needed besides a raspberry pi

1. You need an USB device that generates key events (e.g. keypad, keyboard, ...)

## SETUP INSTRUCTIONS

### 1. Deploy Balena application

So as you might have guessed this is indeed a balena application.  So follow all standard instructions for setting up and deploying this balena application. (e.g. see [Get started with Raspberry Pi 3 and Python
](https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/) and its [github repository](https://github.com/balena-io-projects/simple-server-python))
After this step this balena application should be running on your raspberry pi.

### 2. TBD

### 3. Set Device Service Variables for the python-evdev2mqtt container

Within your balenacloud dashboard you must set the following device service variables for the `python-evdev2mqtt` container.

| Service Variable         | Description                                  |
|------------------------- | ---------------------------------------------|
| **TBD**    |  TBD. |

### Interesting Links

1. [python-evdev](https://python-evdev.readthedocs.io/en/latest/)
1. python-evdev package also comes with a small command-line program for listing and monitoring input devices:

```python -m evdev.evtest```
