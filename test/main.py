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
