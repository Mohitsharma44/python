from numpy import genfromtxt
from matplotlib import pyplot as plt
from matplotlib import gridspec
import numpy as np
import PIL
import matplotlib.animation as animation
import pylab as pl
import time

#------------------------
# Software to process IR Files (.csv)
#
# 2014/11/23 - Written by Mohit Sharma (CUSP/ NYU)
#------------------------

def csv2np():
    pl.ion() #for interactive
    pl.show()
    nparray = np.zeros((240,320,frames))
    z = np.zeros((240,320))
    i=j=count = 0
    k = -1
    fig,(ax1,ax2) = pl.subplots(1,2, figsize = (50,25), dpi = 90)
    fig.suptitle('IR Playback', fontsize=20)
    gs = gridspec.GridSpec(1,2, width_ratios=[3,2])

    #-- Show Video
    ax2 = pl.subplot(gs[0])
    ax2.set_title('Video')
    im = ax2.imshow(z, cmap=pl.cm.gray,
                   vmin = 5, vmax=max_temp,
                   aspect='auto')
    fig.colorbar(im, orientation='vertical')
    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)

    #-- Show Histogram
    ax1 = pl.subplot(gs[1])
    ax1.set_title('Histogram')
    ax1.set_xlabel('Temperature C')
    ax1.set_ylabel('Frequency')
    a,edges = np.histogram(z,bins=1000)
    b = 0.5*(edges[1:]+edges[:-1])
    li, = ax1.plot(b,a,'r-')
    ax1.set_ylim(0,1)
    ax1.set_xlim(5,40)
    ax1.xaxis.grid(True)
    ax1.yaxis.grid(True)
    ax1.locator_params(nbins=15, axis='y')
    #-- Adjust Layout
    pl.subplots_adjust(top=1.5)
    pl.tight_layout()

    #-- Create Data Cube for further processing
    for j in range (0,cols):
        count = count + 1  #Go upto 240 columns, 
        if (j%240 == 0):
            count = 0      #and reset again
            k = k + 1      #Increment dimension
            print "Frames Done:  %s"%k
            a,edges = np.histogram(z,bins=500, normed=True)
            b = 0.5*(edges[1:]+edges[:-1])
            li.set_xdata(b) # ! to set X value, pass it
            li.set_ydata(a) # as Y value and vice-versa

            im.set_data(z)
            im.set_clim(vmin = 0) #change min temperature value
            fig.canvas.draw()

        nparray[count,:,k] = csvfile[j,:]
        z[count,:] = nparray[count,:,k]
    return nparray

def iter_loadtxt(filename, delimiter=',', skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for i in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data


if __name__ == '__main__':
    
    print "Reading CSV file.."
    csvfile = iter_loadtxt('data.csv')
    max_temp = csvfile.max()
    min_temp = csvfile.min()
    cols = csvfile.shape[0]
    frames = cols/240
    csv2np()
