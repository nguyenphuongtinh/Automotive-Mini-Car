import serial
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 9600)
#global vitri
def in_vitri():
    global vitri
    if (ser.in_waiting>0):
        data = ser.readline()
        data = data.decode()
        data1 = data.rstrip()
        print (data1)
        vitri = data1
    return vitri
        