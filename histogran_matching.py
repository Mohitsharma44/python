# ----------------------------------------
#
#  Mapping Histogram of reference Image
#  to other Image.
#
#  Logic: Given two images, the reference and the adjusted images,
#  we compute their histograms. Following, we calculate the
#  cumulative distribution functions of the two images' histograms - 
#  hist_ref(), for the reference image and hist_adj(), for the target
#  image. Then for each gray level in tables=[0,255], we find another
#  gray level table, for which hist_dst[i]>=hist_ref(j), and this is 
#  the result of histogram matching function: M(x)=dst_ref,.
#  Finally, we apply the function M(), on each pixel of the reference 
#  image. 
#
#
#  Created by Mohit Sharma (CUSP/NYU)
#  Date: Aug 22 2014
#
# ----------------------------------------
import numpy as np
import cv
import sys

def channels_split(image):
    # -- split channels into individual channels
    channel = []
    # -- all rows and cols  will have 8 bit unisg value
    for x in range(0,3):
        channel.append(cv.CreateMat(image.rows, image.cols, cv.CV_8UC1))
    cv.Split(image,channel[0], channel[1], channel[2], None)
    return channel

def cdf(channel):
    # -- find cum dist func for individual channel
    # -- find cumulative histogram and calculate hist to find
    #    which bin (between 0,255) corresponds to what value 
    #    and store in refHist
    hist = cv.CreateHist([256],cv.CV_HIST_ARRAY,[[0,256]],1)
    cv.CalcHist([cv.GetImage(channel)],hist)
    refHist = [cv.QueryHistValue_1D(hist,x) for x in range(0,256)]
    # -- calculate cdf
    cdf = [v/np.sum(refHist[:]) for v in refHist[:]]
    for x in range(1,256):
        cdf[x] += cdf[x-1]
    return cdf
        
def cdf_all(channel):
    return [cdf(i) for i in channel]

       
def match(ref,adj):
    # -- find histogram matching function
    i = 0;
    j = 0;
    matchtable = range(0,256)
    for i in range(1,256):
        for j in range(1,256):
            if ref[i] <= adj[j]:
               matchtable[i] = j
               break
    matchtable[255] = 255
    return matchtable


if __name__ == '__main__':

    #-- Reading the jpg images
    refImg = cv.LoadImageM('/home/mohit/devel/python/img1.jpg')
    adjImg = cv.LoadImageM('/home/mohit/devel/python/img2.jpg')

    # -- Split image to individual channels
    sys.stdout.write("\n\n\nSplitting Image into 3 Channels...")
    refch = channels_split(refImg)
    adjch = channels_split(adjImg)
    sys.stdout.write("\tDone\n\n")
    
    # -- output original image
    cv.NamedWindow("Original Image",cv.CV_WINDOW_NORMAL)
    cv.ShowImage('Original Image',adjImg)

    # -- get cdf for the images
    sys.stdout.write("Calculating cumulative distribution functions...")
    cdf_ref = cdf_all(refch)
    cdf_adj = cdf_all(adjch)
    sys.stdout.write("\tDone\n\n")

    # -- histogram matching function
    sys.stdout.write("Generating Histogram Matching function...")
    matchfunc= [match(cdf_adj[i],cdf_ref[i]) for i in range(0,3)]
    sys.stdout.write("\tDone\n\n")
    
    # -- Apply matching function to individual channels of adjImg
    for i in range(0,3):
        print "Performing Histogram Matching for channel ",i+1
        for rows in range(0,adjch[i].rows):
            for cols in range(0,adjch[i].cols):
               val = adjch[i][rows,cols]
               adjch[i][rows,cols] = matchfunc[i][int(val)]
    cv.Merge(adjch[0],adjch[1],adjch[2],None,adjImg)

    # -- output reference and processed images
    print "\n\nOpening Preview..."
    cv.NamedWindow("Reference Image", cv.CV_WINDOW_NORMAL)
    cv.ShowImage('Reference Image', refImg)
    cv.NamedWindow("Histogram Matched Image", cv.CV_WINDOW_NORMAL)
    cv.ShowImage('Histogram Matched Image', adjImg)
    cv.WaitKey(0)
