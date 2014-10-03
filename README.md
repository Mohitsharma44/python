python scripts
======

1. histogram_matching:


  Mapping Histogram of reference Image
  to other Image.

  Logic: Given two images, the reference and the adjusted images,
  we compute their histograms. Following, we calculate the
  cumulative distribution functions of the two images' histograms - 
  hist_ref(), for the reference image and hist_adj(), for the target
  image. Then for each gray level in tables=[0,255], we find another
  gray level table, for which hist_dst[i]>=hist_ref(j), and this is 
  the result of histogram matching function: M(x)=dst_ref,.
  
  Finally, we apply the function M(), on each pixel of the reference 
  image. 

2. raw2jpg.py:

  Converting RAW images to JPG
  Requires:
  a. [DST13]()

3. Weatherbot:

 A bot to crawl the weather underground website to grab the weather data and
 store it in a single csv file. The csv file has 14  columns and 
 24rows. per day.
Columns: 
 'TimeEDT' 'TemperatureF' 'Dew PointF' 'Humidity' 'Sea Level PressureIn'
 'VisibilityMPH' 'Wind Direction' 'Wind SpeedMPH' 'Gust SpeedMPH' 
 'PrecipitationIn' 'Events' 'Conditions' 'WindDirDegrees' 'DateUTC'
 
 Run:
```python
 python weatherbot.py start_year start_month start_day end_year end_month end_day
```
