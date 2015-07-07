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

class CountData:  #エージェント数のカウント
    def __init__(self,agentData):
        for key in agentData.keys():
            print key,
        self.Type = Type
        self.SC = SC
        self.ST = ST
    def count(self):
        countData = {}
        agent = self.agentData
        for key in agent.keys():    #活動しているエージェント
            if agent.SC>0:
                countData[key] = agentData[key]
                if self.Type == 'non-strikenHuman':
                    countData['non-strikenHuman'] += 1
                    countData['all'] += 1
                    countData[0] += self.SC
                    countData[2] += self.SC
                elif self.Type == 'strikenHuman':
                    countData['strikenHuman'] += 1
                    countData['all'] += 1
                    countData[0] += self.SC
                    countData[2] += self.SC
        # activeCount = len(activeAgent)
        return countData

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
    "non-strikenHuman":100#,\
    # "strikenHuman":20\
    }   #エージェント数
    SocialConsumption = 10   #ステップごとのSC消費量
    TimeStep = 1000
    agentData = {}
    agentCount = 0
    for key in AgentNumber:    #クラス生成
        if key == 'non-strikenHuman':
            initialSC = 200
            ST = random.normalvariate(10,0.5)
        else:
            initialSC = 100
            ST = random.normalvariate(5,0.5)
        for num in range(AgentNumber[key]):
            agentCount += 1
            agentn = Agent(agentCount,key,initialSC,ST)
            agentData = agentn.agentData(num,num,agentData)

    """エージェントシミュレーション"""
    ActiveAgentNumber = []
    totalSocialCapital = []
    transactionAgents = len(agentData)
    for k in range(TimeStep):
        # totalCapital = 0
        activeAgent = {}
        totalCapital = {}
        activeCount = {}
        """活動エージェントのみ抽出"""
        countdata = CountData(agentData)
        countData = countdata.count
        for key in agentData.keys():    #活動しているエージェント
            if agentData[key]["SocialCapital"]>0:
                activeAgent[key] = agentData[key]
                # totalCapital += activeAgent[key]['SocialCapital']
                if activeAgent[key]['agentType'] == 'non-strikenHuman':
                    activeCount['non-strikenHuman'] += 1
                    activeCount[2] += 1
                    totalCapital[0] += activeAgent[key]['SocialCapital']
                    totalCapital[2] += activeAgent[key]['SocialCapital']
                else:
                    activeCount[1] += 1
                    activeCount[2] += 1
                    totalCapital[1] += activeAgent[key]['SocialCapital']
                    totalCapital[2] += activeAgent[key]['SocialCapital']
        # activeCount = len(activeAgent)

        """
        取引ルール
        　
        """
        for key in activeAgent.keys():
            transactionPartner = random.choice(activeAgent.items())
            st = -activeAgent[key]['SocialTransaction']\
            + activeAgent[transactionPartner[0]]['SocialTransaction']
            activeAgent[key]['SocialCapital'] += st #- SocialConsumption
            activeAgent[transactionPartner[0]]['SocialCapital'] += st #- SocialConsumption
        ActiveAgentNumber.append(activeCount)
        totalSocialCapital.append(totalCapital)

"""結果表示"""

"""活動エージェント数の推移"""
plt.figure("The number of active agents",figsize=(16,9))
plt.xlabel("Step")
plt.ylabel("The number of active agents")
plt.plot(range(TimeStep),ActiveAgentNumber)
plt.legend(('non-strikenHuman','strikenHuman','total'))
savefigaspdf("TheNumberOfActiveAgents")

"""総保有資源の推移"""
plt.figure("Total amount of social capital",figsize=(16,9))
plt.xlabel("Step")
plt.ylabel("Total amount of social capital")
plt.plot(range(TimeStep),totalSocialCapital)
plt.legend(('non-strikenHuman','strikenHuman','total'))
savefigaspdf("TotalAmountOfSocialCapital")

plt.show()
