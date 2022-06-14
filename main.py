import numpy as np
import itertools as it

#データの読み込み
data = np.loadtxt('t=0.txt',skiprows=2) #'t=0.txt'を上２行をすっ飛ばして読む


#データの仕分け
freq_num = np.shape(data)[0] #周波数の数　データの縦列数 
dataR = np.array(data[:,[1,3,5,7]]).T #実部データ　データの縦列2,4,6,8行目の抽出
dataI = np.array(data[:,[2,4,6,8]]).T #虚部データ

#組み合わせ導出
numlist = [0,1,2,3] #データの数(電池の数)
c2list = list(it.combinations(numlist,2)) #内分２つ 'c2list' means...-> combination 2 list


#内分計算関数
def calc_divide(ratio: tuple, data: tuple):
        # ratio:(m,n),data:(A,B)
        r, s = ratio
        A, B = data
        return (r * A + s * B) / (r + s)

#計算(2つの場合)
f2data = np.empty((0,31)) #縦列なし横列31ある空箱を用意する
for i,j in c2list:
    for r in range(1,10): # r -> ratio 比率 1:9,2:8, ... , 8:2,9:1 の９通り
        s = 10-r
        f2dataR = calc_divide(                     #実部
            (r, s), (dataR[i], dataR[j])
        )
        f2dataI = calc_divide(                     #虚部
            (r, s), (dataI[i], dataI[j])
        )
        add = np.array([f2dataR,f2dataI])
        f2data = np.vstack((f2data,add))           #addとf2dataは横列が同じでなければならない(上で箱の大きさを設定しておく必要がある)
np.savetxt('t=0の時の２点内分.txt',f2data,delimiter="	") #書き出し