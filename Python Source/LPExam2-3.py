
# coding: utf-8

#get_ipython().magic(u'matplotlib inline')
import pylab as pl
#pylab is both pyplot and matplotlib
#import matplotlib as mpl
#import matplotlib.pyplot as pp

#pl.xkcd()
fig = pl.figure()
ax = fig.add_subplot(111)

red = pl.empty((2))
blue = pl.empty((2))


# material used in scenario i <= material A available in scenario i, i={1,2,3}
#(1) * red + (2)*blue <=  150 #1
#(4) * red + (3)*blue <=  200 #2
#(3) * red + (2)*blue <=  200 #3
# 2  * red +  2 *blue <= 100  #4

#limitA1
red[0] = 0
blue[0] = 150/2
red[1] =  150/1
blue[1] = 0
pl.plot(red, blue, '-', c='g', label="A-limit Scenario 1")

#limitA2
red[0] = 0
blue[0] = 200/3
red[1] =  200/4
blue[1] = 0
pl.plot(red, blue, '-', c='b', label="A-limit Scenario 2")

#limitA3
red[0] = 0
blue[0] = 200/2
red[1] =  200/3
blue[1] = 0
pl.plot(red, blue, '-', c='y', label="A-limit Scenario 3")

#2 * red +2 *blue <= 100 (LimitB)
red[0] = 0
blue[0] = 50
red[1] =  50
blue[1] = 0
pl.plot(red, blue, '-', c='m', label="B-limit All Scenarios")

pl.xlabel("Product Red")
pl.ylabel("Product Blue")

pl.plot(50,1,'o',c='r', ms=5)  #yes- its offset slightly
                               #real optimal is (50,0) 
pl.annotate('optimal point', xy=(52.5,5), xytext=(60,25),
            arrowprops=dict(facecolor='red', shrink=.05),)

c_red = .3*2000 + .2*4000 + .5*4000
c_blue = .3*3000 + .2*4000 + .5*3000


red[0]=0
blue[0]= 50000/c_blue
red[1]= 50000/c_red
blue[1]=0
pl.plot(red, blue, ':', c='r', label="z=$50k")
red[0]=0
blue[0]= 100000/c_blue
red[1]= 100000/c_red
blue[1]=0
pl.plot(red, blue, '--', c='r', label="z=$100k")
red[0]=0
blue[0]= 170000/c_blue
red[1]= 170000/c_red
blue[1]=0
pl.plot(red, blue, '-', c='r', label="z=$170k(Optimal)")
pl.ylim(0,100)
pl.xlim(0,100)
pl.legend(prop={'size':8})
pl.title("Problem 2")
pl.fill([0,50,0,0],[0,0,50,0],'black', alpha=.2)
	pl.annotate('feasible region', xy=(10,10))
pl.savefig('Problem2.png', bbox_inches='tight')
pl.show()





