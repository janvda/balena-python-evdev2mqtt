# Balena "keypad2mqtt" Application

This is a [Balena](https://www.balena.io/) application consisting of a single docker container "`keypad2mqtt`"
which ....

## Rationale for this Application

The idea is to use ...

## Features

1. TBD

## Hardware needed besides a raspberry pi

1. ...

## SETUP INSTRUCTIONS

### 1. Deploy Balena application

So as you might have guessed this is indeed a balena application.  So follow all standard instructions for setting up and deploying this balena application. (e.g. see [Get started with Raspberry Pi 3 and Python
](https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/) and its [github repository](https://github.com/balena-io-projects/simple-server-python))
After this step this balena application should be running on your raspberry pi.

### 2. TBD

### 3. Set Device Service Variables for the keypad2mqtt container

Within your balenacloud dashboard you must set the following device service variables for the `keypad2mqtt` container.

| Service Variable         | Description                                  |
|------------------------- | ---------------------------------------------|
| **TBD**    |  TBD. |

### Interesting Links

1. [python-evdev](https://python-evdev.readthedocs.io/en/latest/)
1. python-evdev package also comes with a small command-line program for listing and monitoring input devices:

```python -m evdev.evtest```
