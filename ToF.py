import VL53L1X


def main():
	tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
	tof.open()	
	tof.start_ranging(3)
	while(True):
		distance_in_mm = tof.get_distance()
		print(distance_in_mm)
	tof.stop_ranging()
		

if __name__=="__main__":
	main()