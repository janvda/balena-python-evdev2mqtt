
#see https://hub.docker.com/r/nodered/node-red-docker
FROM nodered/node-red-docker:rpi-v8

USER root

# installing editor nano and usb libraries needed for node-red-contrib-usbhid (https://github.com/LedgerHQ/btchip-python/issues/27)
RUN apt-get update && apt-get install nano libusb-1.0.0-dev libudev-dev

# following command should assure that user node-red can use sudo without requiring to enter a password.
#RUN echo "node-red ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# see https://flows.nodered.org/node/node-red-contrib-usbhid
#RUN mkdir -p /etc/udev/rules.d 
#COPY ./85-pure-data.rules /etc/udev/rules.d
#RUN groupadd -f input
#RUN gpasswd -a node-red input

#USER node-red

#RUN npm install git+https://git@github.com/CCSnell/node-red-contrib-usbhid.git
RUN npm install node-red-contrib-usbhid
RUN npm install node-red-contrib-resinio
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-credentials


COPY ./settings.js /data/settings.js
