#----------------------------------
# A bot to crawl the weather underground website to grab the weather data and
# store it in a single csv file. The csv file has 14  columns and 
# 24rows. per day.
#
# Columns: 
# 'TimeEDT' 'TemperatureF' 'Dew PointF' 'Humidity' 'Sea Level PressureIn'
# 'VisibilityMPH' 'Wind Direction' 'Wind SpeedMPH' 'Gust SpeedMPH' 
# 'PrecipitationIn' 'Events' 'Conditions' 'WindDirDegrees' 'DateUTC<br />'
#
# python weatherbot.py start_year start_month start_day end_year end_month end_day
#
# Created by: Mohit Sharma (CUSP/NYU)
# Date: Sept 09 2014
#---------------------------------

import sys
import csv
import urllib2

url = 'http://www.wunderground.com/history/airport/KNYC/%d/%d/%d/DailyHistory.html?req_city=Manhattan&req_state=NY&req_statename=New+York&format=1'

def readurl(year1, month1, day1, year2, month2, day2):
    #-- Loop through years, months and days
    for y in range(year1,year2+1):
        print 'Year: %d'%y
        for m in range(month1,month2+1):
            print 'Month: %d'%m
            for d in range(day1,day2+1):
                print 'Day: %d'%d
                path = url %(y,m,d)
                print 'Fetching: %s'%path
                data = urllib2.urlopen(path)
                reader = csv.reader(data)
                r = [row for row in reader]
                #-- Append to existing csv file
                with open("/home/mohit/Documents/weather.csv","a") as f:
                    writer = csv.writer(f)
                    writer.writerows(r[2:26])


if __name__ == "__main__":
    #-- Call function with command line arguments
    n = [int (x) for x in sys.argv[1:]]
    readurl(n[0],n[1],n[2],n[3],n[4],n[5])
