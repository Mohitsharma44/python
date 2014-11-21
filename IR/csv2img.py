from numpy import genfromtxt
from matplotlib import pyplot as plt
import numpy as np
import PIL
import matplotlib.animation as animation
import pylab as pl
import time

def csv2np():
    pl.ion()
    #pl.show()
    nparray = np.zeros((240,320,frames))
    z = np.zeros((240,320))
    test = np.zeros((240,320,frames))
    test = csvfile.reshape((240,320,frames))
    i=j=count = 0
    k = -1
    fig,ax = pl.subplots(num = 0, figsize = (10,5), dpi = 150)
    fig.subplots_adjust(0,0,1,1)
    im = ax.imshow(z, cmap=pl.cm.rainbow,                                                                                                                                                                        
                   vmin = min_temp, vmax=max_temp,
                   aspect='auto')
    fig.colorbar(im, orientation='vertical')
    ax.axis = ('off')
    #fig.canvas.draw()
    for j in range (0,cols):
        count = count + 1  #Go upto 240 columns, 
        if (j%240 == 0):
            count = 0      #and reset again
            k = k + 1      #Increment dimension
            print "Columns Done: %s"%j
            print "Frames Done:  %s"%k
            
            #print test[count][j][k]==nparray[count][j][k]
            
            #pl.imshow(z, cmap=pl.cm.rainbow, 
            #           vmin = min_temp, vmax=max_temp,
            #          aspect='auto')
            #pl.colorbar()
            #pl.draw()
            #time.sleep(0.005)
            #pl.clf()
            im.set_data(z)
            fig.canvas.draw()
            #fig.show()
        #for i in range (0,320):
        nparray[count,:,k] = csvfile[j,:]
        z[count,:] = nparray[count,:,k]
    
    
    '''
    for k in range (0,frames):
        z=nparray[:,:,k]
        print z.shape
        pl.imshow(z, cmap=pl.cm.rainbow,
                  vmin = min_temp, vmax = max_temp)
        pl.colorbar()
        pl.draw()
        time.sleep(0.005)
        pl.clf()
    '''
    return nparray


def np2img():
    i=j=0
    nparray = csv2np()
    print "Processing Frame 0"
    z = np.zeros((240,320))
    pl.ion()
    pl.show()
    for k in range (0,frames):
        pl.imshow(z, cmap=pl.cm.Accent, 
                  vmin=z.min(), vmax=z.max(),
                  aspect='auto')
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
    csvfile = genfromtxt('/home/mohitsharma44/devel/python/IR/data.csv',delimiter=',')
    max_temp = csvfile.max()
    min_temp = csvfile.min()
    cols = csvfile.shape[0]
    frames = cols/240
    csv2np()
