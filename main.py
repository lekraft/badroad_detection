import json
import serial
import pynmea2
import mpu6050 as gyro
import time
from gps3 import gps3

#initialise Json Dict
data = {}
data['gps'] = []

global counter
counter = 0

def logger(str, counter):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print("start logging")
        #reading g force from the gyro sensor
 #       force = gyro.mpu9250.get_accel_data_each()[z]

        #append data
        data['gps'].append({
            'counter': counter,
            'timestamp': msg.timestamp,
            'latitude': msg.lat,
            'longitude': msg.lon,
#            'force': force
        })
        print ("Counter: %s -- Timestamp: %s -- Lat: %s  -- Lon: %s  -- Altitude: %s  -- G Force: %s" % (counter,msg.timestamp,msg.lat,msg.lon,force))
        counter +=1
        
    else:
        print("problem")


print("Starting")

#initialise GPS Sensor
#serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
#time.sleep(10)
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

print("initialized")

#main function which starts gps and g force logging and save the data to a Json file.
while True:

    str = serialPort.readline()
    print("start gps")
    logger(str,counter)

    counter += 1

    #write Json
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
