import math
import time
import board
import adafruit_mpu6050
i=0
listy=[]
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)
'''
for _ in range(10*51):
	if i!=50:
		
		x,y,z = mpu.acceleration
	
	else:
		total=math.sqrt(pow(x,2)+pow(y,2)+pow(z,2))
		#print ("x: "+str(x))
		#print ("y: "+str(y))
		#print ("z: "+str(z))
		print (round(total,0))
		i=0
    i+=1
'''
'''

initRead=math.sqrt()

if total in range(10):
    health-=1
elif total in range(10,20):
    health-=2


'''

def sumSquares(x,y,z):
    return math.sqrt(pow(x,2)+pow(y,2)+pow(z,2))

print("\n"*50)

while True:
    x,y,z=mpu.acceleration
    movement = round(sumSquares(x,y,z),0)
    if movement>=20:
        print(movement)

