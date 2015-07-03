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
    def newSC(self,ST):
        self.SC = self.SC + ST
        if self.SC<0:
            self.SC = 0

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
    AgentNumber = 100   #エージェント数
    InitialCapital = 200
    TimeStep = 500
    agentlist = []      #エージェントリスト
    for n in range(AgentNumber):    #クラス生成
        agentlist.append(Agent(n,"human",InitialCapital,\
        random.uniform(0,5)))
    """エージェントシミュレーション"""
    N = range(AgentNumber)
    ActiveAgentNumber = []
    TotalSocialCapital = []
    """取引相手の選択"""
    for k in range(TimeStep):
        transactionagents = N
        random.shuffle(transactionagents)
        activeagentlist = []
        activeagentcapital = []

        """活動エージェントのみ抽出"""
        for n in range(AgentNumber):
            if agentlist[transactionagents[n]].SC>0:
                activeagentlist.append(transactionagents[n])
                activeagentcapital.append(agentlist[transactionagents[n]].SC)
        totalcapital = sum(activeagentcapital)
        activecount = np.size(activeagentlist)

        """取引"""
        for n in range(activecount/2):
            """エージェントの活動条件：保有資源＞０"""
            if agentlist[activeagentlist[2*n-1]].SC > 0\
            and agentlist[activeagentlist[2*n]].SC > 0:
                st = -agentlist[activeagentlist[2*n-1]].ST\
                + agentlist[activeagentlist[2*n]].ST
                agentlist[activeagentlist[2*n-1]].newSC(st)
                agentlist[activeagentlist[2*n]].newSC(-st)
                # totalcapital = agentlist[activeagentlist[2*n-1]].SC + \
                # agentlist[activeagentlist[2*n]].SC
        ActiveAgentNumber.append(activecount)
        TotalSocialCapital.append(totalcapital)
    """活動エージェント数の推移"""
    plt.figure("The number of active agents",figsize=(16,9))
    plt.xlabel("Step")
    plt.ylabel("The number of active agents")
    plt.plot(range(TimeStep),ActiveAgentNumber)
    savefigaspdf("TheNumberOfActiveAgents")

    """総保有資源の推移"""
    plt.figure("Total amount of social capital",figsize=(16,9))
    plt.xlabel("Step")
    plt.ylabel("Total amount of social capital")
    plt.ylim([19000,21000])
    plt.plot(range(TimeStep),TotalSocialCapital)
    savefigaspdf("TotalAmountOfSocialCapital")

    plt.show()
