import numpy as np
import itertools as it
import glob

#データの読み込み
data = glob.glob('t=0.txt',skiprows=2) #'t=0.txt'を上２行をすっ飛ばして読む
print (data)
print("Hello")