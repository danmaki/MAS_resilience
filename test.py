#!/usr/bin/env python
# -*- coding: utf-8 -*-
# インポート
import random
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import math
import wx

if __name__ == "__main__":
    marks = ['club', 'diamond', 'heart', 'spade']
    numbers = range(1, 14)
    cards = [(m, n) for m in marks for n in numbers]
    print cards
