import Adafruit_DHT
while True:
    hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)

    if temp and hum:
        print(temp, hum)
    else:
        print("None")

