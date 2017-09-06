import pandas as pd
from_csv = pd.read_csv('peyton-passing-TDs-2012.csv')
cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,names=cols)
print no_headers.head()
