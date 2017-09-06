import pandas as pd
import numpy as np

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv',
                      header=0,
                      names=headers,
                      converters={'salary': lambda x: float(x.replace('$', ''))})
avg_salary=int(chicago['salary'].mean())
print "-"*50,"\navg salary:",avg_salary
print "-"*50,"\n",(chicago[(chicago['salary'] >= avg_salary)].name.count()*100)/chicago.name.count(),"% are above avg."
print "-"*50,"\nemployees who's salary is above avg.\n",chicago[(chicago['salary'] >= avg_salary)][:5] #finding employees who's salary is above avg. upto 5 records
print "-"*50,"\nemployees who's salary is min.\n",chicago[(chicago['salary'] == chicago['salary'].min())] #finding employees who's salary is min.
print "-"*50,"\nemployees who's salary is max.\n",chicago[(chicago['salary'] == chicago['salary'].max())] #finding employees who's salary is max.

by_dept = chicago.groupby('department')

dept_mean=by_dept['salary'].mean()
print "-"*50,"\n avg of each dept\n",dept_mean #finding avg of each department

#finding min and max of each department and combining in to one dataframe
dept_min = by_dept['salary'].min()
dept_max = by_dept['salary'].max()
d = {'avg':dept_mean.round(2),'max':dept_max,'min':dept_min}
print "-"*50
dept_salary_stats=pd.DataFrame(d)
dept_salary_stats.to_csv('dept_salary_stats.csv', encoding='utf-8')