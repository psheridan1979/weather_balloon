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
        #print("GPS error")
        return (-1000,-1000,-1000)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Log GPS data to csv file.')
    parser.add_argument("--log_file", help="the path to write the log to", type=str, default="../logs/gps.csv")
    parser.add_argument("--current_file" help="the path to write the most recent data to", type=str, default="../logs/current.csv")
    parser.add_argument("--interval", help="interval between log entries in seconds", type=float, default=5.0)
    args = parser.parse_args()
    file_path = args.log_file
    aprs_path = args.current_file
    interval = args.interval
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time','Lat', 'Lon','Alt(M)'])
        try:
            gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
            print("Waiting for GPS to initialize")
            time.sleep(5.0)
            print("Application started!")
            running = True
            while running:
                with open(current_file, 'w') as current_file:
                    current_writer = csv.writer(current_file)
                    [latitude,longitude,altitude] = getPositionData(gpsd)
                    if latitude != -1000:
                        print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude) + ", alt = " + str(altitude))
                        current_writer.writerow([time.time(),latitude,longitude,altitude])
                        writer.writerow([time.time(),latitude,longitude,altitude])
                        time.sleep(interval)
        except (KeyboardInterrupt):
            running = False
            csvfile.close()
            print("Application closed!")
