#this is my header file
import os

class ddict(dict):
    def __init__(self, **kwds):
        self.update(kwds)
        self.__dict__ = self

Dirs = ddict(drive_loc = None)

try:
    ntbpath
except:
    ntbpath = os.getcwd()

path1_GD = []
for i in ntbpath.split("\\"):
    path1_GD.append(i)
    if 'drive' in i.lower():
        break
path2_GD = ''
for i in path1_GD:
    path2_GD = path2_GD + i + '//'
Dirs.drive_loc = os.path.abspath(path2_GD)
Dirs.current = os.getcwd()

del path1_GD
del path2_GD
del ntbpath
del i

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime

google_colors = ['#a93329', '#d94234', '#ffd200', '#e3b73c', '#0ca55f', '#0c9458', '#378fdd', '#2154ac']


# Plotly tokens - https://www.mapbox.com/
plotly_token1 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2sxbnAxa210MGNudDNtczBvcWp5M3NjZCJ9.V62gASFJHH68i3bfxiCHEw"
# plotly_token2 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2pueXI3b255MDRiZDNqbWI0ZnVkeXowMiJ9.3YrwQ2KJMqI16PcRbsfQDw"
# plotly_token3 = "pk.eyJ1IjoidGFua3giLCJhIjoiY2pueXI5MWt0MDFkYzN2dDdtYm1vY2k2bSJ9.xtopABkqm1EZPPeMIB8CrA"


# Some matplotlib settings
plt.style.use('seaborn-white')
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['axes.grid'] = True
# plt.rcParams['legend.handlelength'] = 12

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 300)