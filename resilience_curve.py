#!/usr/bin/env python
# -*- coding: utf-8 -*-
# インポート
import os
import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname="/Library/Fonts/Microsoft/MS Gothic.ttf")

if __name__ == "__main__":
    L0 = 0.5
    omega = 0.03
    t = np.arange(0,1000,1)
    EC = 1 - L0*np.exp(-omega*t)*(1+omega*t)
    SC = 1 - L0*np.exp(-0.3*omega*t)*(1+0.3*omega*t)
    plt.figure(figsize=(16,9))
    plt.plot([-100,0,0],[1,1,0.5],"b-")
    plt.plot(t, EC,"b-",label="Economic Capital")
    plt.plot(t, SC,"g-",label="Social Capital")
    plt.tick_params(labelsize=21)
    plt.xlabel(u"経過日数",fontsize=24,fontproperties=fp)
    plt.ylabel(u"平常時に対する資本割合",fontsize=24,fontproperties=fp)
    plt.xlim([-100,1000])
    plt.ylim([0,1.1])
    plt.grid()
    plt.legend(fontsize=21,loc="lower right")
    # plt.show()
    date = datetime.date.today()
    if os.path.exists("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s%s%s"% (date.year, date.month, date.day))==False:
        os.mkdir("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s%s%s"\
        % (date.year, date.month, date.day))
    plt.savefig("/Users/danmaki/GoogleDrive/Program/figures/resilience/%s%s%s/resilience_curve.pdf"\
    % (date.year, date.month, date.day))
    plt.close
