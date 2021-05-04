from MPU_9250 import MPU_9250

sensor = MPU_9250(0x68)

while(1):
	g = sensor.get_gyro_reg()
	a = sensor.get_accel_reg()
	print(g,a)
