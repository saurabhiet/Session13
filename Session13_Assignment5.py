import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays':  [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

df_ = pd.DataFrame()
df_['From'] = df['From_To'].str.split('_').str[0].str.capitalize()
df_['To'] = df['From_To'].str.split('_').str[1].str.capitalize()
df = df.drop('From_To', 1)
df['From'] = df_['From']
df['To'] = df_['To']
df2 = pd.DataFrame()
df2 = df['RecentDelays'].apply(pd.Series)
df2 = df2.rename(columns = lambda x : 'Delay_' + str(x))

df = pd.concat([df[:], df2[:]], axis=1)
df = df.drop('RecentDelays', 1)
df