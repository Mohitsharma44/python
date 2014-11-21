from numpy import genfromtxt
from matplotlib import pyplot as plt
import numpy as np
import PIL
import matplotlib.animation as animation
from pylab import *

def csv2np(path):
    csvfile = genfromtxt(path,delimiter=',')
    cols = csvfile.shape[0]
    frames = cols/240
    nparray = np.zeros((240,320,frames))
    i=j=count = 0
    k = -1
    for j in range (0,cols):
        count = count + 1
        if (j%240 == 0):
            count = 0
            k = k + 1
            print "Reading Frame %s"%k
        for i in range (0,320):
            nparray[count][i][k] = csvfile[j][i]
            
    return nparray

def np2img(path):
    i=j=0
    nparray = csv2np(path)
    print "Processing Frame 0"
    z = np.zeros((240,320))
    for i in range (0,240):
        for j in range(0,320):
            z[i][j]=nparray[i][j][0]
            
    return z

def img2plt(path):
    z = np.zeros((240,320))
    z = np2img(path)
    plt.imshow(z, cmap=plt.cm.gray, vmin=z.min(), vmax=z.max())
    colorbar()
    #savefig('foo1.png')
    plt.show()

'''
def animate(path):
    nparray = np.zeros((240,320,75))
    nparray = csv2np(path)
    fig = plt.figure()
    im_list = []
    for i in range (0,75):
        im_list.append(nparray[:][:][i])
    animation.ArtistAnimation(fig, im_list, interval=50)
    plt.show()
'''

if __name__ == '__main__':
    print "Starting"
    img2plt('/home/mohit/devel/python/mohit/python/data.csv')
