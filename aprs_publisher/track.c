#include "aprs.h"
#include "gps.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
   char *file_path = "../logs/current.csv";
   FILE *fd;
   if ((fd = fopen(file_path, "r")) != NULL)
   {
      char line[MAX_LINE_LENGTH] = {0};

      while(1) 
      {
         fgets(line, MAX_LINE_LENGTH, fd );
         char *line_duplicate = strdup(line);
         const char *time = getfield(line_duplicate, 1);
         const char *lat = getfield(line_duplicate, 2);
         const char *lon = getfield(line_duplicate, 3);
         const char *alt = getfield(line_duplicate, 4);
         printf("Time: %s\n", time);
         printf("Lat: %s\n", lat);
         printf("Time: %s\n", lon);

         struct TGPS GPS;
         char *ptr;
         GPS.Altitude = atoi(alt);
         GPS.Latitude = strtod(lat, &ptr);
         GPS.Longitude = strtod(lon, &ptr);
         GPS.EpochTime = atoi(time);


      }
   }
   else 
   {
      printf("Make sure the gps logger is running");
      exit(0);
   }
   return(1);
}



