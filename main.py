import json
import serial
import pynmea2
import mpu6050 as gyro

#initialise Json Dict
data = {}
data['gps'] = []

global counter
counter = 0

def logger(str, counter):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)

        #reading g force from the gyro sensor
        force = gyro.mpu9250.get_accel_data_each()[z]

        #append data
        data['gps'].append({
            'counter': counter,
            'timestamp': msg.timestamp,
            'latitude': msg.lat,
            'longitude': msg.lon,
            'force': force
        })
        print ("Counter: %s -- Timestamp: %s -- Lat: %s  -- Lon: %s  -- Altitude: %s  -- G Force: %s" % (counter,msg.timestamp,msg.lat,msg.lon,force))
        counter +=1


print("Starting")

#initialise GPS Sensor
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

print("initialized")

#main function which starts gps and g force logging and save the data to a Json file.
while True:

    str = serialPort.readline()
    logger(str,counter)

    counter += 1

    #write Json
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
