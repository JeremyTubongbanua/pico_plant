from machine import Pin
from dht11 import DHT11
from utime import sleep

def main():
    pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
    dht = DHT11(pin)
    for i in range(1000):
        try:
            print('Temperature: %s' %str(dht.temperature))
            print('Humidity: %s\n' %str(dht.humidity))
        except Exception as e:
            print('Failed to get temperature and humidity: %s' %str(e))
            continue
        sleep(2)

if __name__ == '__main__':
    main()