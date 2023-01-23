# import libraries
import serial
import time

# configure USB port
port = "/dev/ttyUSB0"
baudrate = 9600

# open serial connection
ser = serial.Serial(port, baudrate)
time.sleep(2)

# send 3 bytes of data (RGB value)
ser.write(b'\xFF\x00\xFF')

# close serial connection
ser.close()
