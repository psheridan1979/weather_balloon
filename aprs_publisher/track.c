#include "aprs.h"
#include "gps.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_LINE_LENGTH 80
#define APRS_CALLSIGN "K6TMS"

const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ",");
            tok && *tok;
            tok = strtok(NULL, ",\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

int main()
{
   char file_path[] = "../logs/current.csv";
   FILE *fd;
   
      char line[MAX_LINE_LENGTH] = {0};

      while(1) 
      {
         if ((fd = fopen(file_path, "r")) != NULL)
         {
            fgets(line, MAX_LINE_LENGTH, fd );
            if (line[0] != '\0')
            {
               printf(line);
               char *line_duplicate = strdup(line);
               const char *time = getfield(line_duplicate, 1);
               line_duplicate = strdup(line);
               const char *lat = getfield(line_duplicate, 2);
               line_duplicate = strdup(line);
               const char *lon = getfield(line_duplicate, 3);
               line_duplicate = strdup(line);
               const char *alt = getfield(line_duplicate, 4);
               printf("Time: %s\n", time);
               printf("Lat: %s\n", lat);
               printf("Lon: %s\n", lon);
               printf("Alt: %s\n", alt);

               struct TGPS GPS;
               char *ptr;
               GPS.Altitude = atoi(alt);
               GPS.Latitude = strtod(lat, &ptr);
               GPS.Longitude = strtod(lon, &ptr);
               GPS.EpochTime = atoi(time);
               GPS.AscentRate = 0.0;
               GPS.BatteryVoltage = 0.0;
               GPS.BMP180Temperature = 0.0;
               GPS.BoardCurrent = 0.0;
               GPS.BurstLatitude = 0.0;
               GPS.BurstLongitude = 0.0;
               GPS.CDA = 0.0;
               GPS.CutdownStatus = csFlightTime;
               GPS.Direction = 0;
               GPS.DS18B20Count = 0;
               //GPS.DS18B20Temperature = {0.0};
               GPS.FlightMode = fmIdle;
               GPS.Hours = 0;
               GPS.Minutes = 0;
               GPS.Seconds = 0;
               GPS.SecondsInDay = 0;
               GPS.SecondsSinceLaunch = 0;

               SendAPRS(&GPS, APRS_CALLSIGN);
               
            }
            fclose(fd);
         }
         if (remove(file_path) == 0)  printf("Deleted successfully\n");
         else printf("Could not delete file\n");
         sleep(5);
      }
   return(1);
}



