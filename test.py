#!/usr/bin/env python
# -*- coding: utf-8 -*-
# インポート
import os
import random
import datetime
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import math
import wx

# クラス定義
class Agent:    #エージェントクラス
    def __init__(self,Number,Type,SC,ST):
        self.Number = Number
        self.Type = Type
        self.SC = SC
        self.ST = ST
    def location(self,x,y):
        locationData = {}
        locationData['agentNumber'] = self.Number
        locationData['locationX'] = x
        locationData['locationY'] = y
        return locationData
    def newSC(self,ST):
        self.SC = self.SC + ST
        if self.SC<0:
            self.SC = 0

class SeismicLoss:
    def __init__(self,agent,loss):
        self.agent = agent
        self.loss = loss
    def lossCalc(self):
        return loss

# 関数定義
def savefigaspdf(name):
    date = datetime.date.today()
    if os.path.exists("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s"% (date.year, date.month, date.day))==False:
        os.mkdir("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s"\
        % (date.year, date.month, date.day))
    plt.savefig("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s/%s.pdf"\
    % (date.year, date.month, date.day, name))
    plt.close


if __name__ == "__main__":
    a = Agent(1,"human",200,random.randint(0,10))
    locationData = a.location(1,10)
    print locationData
