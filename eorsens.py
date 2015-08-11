import numpy as np
import matplotlib.pyplot as plt

sens = """PAPER 128  &  1.56  &  -  &  4.46  &  - 
MWA 128      &  0.66  & 0.86  &  2.50  &  3.15 
LOFAR (core) & 0.70  & 1.90  & 7.48  &  12.22 
HERA 37         & 5.67  &  -  & 15.46   &  - 
HERA 331       & 38.75 & -  &  111.69  &  - 
MWA 256         &2.40   &  2.81  &  8.28  & 9.64 
SKA1 Low      &21.23   & 26.92  & 139.07  & 115.13"""

sens = sens.split('\n')
arrnames = []
arrsens = []
for line in sens:
    data=line.split('&')
    arrnames.append(data[0].strip())
    del(data[0])
    varr = []
    for v in data:
        if v.strip()=='-':
            varr.append(0.0)
        else:
            varr.append(float(v))
    arrsens.append(varr)
arrsens = np.array(arrsens)
print arrnames
print arrsens

gridlines = [0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0]
gridlines = [1.0,10.0,100.0]
for g in gridlines:
    plt.plot([-1.5,13.5],[g,g],'k:')

w = 0.4
c = ['b','c','m','r']
labels = ['Avoid(drift)','Subtract(drift)','Avoid(track)','Subtract(track)']
cols = [0,2,1,3]
ll = np.arange(len(arrsens[:,0]))*2-0.5+w/2.0
for i in range(len(cols)):
    plt.bar(ll+i*w*1.05,arrsens[:,cols[i]],color=c[i],width=w,label=labels[i])
plt.yscale('log')
plt.axis([-1.5,13.5,0.5,140.0])
plt.legend(loc='upper left')
xt = [0,2,4,6,8,10,12]
plt.xticks(xt,arrnames,rotation=70)
plt.plot([5.55,5.55],[0.5,140],'k',linewidth=3)


