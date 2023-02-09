# galmplaat

The setup consists of two raspberri Pi 4B computers with a pisound sound card.
Device 1 is connected with it's audio out (mono) to the reverb plate, and the stereo output is connected back to the pisound.
There is also a circuit connected to 2 GPIO pins driving the motor controls of the reverb plate
It is connected to the internet for receiving audio and sending the processed audio back.

Device 2 is connected to the internet and has mono audio send and stereo receive. The controls are a standard midi controller.


## device 1 (connected to galmplaat)

### install base image on pisound
follow instructions [here](https://blokas.io/patchbox-os/#patchbox-os-download)

### install dependencies
```
sudo apt update
sudo apt upgrade
sudo apt install qtbase5-dev qt5-qmake qtbase5-dev-tools
sudo apt install --no-install-recommends build-essential
sudo apt install --no-install-recommends autoconf automake libtool make libjack-jackd2-dev git help2man
sudo apt install qjackctl qt5-qmake qttools5-dev libqt5svg5-dev libqt5networkauth5-dev qtdeclarative5-dev qml-module-qtquick-controls libqt5websockets5-dev
sudo apt -y install qml-module-qtquick-controls2 
sudo apt install librtaudio-dev
```
### clone
```
git clone --recurse-submodules https://github.com/jacktrip/jacktrip.git
```
### build
```
cd jacktrip
./build
```
### create service to start jacktrip
clone this repo



