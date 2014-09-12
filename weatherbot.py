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
import calendar
from datetime import datetime

url = 'http://www.wunderground.com/history/airport/KNYC/%d/%d/%d/DailyHistory.html?req_city=Manhattan&req_state=NY&req_statename=New+York&format=1'

def diff_month(d2,d1):
    return(d2.year-d1.year)*12 + d2.month-d1.month

def readurl(year1, month1, day1, year2, month2, day2):
    print 'starting'
    #-- Find number of days in a month
    a = diff_month(datetime(year2,month2,1), datetime(year1,month1,1))
    print a
    n = 1
    y = year1

    for m in range(month1, month1+a+a/12):
            if(m % 13*n == 0):
                y = y + 1
                n = n + 1

            #-- m%m =0, to remove that
            if(m%13 != 0):
                dmod = (calendar.monthrange(y,m%13)[1])                
                for d in range(1,dmod+1):
                    #-- Join year/month/dates
                    path = url %(y,m%13,d%32)
                    print 'Fetching for: %d %d %d'%(y,m%13,d)
                    data = urllib2.urlopen(path)
                    reader = csv.reader(data)
                    r = [row for row in reader]
                    #-- Append to existing csv file
                    with open("/home/mohitsharma44/devel/weather.csv","a") as f:
                        writer = csv.writer(f)
                        writer.writerows(r[2:])


if __name__ == "__main__":
    #-- Call function with command line arguments
    n = [int (x) for x in sys.argv[1:]]
    readurl(n[0],n[1],n[2],n[3],n[4],n[5])
