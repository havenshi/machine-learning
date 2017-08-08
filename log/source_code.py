#!/usr/bin/env python3

import pandas as pd
from pandas import ExcelWriter

# delete beginning
lines = open('u_ex170703_x.log').readlines()
open('newfile1.txt', 'w').writelines(lines[4:-1])

# add headers
user_cols = ['date', 'time', 's-ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port', 'cs-username', 'c-ip', 'cs(User-Agent)', 'cs(Referer)', 'sc-status', 'sc-substatus', 'sc-win32-status', 'time-taken', 'c-ip-1']
# parce columns
df = pd.read_table('newfile1.txt', sep=" ", names = user_cols)

# group by col
result = df.groupby('c-ip-1').size().sort_values(ascending=False).reset_index(name='count')

# new file.xlsx
writer = ExcelWriter('file.xlsx')
result.to_excel(writer)
writer.save()

# DF TO CSV
result.to_csv('v.csv', sep=',')