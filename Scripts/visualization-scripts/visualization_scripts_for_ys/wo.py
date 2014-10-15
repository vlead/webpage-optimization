import matplotlib.pyplot as plt
import numpy as np	
import sys
import csv    # it is a library for operating on csv files.
import os
import re
path = sys.argv[3]
fname = sys.argv[1]
iname = sys.argv[2]
imgname = iname+'.jpg'
fullpath = os.path.join(path, imgname)
counta = 0
countb = 0
countc = 0
countd = 0
counte = 0
countf = 0
width = 0.10
N = 1
with open(fname, 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='\n')                    
    for row in lines:
        #print row[0]
        if (re.match(r'[A][(][0-9][0-9][)]',row[0]) or re.match(r'[A][(][0-9][0-9][0-9][)]',row[0])):
            counta += 1
        elif(re.match(r'[B][(][0-9][0-9][)]',row[0])):
            countb += 1
        elif(re.match(r'[C][(][0-9][0-9][)]',row[0])):
            countc += 1
        elif(re.match(r'[D][(][0-9][0-9][)]',row[0])):
            countd += 1
        elif(re.match(r'[E][(][0-9][0-9][)]',row[0])):
            counte += 1
        elif(re.match(r'[F][(][0-9][0-9][)]',row[0]) or re.match(r'[F][(][0-9][)]',row[0])):
            countf += 1
#print counta
#print countb
#print countc
#print countd
#print counte
#print countf
y1 = (counta)
y2 = (countb)
y3 = (countc)
y4 = (countd)
y5 = (counte)
y6 = (countf)
fig = plt.figure()
ax = fig.add_subplot(111)
ind = np.arange(N)
rect1 = ax.bar(ind, y1, width, color='r', label ='90-100')
rect2 = ax.bar(ind+width, y2, width, color='b', label ='80-90')
rect3 = ax.bar(ind+width*2, y3, width, color='c', label ='70-80')
rect4 = ax.bar(ind+width*3, y4, width, color='y', label ='60-70')
rect5 = ax.bar(ind+width*4, y5, width, color='g', label ='50-60')
rect6 = ax.bar(ind+width*5, y6, width, color='m', label ='< 50')
ax.set_xlabel('grading for "'+ iname + '"')
ax.set_ylabel('number of urls in a grade')
ax.set_xticks([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65])
ax.set_xticklabels( ('90-100 (A)', '80-90 (B)', '70-80 (C)', '60-70 (D)', '50-60 (E)', 'below 50') )
#ax.legend( (rect1[0], rect2[0], rect3[0], rect4[0], rect5[0], rect6[0]), ('90-100', '80-90', '70-80', '60-70', '50-60', 'below 50') )
legend = plt.legend(loc='best', shadow=True)
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.00*height, '%d'%int(height), ha='center', va='bottom')

autolabel(rect1)
autolabel(rect2)
autolabel(rect3)
autolabel(rect4)
autolabel(rect5)
autolabel(rect6)
fig.savefig(fullpath)
#plt.show()

