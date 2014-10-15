import matplotlib.pyplot as plt
import numpy as np	
import sys
import csv    # it is a library for operating on csv files.
import os
import re
path = sys.argv[3]
fname = sys.argv[1]
iname = sys.argv[2]
imgname = iname+'.svg'
fullpath = os.path.join(path, imgname)
counta1 = 0
countb1 = 0
countc1 = 0
countd1 = 0
counte1 = 0
counta2 = 0
countb2 = 0
countc2 = 0
countd2 = 0
counte2 = 0
countf = 0
width = 0.10
N = 1
with open(fname, 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='\n')                    
    for row in lines:
        #print row[0]
        if (re.match(r'[A][(][9][5-9][)]',row[0]) or re.match(r'[A][(][0-9][0-9][0-9][)]',row[0])):
            counta1 += 1
        elif (re.match(r'[A][(][9][0-4][)]',row[0])):
            counta2 += 1
        elif(re.match(r'[B][(][8][5-9][)]',row[0])):
            countb1 += 1
        elif(re.match(r'[B][(][8][0-4][)]',row[0])):
            countb2 += 1
        elif(re.match(r'[C][(][7][5-9][)]',row[0])):
            countc1 += 1
        elif(re.match(r'[C][(][7][0-4][)]',row[0])):
            countc2 += 1
        elif(re.match(r'[D][(][6][5-9][)]',row[0])):
            countd1 += 1
        elif(re.match(r'[D][(][6][0-4][)]',row[0])):
            countd2 += 1
        elif(re.match(r'[E][(][5][5-9][)]',row[0])):
            counte1 += 1
        elif(re.match(r'[E][(][5][0-4][)]',row[0])):
            counte2 += 1
        elif(re.match(r'[F][(][0-9][0-9][)]',row[0]) or re.match(r'[F][(][0-9][)]',row[0])):
            countf += 1
y1 = (counta1)
y2 = (counta2)
y3 = (countb1)
y4 = (countb2)
y5 = (countc1)
y6 = (countc2)
y7 = (countd1)
y8 = (countd2)
y9 = (counte1)
y10 = (counte2)
y11 = (countf)
fig = plt.figure()
ax = fig.add_subplot(111)
ind = np.arange(N)
kwargs = {"hatch":'x'} 
rect1 = ax.bar(ind, y1, width, color='w', ecolor='k', **kwargs)
rect2 = ax.bar(ind+width, y2, width, color='w', ecolor='k', **kwargs)
rect3 = ax.bar(ind+width*2, y3, width, color='w', ecolor='k', **kwargs)
rect4 = ax.bar(ind+width*3, y4, width, color='w', ecolor='k', **kwargs)
rect5 = ax.bar(ind+width*4, y5, width, color='w', ecolor='k', **kwargs)
rect6 = ax.bar(ind+width*5, y6, width, color='w', ecolor='k', **kwargs)
rect7 = ax.bar(ind+width*6, y7, width, color='w', ecolor='k', **kwargs)
rect8 = ax.bar(ind+width*7, y8, width, color='w', ecolor='k', **kwargs)
rect9 = ax.bar(ind+width*8, y9, width, color='w', ecolor='k', **kwargs)
rect10 = ax.bar(ind+width*9, y10, width, color='w', ecolor='k', **kwargs)
rect11 = ax.bar(ind+width*10, y11, width, color='w', ecolor='k', **kwargs)
ax.set_xlabel('grading for "'+ iname + '"')
ax.set_ylabel('# urls for each rating')
ax.set_xticks([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05, 1.15])
ax.set_xticklabels( ('A+', 'A-', 'B+', 'B-', 'C+', 'C-', 'D+', 'D-', 'E+', 'E-', 'below 50') )
#ax.legend( (rect1[0], rect2[0], rect3[0], rect4[0], rect5[0], rect6[0]), ('90-100', '80-90', '70-80', '60-70', '50-60', 'below 50') )
#legend = plt.legend(loc='best', shadow=True)
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
autolabel(rect7)
autolabel(rect8)
autolabel(rect9)
autolabel(rect10)
autolabel(rect11)
fig.savefig(fullpath)
#plt.show()

