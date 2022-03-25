import serial
ser = serial.Serial(0)
print(serial.portstr)
ser.baudrate = 19200
ser.port = 'COM1'
ser.timeout(5000)
print(ser.port)
ser.close()
ser.open()