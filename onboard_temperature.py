import machine
from utime import sleep

def main():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    
    for i in range(1000):
        reading = sensor_temp.read_u16() * conversion_factor 
        temperature = 27 - (reading - 0.706)/0.001721
        print(temperature)
        sleep(2)
        

if __name__ == '__main__':
    main()