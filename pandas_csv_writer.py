import pandas as pd
import numpy as np

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv',
                      header=0,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})

by_dept = chicago.groupby('department')


def ranker(df):
    """Assigns a rank to each employee based on salary, with 1 being the highest paid.
    Assumes the data is DESC sorted."""
    df['dept_rank'] = np.arange(len(df)) + 1
    return df


chicago.sort_values('salary', ascending=False, inplace=True)
chicago = chicago.groupby('department').apply(ranker)
# print  chicago.head(10)
chicago.sort_index(ascending=True, inplace=True)
chicago.to_csv("t1.csv", index=False, encoding='utf-8')
