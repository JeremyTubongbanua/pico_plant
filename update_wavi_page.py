
def main():
    # read settings.json
    from lib.at_client.io_util import read_settings
    ssid, password, atSign = read_settings()
    del read_settings

    # connect to wifi
    print('Connecting to WiFi %s...' % ssid)
    from lib.wifi import init_wlan
    init_wlan(ssid, password)
    del ssid, password, init_wlan

    # authenticate into server
    from lib.at_client.at_client import AtClient
    atClient = AtClient(atSign, writeKeys=True)
    del AtClient
    atClient.pkam_authenticate(verbose=True)

    from micropython import const
    key_temperature = const('custom_temperature')
    key_humidity = const('custom_humidity')
    key_water_level = const('custom_water_level')
    key_timestamp = const('timestamp')
    namespace_wavi = const('wavi')
    del const

    for i in range(10000):
        temperature, humidity = get_temperature_and_humidity()
        water_level = get_water_level()
        timestamp = get_current_timestamp()

        str_temperature = str(temperature)
        str_humidity = str(humidity)
        str_water_level = str(water_level)
        str_timestamp = str(timestamp)

        print('Temperature: %s' % str_temperature)
        print('Humidity: %s' % str_humidity)
        print('Water Level: %s' % str_humidity)
        print('Timestamp: %s' % str_timestamp)

        atClient.put_public(key_temperature, str_temperature, namespace=namespace_wavi)
        atClient.put_public(key_humidity, str_humidity, namespace=namespace_wavi)
        atClient.put_public(key_water_level, str_water_level, namespace=namespace_wavi)
        atClient.put_public(key_timestamp, str_timestamp)

def get_temperature_and_humidity():
    from dht11 import DHT11
    from machine import Pin
    dht = DHT11(Pin(0, Pin.OUT, Pin.PULL_DOWN))
    del Pin, DHT11
    try:
        temperature = dht.temperature
        humidity = dht.humidity
    except Exception:
        temperature = 0
        humidity = 0
    return temperature, humidity

def get_water_level():
    from machine import ADC
    adc = ADC(27)
    del ADC

    from utime import sleep_ms
    sleep_ms(100)
    del sleep_ms

    water_level = adc.read_u16()
    return water_level

def get_current_timestamp():
    from utime import time
    timestamp = time()
    del time
    return timestamp

if __name__ == '__main__':
    main()