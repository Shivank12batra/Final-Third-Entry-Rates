import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
chrome_driver_path = r'C:\Users\shivank\Untitled Folder\chromedriver.exe'


data = pd.read_csv('LaLigaPass.csv')

data['x'] = data['x']*1.2
data['y'] = data['y']*0.8
data['endX'] = data['endX']*1.2
data['endY'] = data['endY']*0.8


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
            if (df2['x'][i] < 6) and (30 < df2['y'][i] < 50) and (df2['endX'][i] < 18) and (18 < df2['endY'][i] < 62):
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

driver.get('https://1xbet.whoscored.com/Teams/60/Show/Spain-Deportivo-Alaves')
names = []
for team in teams:
    driver.get('https://1xbet.whoscored.com/Teams/{}/Show/Spain-Deportivo-Alaves'.format(team))
    element = driver.find_element_by_css_selector('.team-header-name')
    names.append(element.text)
driver.close()

comparison = [final_third_percentage(data, team) for team in teams]
c_list = zip(comparison, teams, names)
c_list = sorted(c_list, key=lambda x: x[0], reverse=True)
names = [c[2] for c in c_list]
rank = [c[0] for c in c_list]


fig, ax = plt.subplots(figsize=(18,12),facecolor='#222222')
ax.set_facecolor('#222222')
ax.barh(names, rank, color='red')
ax.margins(y=0)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('% Of Final Third Entries From Uninterrupted Short Goal Kick Sequences',c='white',size=17,fontfamily='serif',labelpad=20,ha='center')
ax.set_yticklabels(names,size=17,fontfamily='serif',color='white')
ax.set_xticklabels([0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20], size=13, fontfamily='serif', color='white')
ax.tick_params(axis='y', size=0)
ax.tick_params(axis='x', size=0)
ax.invert_yaxis()
ax.text(-3, -1.5, ' Which La Liga Teams Had The Highest Final Third Entry Rates From Short Goal Kick Sequences?', color='white',size=22,fontweight='bold',fontfamily='serif')
ax.text(7, -1, 'La Liga 20/21', color='white',size=20, fontweight='bold', fontfamily='serif')
plt.tight_layout()
plt.savefig("final third entries", dpi=500, bbox_inches="tight")





