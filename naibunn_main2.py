import numpy as np

#データの読み込み
data = np.loadtxt('t=35の時の２点内分.txt',skiprows=0) #'t=0.txt'を上２行をすっ飛ばして読む


#データの仕分け
freq = np.array([5000,3406.5,2320.8,1581.1,1077.2,733.9,500,340.65,232.08,158.11,107.72,73.39,50,34.065,23.208,15.811,10.772,7.339,5,3.406,2.321,1.581,1.077,0.734,0.5,0.341,0.232,0.158,0.108,0.073,0.05])
freq_num=np.shape(data)[1]
dataR=np.array(data[0::2,:]).T #0行目から2列おきにとる
dataI=np.array(data[1::2,:]).T

datan = np.empty(5022).reshape(54,93)
for i in range(freq_num):
    datan[:,3*i]=freq[i]
    datan[:,3*i+1]=dataR[i]
    datan[:,3*i+2]=dataI[i]

np.savetxt('t=35の時の２点内分改.txt',datan,delimiter="	")