import random as rand
import requests
import time

THINGSPEAK_API_KEY = "ADD_KEY_HERE"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_to_thingspeak(temp, hum, co2):
    payload = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": temp,
        "field2": hum,
        "field3": co2
    }
    response = requests.get(THINGSPEAK_URL, params=payload)
    print("Response:", response.text)

def gen_temp():
    temp = rand.randint(-50, 50)
    hum = rand.randint(0, 100)
    co2 = rand.randint(300,2000)
    return temp, hum, co2

def main():
    while(1):
        temp, hum, co2 = gen_temp()
        send_to_thingspeak(temp, hum, co2)
        print(temp, hum, co2)
        time.sleep(5)

main()
