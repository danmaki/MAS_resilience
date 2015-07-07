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
    def agentData(self,x,y,agentData={}):
        key = 'Agent'+str(self.Number)
        agentData[key] = {\
        'Number':self.Number,\
        'agentType':self.Type,\
        'SocialCapital':self.SC,\
        'SocialTransaction':self.ST,\
        'locationX':x,'locationY':y\
        }
        return agentData

class Count:  #エージェント数のカウント
    def __init__(self,agentData,timeStep):
        self.countData = {'TimeStep':timeStep,\
        'activeAgent':{'non-strikenHuman':0,'strikenHuman':0},\
        'totalCapital':{'non-strikenHuman':0,'strikenHuman':0}\
        }
        for key in agentData.keys():
            agentType = agentData[key]['agentType']
            agentCapital = agentData[key]['SocialCapital']
            self.countData['activeAgent'][agentType] += 1
            self.countData['totalCapital'][agentType] += agentCapital
        self.timeStep = timeStep
    def getData(self,data):
        data = self.countData
        return data

class SeismicLoss:
    def __init__(self,agent,loss):
        self.agent = agent
        self.loss = loss
    def lossCalc(self):
        return loss

class Transaction:
    def __init__(self,transactionAgents):
        self.transactionAgents = transactionAgents

# 関数定義
def savefigaspdf(name):
    date = datetime.date.today()
    if os.path.exists("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s"% (date.year, date.month, date.day))==False:
        os.mkdir("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s"\
        % (date.year, date.month, date.day))
    plt.savefig("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s-%s-%s/%s.pdf"\
    % (date.year, date.month, date.day, name))
    plt.close

# メインループ
if __name__ == "__main__":
    """エージェント定義"""
    AgentNumber = {\
    "Human":100
    }
    TimeStep = 1000
    agentData = {}
    agentCount = 0
    for key in AgentNumber:    #クラス生成
        if key == 'Human':
            initialSC = 200
            ST = 1
        if key == 'Enterprise':
            initialSC = 2000
            ST = 10
        for n in range(AgentNumber[key]):
            agentCount += 1
            agentn = Agent(agentCount,key,initialSC,ST)
            agentData = agentn.agentData(random.random(),random.random(),agentData)
    """エージェントシミュレーション"""
    countData = []
    for k in range(TimeStep):
        if k == 100:
            for key in agentData.keys():
                if agentData[key]['locationX'] and agentData[key]['locationY'] > 0.5:
                    agentData[key]['SocialCapital'] -= 100
        activeAgent = {}
        """活動エージェントのみ抽出"""
        for key in agentData.keys():    #活動しているエージェント
            """エージェントタイプの判別・変更"""
            if agentData[key]["SocialCapital"]>180: #非被災条件 SC > 0.8*initialSC
                agentData[key]['agentType'] = 'non-strikenHuman'
            else:
                agentData[key]['agentType'] = 'strikenHuman'
            if agentData[key]["SocialCapital"]>0:
                    activeAgent[key] = agentData[key]
        countDatan = Count(activeAgent,k)
        countData.append(countDatan.getData(countData))
        """
        取引ルール
        """
        for key in activeAgent.keys():
            if activeAgent[key]['agentType'] == 'non-strikenHuman':
                sc = random.uniform(1.5,2.5)   #ステップごとのSC消費量
            elif activeAgent[key]['agentType'] == 'strikenHuman':
                sc = random.uniform(0.5,1.5)   #ステップごとのSC消費量
            transactionPartner = random.choice(activeAgent.items())
            st = activeAgent[key]['SocialTransaction']\
            + activeAgent[transactionPartner[0]]['SocialTransaction']
            activeAgent[key]['SocialCapital'] += st - sc
            activeAgent[transactionPartner[0]]['SocialCapital'] += st - sc

    """結果計算"""
    figX = []
    figYTotalSC = []
    figYActiveagent = []
    for key in range(len(countData)):
        figX.append(countData[key]['TimeStep'])
        figYActiveagent.append([\
        countData[key]['activeAgent']['non-strikenHuman'],\
        countData[key]['activeAgent']['strikenHuman'],\
        sum(countData[key]['activeAgent'].values())\
        ])
        figYTotalSC.append([\
        countData[key]['totalCapital']['non-strikenHuman'],\
        countData[key]['totalCapital']['strikenHuman'],\
        sum(countData[key]['totalCapital'].values())\
        ])

"""活動エージェント数の推移"""
plt.figure("The number of active agents",figsize=(16,9))
plt.xlabel("Step")
plt.ylabel("The number of active agents")
plt.plot(figX,figYActiveagent)
plt.legend(('non-strikenHuman','strikenHuman','total'))
savefigaspdf("TheNumberOfActiveAgents")

"""総保有資源の推移"""
plt.figure("Total amount of social capital",figsize=(16,9))
plt.xlabel("Step")
plt.ylabel("Total amount of social capital")
plt.plot(figX,figYTotalSC)
plt.legend(('non-strikenHuman','strikenHuman','total'))
savefigaspdf("TotalAmountOfSocialCapital")

plt.show()
