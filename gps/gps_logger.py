from gps import *
import time
import argparse

running = True

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print "Your position: lon = " + str(longitude) + ", lat = " + str(latitude)

	gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print "Application started!"
    while running:
        getPositionData(gpsd)
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    print "Applications closed!"

if __name__=='__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("square", help="display a square of a given number", type=int)
	args = parser.parse_args()
	print(args.square**2)
