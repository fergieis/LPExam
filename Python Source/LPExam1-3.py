
# coding: utf-8



#get_ipython().magic(u'matplotlib inline')
import pylab as pl
#import matplotlib as mpl
#import matplotlib.pyplot as pp

#pl.xkcd()
fig = pl.figure()
ax = fig.add_subplot(111)

red = pl.empty((2))
blue = pl.empty((2))

b_A = .3*150 + .2*200 + .5*200
b_B = .3*200 + .2*180 + .5*100

#(.3*1+.2*4+.5*3) * red + (.3*2+.2*3+.5*2)*blue <= b_A
red[0] = 0
blue[0] = b_A/(.3*2+.2*3+.5*2)
red[1] =  b_A/(.3*1+.2*4+.5*3)
blue[1] = 0
pl.plot(red, blue, '-', c='g', label="A-limit")


#2 * red +2 *blue <= b_B
red[0] = 0
blue[0] = b_B/2
red[1] =  b_B/2
blue[1] = 0
pl.plot(red, blue, '-', c='m', label="B-limit")

pl.xlabel("Product Red")
pl.ylabel("Product Blue")

pl.plot(71,.5,'o',c='r', ms=5)
#real optimal is at (71.1538461538,0)
# but doesn't plot as well
pl.annotate('optimal point\n(71.15...,0)', xy=(71,5), xytext=(45,50),
            arrowprops=dict(facecolor='red', shrink=.05),)
pl.legend()

#close enough...
pl.fill([0,71,62,0],[0,0,11,73],"black", alpha=.2)
pl.annotate('feasible region', xy=(10,10))
pl.title("Problem 1")
pl.savefig('Problem1a.png', bbox_inches='tight')
pl.show()


#----------------------------------------
#     Now slightly zoomed in
#----------------------------------------

red[0] = 0
blue[0] = b_A/(.3*2+.2*3+.5*2)
red[1] =  b_A/(.3*1+.2*4+.5*3)
blue[1] = 0
pl.plot(red, blue, '-', c='g',label="A-limit")


#2 * red +2 *blue <= b_B
red[0] = 0
blue[0] = b_B/2
red[1] =  b_B/2
blue[1] = 0
pl.plot(red, blue, '-', c='m', label="B-limit")

pl.xlabel("Product Red")
pl.ylabel("Product Blue")

pl.plot(71.1,0.2,'o',c='r', ms=5)
pl.fill([0,71,62,0],[0,0,11,73],"black", alpha=.2)
pl.annotate('optimal point\n(71.15...,0)', xy=(71.1,.5), xytext=(70,10),
            arrowprops=dict(facecolor='red', shrink=.05),)
pl.annotate('feasible region', xy=(62,2.5))
pl.legend()
pl.title("Problem 1-Zoom")
pl.xlim(60, 80)
pl.ylim(0, 20)
pl.savefig('Problem1b.png', bbox_inches='tight')

