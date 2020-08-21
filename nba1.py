# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:21:17 2019

@author: George
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

table= [("Atlanta Hawks",	0.533,	8.4),
("Boston Celtics",	0.531,	17.3),
("Brooklyn Nets",	0.528,	-2.2),
("Charlotte Hornets",	0.321,	-8.4),
("Chicago Bulls",	0.353,	-12.1),
("Cleveland Cavaliers",	0.440,	-10.3),
("Dallas Mavericks",	0.485,	-0.8),
("Denver Nuggets",	0.649,	14.6),
("Detroit Pistons",	0.486,	0.7),
("Golden State Warriors",	0.600,	11.4),
("Houston Rockets",	0.588,	-11),
("Indiana Pacers",	0.625,	13.6),
("LA Clippers", 0.583,	17.3),
("Los Angeles Lakers",	0.486,	4.9),
("Memphis Grizzlies",	0.400,	-12.6),
("Miami Heat",	0.472,	-2.6),
("Milwaukee Bucks",	0.667,	6.7),
("Minnesota Timberwolves",	0.417,	-16.1),
("New Orleans Pelicans",	0.359,	-11.4),
("New York Knicks",	0.286,	-5),
("Oklahoma City Thunder",	0.459,	-1.5),
("Orlando Magic",	0.410,	-5.7),
("Philadelphia 76ers",	0.686,	-1.9),
("Phoenix Suns",	0.375,	-11),
("Portland Trail Blazers", 	0.548,	-2.5),
("Sacramento Kings",	0.571,	9.5),
("San Antonio Spurs",	0.600,	-4.5),
("Toronto Raptors",	0.633,	6.7),
("Utah Jazz",	0.483,	10.9),
("Washington Wizards",	0.375,	-0.3)]

table1=np.array(table)
winpct=table1[:,1]
winpct=winpct.astype(np.float)
netrtg=table1[:,2].astype(np.float)

#cor=np.corrcoef(winpct,netrtg)  file_000802 https://www.youtube.com/watch?v=dqKS7F5L_IU

def getImage(path,zoom=0.1):
    return OffsetImage(plt.imread(path),zoom=zoom)



plt.style.use('seaborn-whitegrid')

fig = plt.figure(figsize=(14,9),dpi=400)
ax = plt.gca()
plt.scatter(winpct,netrtg,marker='x')

plt.xlim(0.25,0.75)
plt.ylim(-20,20)

plt.xticks(np.arange(.25, .76, step=0.5),('0.250','0.750'))
plt.yticks(np.arange(-20, 21, step=40),('-20','+20'))

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.legend()            
plt.grid()
label = ax.set_xlabel('Win Percentage', fontsize = 16)
ax.xaxis.set_label_coords(.9999, .55)

label = ax.set_ylabel('Net Rating', fontsize = 16, rotation='0')
ax.yaxis.set_label_coords(.43, .985)

ax.tick_params(axis="y",direction="in", pad=-28, labelsize = 16)
ax.tick_params(axis="x", labelsize = 16)

plt.savefig('D:\sxolh\explicit.png')
