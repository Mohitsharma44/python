import time
import numpy
import matplotlib.pyplot as plt
from numpy import genfromtxt
from matplotlib import pyplot as plt
import numpy as np
import PIL
import matplotlib.animation as animation
from pylab import *

fig = plt.figure( 1 )
ax = fig.add_subplot( 111 )
ax.set_title("My Title")

im = ax.imshow( numpy.zeros( ( 240, 320) ) )# Blank starting image
fig.show()
im.axes.figure.canvas.draw()

tstart = time.time()
for a in xrange( 100 ):
  print "Rendering Frame %s"%a
  data = numpy.random.random( ( 240, 320) ) # Random image to display
  ax.set_title( str( a ) )
  im.set_data( data )
  im.axes.figure.canvas.draw()

print ( 'FPS:', 100 / ( time.time() - tstart ) )
