import pandas as pd

pd.set_option('max_columns', 50)

l = [i * 2 for i in xrange(10)]
s = pd.Series(l)
print  s