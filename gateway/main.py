import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "vantri15042003"
AIO_KEY = "aio_Erbj63rQcxAHYjaJ9RzeNrcNHYgN"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    if feed_id == "nutnhan1" :
        if payload == "1":
            sendData("bat may 1")
        else :
            sendData("tat may 1")
    elif feed_id == "nutnhan2" :
        if payload == "1":
            sendData("bat may 2")
        else :
            sendData("tat may 2")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
counter_ai = 5

ai_res = ""
prev_ai_res = ""

while True:
    readSerial(client)
    # # Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)

    # # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
    #     break
    time.sleep(1)
    pass