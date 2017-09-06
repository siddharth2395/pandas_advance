import pandas as pd
import numpy as np

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv',
                      header=0,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})
print chicago.head()
by_dept = chicago.groupby('department')
print "-" * 50, "\n", by_dept
print "-" * 50
print(by_dept.count().head())  # NOT NULL records within each column
print('\n')
print(by_dept.size().tail())  # total records for each department

print "-" * 50, "\nsum:"
print(by_dept.sum()[20:25])  # total salaries of each department
print "-" * 50, "\nmean:"
print(by_dept.mean()[20:25])  # average salary of each department
print "-" * 50, "\nmedian:"
print(by_dept.median()[20:25])  # take that, RDBMS!

print "-" * 50, "\n", by_dept.title.nunique().sort_values(ascending=False)[:5]


def ranker(df):
    """Assigns a rank to each employee based on salary, with 1 being the highest paid.
    Assumes the data is DESC sorted."""
    df['dept_rank'] = np.arange(len(df)) + 1
    return df


chicago.sort_values('salary', ascending=False, inplace=True)
chicago = chicago.groupby('department').apply(ranker)
print "-" * 50
print(chicago[chicago.dept_rank == 1].head(7))

print "-" * 50, "\n", chicago[chicago.department == "LAW"][
                      :5]  # each employee ranks within their department based on salary
