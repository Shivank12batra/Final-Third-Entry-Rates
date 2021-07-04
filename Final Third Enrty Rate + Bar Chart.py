#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('LaLigaPass.csv')


# In[6]:


def deep_completions_percentage(df1, team_id):
    df2 = df1[df1['team_id'] == team_id]
    df2 = df2.reset_index()
    n = 0
    completions = 0
    total = 0
    on = True
    while on:
        on = False
        for i in range(n, len(df2['x'])):
            if n > len(df2['x']):
                break
            if (df2['endX'][i] < 6) and (df2['endY'][i] > 30) and (df2['endY'][i] < 50):
                n = i + 2
                on = True
                break
            if (df2['x'][i] < 6) and (df2['y'][i] > 30) and (df2['y'][i] < 50):
                total += 1
                for x in range(i, len(df2['x'])):
                    if df2['outcome'][x] != 'Unsuccessful' and df2['endX'][x] < 80:
                        continue
                    if df2['outcome'][x] != 'Unsuccessful' and df2['endX'][x] > 80:
                        completions += 1
                    n = x+1
                    on = True
                    break
                break

    percentage = (completions/total)*100
    return percentage


teams = data['team_id'].unique().tolist()
comparison = []
for team in teams:
    rank = deep_completions_percentage(data, team)
    comparison.append(rank)
    
comparison


# In[7]:


comparison.sort(reverse=True)
laliga_teams = ['Barcelona', 'Real Madrid', 'Villarreal', 'Eibar', 'Real Sociedad', 'Sevilla', 'Huesca', 'Valencia',
               'Real Betis', 'Levante', 'Athletic Bilbao', 'Atletico Madrid', 'Celta Vigo', 'Osasuna', 'Elche',
               'Real Valladolid', 'Alaves', 'Cadiz', 'Getafe', 'Granada']


# In[8]:


fig, ax = plt.subplots(figsize=(18,12),facecolor='#222222')
ax.set_facecolor('#222222')
ax.barh(laliga_teams, comparison)
ax.margins(y=0)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('% Of Final Third Entries From Uninterrupted Goal Kick Sequences',c='white',size=17,fontfamily='serif',labelpad=20,ha='center')
ax.set_yticklabels(laliga_teams,size=17,fontfamily='serif',color='white')
ax.set_xticklabels([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20], size=13, fontfamily='serif', color='white')
ax.tick_params(axis='y', size=0)
ax.tick_params(axis='x', size=0)
ax.invert_yaxis()
ax.text(-3, -1, ' Which La Liga Teams Had The Highest Final Third Entry Rates From Goal Kick Actions Last Season?', color='white',size=22,fontweight='bold')
plt.tight_layout()
plt.savefig("final third entries", dpi=500, bbox_inches="tight")


# In[ ]:




