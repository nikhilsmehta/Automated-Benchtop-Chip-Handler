import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(5)
ser.write(b"H")
time.sleep(5)
