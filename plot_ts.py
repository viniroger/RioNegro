#!/usr/bin/env python3.9.5
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def select_year(year, df):
    '''
    Select values from interval
    '''
    start_date = f'{year}-12-01'
    end_date = f'{year+1}-06-30'
    mask = (df['dia'] >= start_date) & (df['dia'] <= end_date)
    df_sel = df.loc[mask].reset_index(drop=True).copy()
    # If cota==0 is NaN
    df_sel['cota'] = df_sel['cota'].replace({0.00:np.nan})
    # Ignore year + sum number of days until Nov 30
    df_sel['index'] = df_sel.index + 334
    return df_sel

# Get data from file and convert date column to datetime
df = pd.read_csv('cotas_RioNegro.csv', delimiter=',')
df['dia'] = pd.to_datetime(df['dia'])

# Start plot
plt.title('Cotas Rio Negro (m) - Dezembro a Junho')
ax = plt.gca()
ax.set_ylim([15, 31])
# Plot some years
plot_years = [2001,2014,2020]

# Loop for all years - plot some
years = range(2000,2021)
for year in years:
    print(year)
    # Select dates from time interval
    df_sel = select_year(year, df)
    # Plot just if year is in list 'years'
    if year in plot_years:
        plt.plot(df_sel['index'],df_sel['cota'], marker='.', linestyle='',\
         label=f'{year}-{year+1}')
    # Sum all cota values (create if doesn't exist)
    if 'df_sum' in globals():
        df_sum['cota'] = df_sum['cota'] + df_sel['cota']
        n = n + 1
    else:
        df_sum = pd.DataFrame(columns=['cota'])
        df_sum['cota'] = df_sel['cota']
        n = 1
# Calculate mean
df_sum['cota'] = df_sum['cota']/n
# Ignore year + sum number of days until Nov 30
df_sum['index'] = df_sum.index + 334

# Plot mean
plt.plot(df_sum['index'],df_sum['cota'], marker='.', linestyle='', label='Média 00-20')
# Finalize plot
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('cotas_m.png')
plt.close()
