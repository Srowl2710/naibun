import numpy as np
import itertools as it

#データの読み込み
data = np.loadtxt('t=0の時の２点内分.txt',skiprows=0) #'t=0.txt'を上２行をすっ飛ばして読む


#データの仕分け
num = np.shape(data)[0] #データの縦列数
freq_num=np.shape(data)[1]
dataR=np.empty((55,31))
dataI=np.empty((55,31))
n=0
m=0
for i in range(freq_num):
    for j in range(num):
        if (j%2==1):
            dataR[n,:]=data[i,:]
            n = n+1
        else:
            dataI[m,:]=data[i,:]
            m = m+1

print(dataR)