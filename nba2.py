# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:54:39 2019

@author: George
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

df=pd.read_excel(r"C:\Users\George\Desktop\trials.xls")
dfa=df.values

index=np.asarray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
xticks=['Embiid','Nurkic','Lopez','Horford','Gobert','Vucevic','Jokic',\
        'Turner','Davis','Drummond','Gasol(MEM)','Ibaka','Capela','Aldidge',\
        'Ayton','Adams','KAT','Cousins']





plt.style.use('seaborn-whitegrid')
fig = plt.figure(figsize=(9,6),dpi=400)
ax = plt.gca()
plt.scatter(dfa[:,0],index,marker='x')
plt.scatter(dfa[:,3],index,marker='o')
# =============================================================================
# plt.xlim(0.25,0.75)
# plt.ylim(-20,20)
# 
# plt.xticks(np.arange(.25, .76, step=0.5),('0.250','0.750'))
# plt.yticks(np.arange(-20, 21, step=40),('-20','+20'))
# 
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('center')
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# 
# =============================================================================
#plt.legend()            
#plt.grid()
# =============================================================================
# label = ax.set_xlabel('Win Percentage', fontsize = 16)
# ax.xaxis.set_label_coords(.9999, .55)
# 
# label = ax.set_ylabel('Net Rating', fontsize = 16, rotation='0')
# ax.yaxis.set_label_coords(.43, .985)
# 
# ax.tick_params(axis="y",direction="in", pad=-28, labelsize = 16)
# ax.tick_params(axis="x", labelsize = 16)
# 
# =============================================================================
plt.savefig('D:\sxolh\explicit.png')
