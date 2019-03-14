import requests
import json
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
def tindershow():
    req = requests.get("https://randomuser.me/api/").json()
    with open('data.json', 'a') as outfile:
        json.dump(req, outfile)
    print(req["results"][0]["name"]['first'])
    sense.show_message(req["results"][0]["name"]['first'])
tindershow()
while 1:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "left":
                sense.clear(255, 0, 0)
                print('skipppppp')
            elif event.direction == "right":
                sense.clear(0, 255, 0)
                print('bootycall')
            tindershow()
            sleep(1)
            sense.clear()
