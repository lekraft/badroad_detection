from gps3 import gps3
import json
import mpu6050 as mpu6050
import time
from time import gmtime, strftime

print("started")

#initialise Json Dict
data = {}
data['gps'] = []

global counter
counter = 0

#initialize GPS and MPU
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sensor = mpu6050.mpu6050(0x68)

time.sleep(6)
print("initializied")

#run logging
for new_data in gps_socket:
    if new_data:

        #get GPS data
        data_stream.unpack(new_data)

        #get MPU data
        forcedata = sensor.get_accel_data_each()[2]

        time = strftime("%Y-%m-%d %H:%M:%S")
        data['gps'].append({
            'counter': counter,
            'timestamp': time,
            'latitude': data_stream.TPV['lat'],
            'longitude': data_stream.TPV['lon'],
            'force': forcedata
        })

        print ("Counter: %s -- Timestamp: %s -- Lat: %s  -- Lon: %s  -- Force: %s" % (counter,time,data_stream.TPV['lat'],data_stream.TPV['lon'],forcedata))
        counter +=1

        #write Json
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)


        
