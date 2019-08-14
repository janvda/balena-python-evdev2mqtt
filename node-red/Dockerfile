
#see https://hub.docker.com/r/nodered/node-red-docker
FROM nodered/node-red-docker:rpi-v8

# run node-red as root user as this is needed to get the HIDdevice node working.
USER root

# is needed if we want to create a hashed password using the node-red terminal window in the balenaCloud dashboard.
# note that installing it globally (-g option) didn't work - there I had to install it locally and next
# RUN command will create a symbolic link so that node-red-admin is in the $PATH
RUN npm install node-red-admin
RUN ln -s  /usr/src/node-red/node_modules/.bin/node-red-admin  /usr/local/bin/node-red-admin

# installing editor nano and usb libraries needed for node-red-contrib-usbhid (https://github.com/LedgerHQ/btchip-python/issues/27)
RUN apt-get update && apt-get install nano libusb-1.0.0-dev libudev-dev

RUN npm install git+https://git@github.com/CCSnell/node-red-contrib-usbhid.git
# it is bit unclear why the installation of the above fork of node-red-contrib-usbhid makes a difference compared to the master version
# but it effectively makes a difference:
#   - The getHIDdevices node provides more detail.
#   - the HIDdevice node seems to be more stable (is always reacting to a device event)
# RUN npm install node-red-contrib-usbhid

RUN npm install node-red-contrib-resinio
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-credentials

COPY ./settings.js /data/settings.js
COPY ./flows.json  /data/flows.json
