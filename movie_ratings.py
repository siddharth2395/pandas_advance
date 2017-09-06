import pandas as pd

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')
print movies.info()

print "-" * 50, "\n", movies.dtypes
print "-" * 50, "\n", users.describe()
print "-" * 50, "\n", movies.head()
print "-" * 50, "\n", movies.tail()
print "-" * 50, "\n", movies[20:22]
print "-" * 50, "\n", users['occupation'].head()
print "-" * 50, "\n", users[['age', 'zip_code']].head()
print "-" * 50, "\n", users[users.age > 25].head()
print "-" * 50, "\n", users[(users.age == 40) & (users.sex == 'M')].head(3)
print "-" * 50, "\n", users[(users.sex == 'F') | (users.age < 30)].head(3)

print  "\n" * 3
print "-" * 50

print(users.set_index('user_id').head())  # makes user_id and returns new df
print('\n')
print(users.head())  # doesn't actually modify original df
print("\n^^^didn't actually change the DataFrame.^^^\n")
with_new_index = users.set_index('user_id')  # making a copy of df with user_id as index
print(with_new_index.head())
print("\n^^^set_index actually returns a new DataFrame.^^^\n")

print "-" * 50

print(users.iloc[99])
print('\n')
print(users.iloc[[1, 50, 300]])

print "-" * 50

print(users.loc[100])
print('\n')
print(users.loc[[2, 51, 301]])

with_new_index.reset_index(inplace=True)  # reset_index to df copy we made above line 36
print "-" * 50, "\n", with_new_index.head()
