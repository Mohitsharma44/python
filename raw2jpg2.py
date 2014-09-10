import dst13
import scipy
import sys
import os
import cv2

if __name__=='__main__':
    dir='/home/mohit/Desktop/vis/'
    files = sorted([f for f in os.listdir(dir)])
    for f in files:
        print "Processing Image %s \n\n"%f
        n = dir+f
        scipy.misc.imsave('/home/mohit/Pictures/%s.jpg'%f,dst13.read_raw(n))

        
