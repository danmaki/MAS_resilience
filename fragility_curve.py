#!/usr/bin/env python
# -*- coding: utf-8 -*-
# インポート
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import math
import wx

# クラス定義
class plotfig:  #プロット
    def __init__(self,x,y):
        self.title = u"図"
        self.xlabel = u"x軸タイトル"
        self.ylabel = u"y軸タイトル"
    def setproperty(self,title,xlabel,ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
    def display(self):
        plt.figure(self.title)
        plt.grid()
        plt.plot(x,y)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

# 関数定義
def logncdf(x,mu,sigma):    #対数正規累積確率分布関数
    if x<0:
        cdf  = 0.
    elif sp.isposinf(x):
        cdf  = 1.
    else:
        z    = (sp.log(x)-mu)/float(sigma)
        cdf  = .5*(math.erfc(-z/sp.sqrt(2)))
    return cdf

def fragility(X,mu,sigma):  #フラジリティ曲線
    x = np.arange(0,X,0.01)
    y = np.zeros(np.size(x))
    for n in range(np.size(x)):
        y[n] = logncdf(x[n],mu,sigma)
    return x, y

# メインループ
if __name__ == "__main__":
    # フラジリティカーブ
    x, y = fragility(2,0,0.1)
    plot1 = plotfig(x,y)
    plot1.setproperty(u"フラジリティ曲線",u"地動加速度 [m/s^2]",u"非超過確率")
    plot1.display()
