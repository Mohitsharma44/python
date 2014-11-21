from numpy import genfromtxt
from matplotlib import pyplot as plt
import numpy as np
import PIL
import matplotlib.animation as animation
import pylab as pl
import time

def csv2np():
    pl.ion()
    pl.show()
    nparray = np.zeros((240,320,frames))
    z = np.zeros((240,320))
    i=j=count = 0
    k = -1
    for j in range (0,cols):
        count = count + 1  #Go upto 240 columns, 
        if (j%240 == 0):
            count = 0      #and reset again
            k = k + 1      #Increment dimension
            print "Columns Done: %s"%j
            print "Frames Done:  %s"%k
            pl.imshow(z, cmap=pl.cm.rainbow, 
                       vmin = min_temp, vmax=max_temp)
            pl.colorbar()
            pl.draw()
            time.sleep(0.005)
            pl.clf()
        for i in range (0,320):
            nparray[count][i][k] = csvfile[j][i]
            z[count][i] = nparray[count][i][k]
    return nparray


def np2img():
    i=j=0
    nparray = csv2np()
    print "Processing Frame 0"
    z = np.zeros((240,320))
    pl.ion()
    pl.show()
    for k in range (0,frames):
        pl.imshow(z, cmap=pl.cm.Accent, vmin=z.min(), vmax=z.max())
        pl.colorbar()
        pl.draw()
        time.sleep(0.05)
        pl.clf()
        for i in range (0,240):
            for j in range(0,320):
                z[j][i]=nparray[j][i][k]
                
            
    return z

def img2plt():
    z = np.zeros((240,320))
    z = np2img()
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
    csvfile = genfromtxt('/home/mohit/devel/python/mohit/python/IR/data.csv',delimiter=',')
    max_temp = csvfile.max()
    min_temp = csvfile.min()
    cols = csvfile.shape[0]
    frames = cols/240
    csv2np()
