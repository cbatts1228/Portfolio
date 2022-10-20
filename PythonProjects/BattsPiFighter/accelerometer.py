
import time
import board
import busio
import adafruit_adx134x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adx134x.ADXL345(i2c)

while True:
	print("%f %f %f"%accelerometer.acceleration)
	time.sleep(0.5)
