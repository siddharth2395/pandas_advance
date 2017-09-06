import pandas as pd

left_frame = pd.DataFrame({'key': range(5),'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7),'right_value': ['f', 'g', 'h', 'i', 'j']})

print(left_frame)
print('\n')
print(right_frame)

print "-"*50,"\n",pd.merge(left_frame, right_frame, on='key', how='inner')#inner join
print "-"*50,"\n",pd.merge(left_frame, right_frame, on='key', how='left')#left outer join
print "-"*50,"\n",pd.merge(left_frame, right_frame, on='key', how='right')#right outer join
print "-"*50,"\n",pd.merge(left_frame, right_frame, on='key', how='outer')#full outer join
print "-"*50,"\n",pd.concat([left_frame, right_frame])#concat equivalent to SQL's UNION clause
print "-"*50,"\n",pd.concat([left_frame, right_frame], axis=1)#concate  side-by-side


