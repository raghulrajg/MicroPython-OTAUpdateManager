# OTAUpdateManager
Implementation of OTA for remote monitoring and control of IoT devices

[![micropython](https://img.shields.io/badge/micropython-Ok-purple.svg)](https://micropython.org)

[![ESP8266](https://img.shields.io/badge/ESP-8266-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp8266)

[![ESP32](https://img.shields.io/badge/ESP-32-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32)
[![ESP32](https://img.shields.io/badge/ESP-32S2-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32-s2)
[![ESP32](https://img.shields.io/badge/ESP-32C3-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32-c3)


## Contents
 - [How it works](#how-it-works)
 - [Quick start](#quick-start)
   - [Installing](#installing)
     - [Arduino - Through Library Manager](#install-through-library-manager)
     - [Arduino - From Github](#checkout-from-github)
   - [Using](#using)
 - [Documentation](#documentation)
   - [Server connection configuration](#Server-connection-configuration)

## How It Works

### User Connection:
- Manually enter the network name (SSID) and password.

### MQTT Connection:
- The ESP can connect to an MQTT server to check for updates and maintain a live connection.
- This connection allows for monitoring the live online state and managing updates.

- Use the web application to check the live online state.
- Upload new code to the ESP board through the update section.

## How It Looks
ESP8266/ESP32 modules OTA update and monitoring using [website](https://ota.serveo.net/).
![Homepage](https://i.imgur.com/3LIUSZR.png) ![user dashboard](https://i.imgur.com/sccSpXp.png) ![program editor](https://i.imgur.com/DLfxktF.png)

## Quick Start

### Installing

#### Installing with mip

Py-file
```python
import mip
mip.install('github:raghulrajg/MicroPython-OTAUpdateManager/OTAUpdateManager.py')
```

To install using mpremote

```bash
    mpremote mip install github:raghulrajg/MicroPython-OTAUpdateManager
```

To install directly using a WIFI capable board

```bash
    mip.install("github:raghulrajg/MicroPython-OTAUpdateManager")
```

#### Installing Library Examples

If you want to install library examples:

```bash
    mpremote mip install github:raghulrajg/MicroPython-OTAUpdateManager/examples.json
```

To install directly using a WIFI capable board

```bash
    mip.install("github:raghulrajg/MicroPython-OTAUpdateManager/examples.json")
```

#### Installing from PyPI

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/MicroPython-OTAUpdateManager/>`_.
To install for current user:

```bash
    pip3 install MicroPython-OTAUpdateManager
```

To install system-wide (this may be required in some cases):


```bash
sudo pip3 install MicroPython-OTAUpdateManager
```
To install in a virtual environment in your current project:

```bash
    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install MicroPython-OTAUpdateManager
```

Also see [examples](https://github.com/raghulrajg/OTAUpdateManager/tree/main/test).

## Using
This library provides a OTA update
    1. handling code updates during boot (OTAUpdateManager)

Put the file name is called main.py
```python
import OTAUpdateManager

#Avoid the GPIO pin number 2 because of predefine pin
#create your User ID and Token in https://ota.serveo.net/

#server connection config
User = b"YOUR_USER_ID"
Token = b"YOUR_TOKEN"

#WiFI Network connection config
SSID = "YOUR_APN_NAME"
Password = "YOUR_APN_PASSWORD"

OTAUpdate = OTAUpdateManager.espFOTA(User, Token, SSID, Password)

def loop():
    while True:
        #Put your code here
        OTAUpdate.run()

if __name__ == '__main__':
    loop()
```
Here's the provided `main.py` file, which includes configuration details for connecting to a Wi-Fi network and checking for OTA (Over-the-Air) updates using a user ID and token. You need to fill in your actual Wi-Fi credentials, user ID, and token.

## Documentation

### Server connection configuration

#### Connecting to the Web Application:
- Go to the website: https://ota.serveo.net/.
- Log in to the web application.

#### Token Configuration:
- In the Token section, a default token is created.
- Copy the UserID and Token from this section.

#### Example Code Integration:
- Paste the UserID and Token into your example code.
- Set your connection method to either manual WiFi or APN.

#### Upload Program:
- Upload the program to the ESP.
- The ESP will connect to the MQTT server and send packets to keep the connection alive.

### OTA Update Process

#### Update Detection:
- The server will notify the ESP when an update is available.
- The ESP receives a payload to prepare for the update.
 
#### Update Execution:
- Once the update process is initiated, the ESP will start updating.
- The update status can be monitored on the website in the status section.

