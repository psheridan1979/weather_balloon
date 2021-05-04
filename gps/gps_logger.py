from gps import *
import time
import argparse
import csv

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        altitude = getattr(nx, 'alt', "Unknown")
        return (latitude, longitude, altitude)
    else:
        print("GPS error")
        return (0,0,0)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Log GPS data to csv file.')
    parser.add_argument("--log_file", help="the path to write the log to", type=str, default="../logs/gps.csv")
    args = parser.parse_args()
    print(args.log_file)
    file_path = args.log_file
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time','Lat', 'Lon','Alt(M)'])
        try:
            gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
            print("Waiting for GPS to initialize")
            nx = gpsd.next()
            while nx['class'] != 'TPV':
                nx = gpsd.next()
            print("Application started!")
            running = True
            while running:
                [latitude,longitude,altitude] = getPositionData(gpsd)
                print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude) + ", alt = " + str(altitude))
                writer.writerow([time.time(),latitude,longitude,altitude])
                time.sleep(1.0)
        except (KeyboardInterrupt):
            running = False
            print("Application closed!")