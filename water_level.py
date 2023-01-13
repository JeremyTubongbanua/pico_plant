from machine import ADC
from utime import sleep

def main():
    # gpo 27 is analog in (ADC1 on the pin map)
    adc = ADC(27)

    for i in range(1000):
        # read analog value from pin
        value = adc.read_u16()

        # print analog value
        print(value)

        # wait 2 seconds
        sleep(2)

if __name__ == '__main__':
    main()