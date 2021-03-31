import serial
ser = serial.Serial('COM3') #Receive serial data from 'COM3'
while 1:
    v = ser.readline() #read data from the serial device data tybe : bytes
    try:
        v = v.decode('UTF-8')#decode the data into a string
        if 'NMEA unknown' not in v: #filter garbage data
            if ('$GPRMC' or '$GPGGA') in v: #filter garbage data
                print(v)
    except:
        continue
