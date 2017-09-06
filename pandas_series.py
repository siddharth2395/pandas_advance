import pandas as pd

pd.set_option('max_columns', 50)

l = [i * 2 for i in xrange(10)]
s = pd.Series(l)
print  s

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print  cities
print cities[['Chicago', 'Portland', 'San Francisco']]
print "\n----"
c = cities[cities < 1000]
print c[c>500]
