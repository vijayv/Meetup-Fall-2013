# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Exercise Titanic Data

# <markdowncell>

# This is the 892 line training set from [Kaggle](http://www.kaggle.com/c/titanic-gettingStarted/data).

# <codecell>

import os, csv
data_path = os.path.join('data','titanic.csv')
print data_path

# <markdowncell>

# ### Read the data
# 
# - Consider using the `csv` module
# - Verify that you get `892` lines

# <codecell>

with open(data_path,'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# <codecell>

print len(data)

# <markdowncell>

# ### What percent of the people survied?
# 
# - If the first column is a one, they survived.
# - You *may* need to catch a `ValueError`
# - Make sure you compare the same types:
# ```python
#     d[0] == '1'
#     int(d[0]) == 1
# ```

# <codecell>

survived = 0
for d in data:
    try:
        if int(d[0]) == 1:
            survived+=1
    except ValueError:
        pass

# <codecell>

print survived/float(len(data))*100

# <markdowncell>

# ### Function
# 
# Write a function that returns a dictionary of the number of `survived`, `not survived`, and `unknown`.  Here is the example function call:
# ```python
# print titanic_function(data)
# 
# {'unknown': 1, 'survived': 342, 'not survived': 549}
# 
# ```

# <codecell>

def titanic_function(data):
    tmp = {}
    for d in data:
        try:
            if int(d[0]) == 1:
                tmp['survived'] = tmp.get('survived',0) + 1
            else:
                tmp['not survived'] = tmp.get('not survived',0) + 1
        except ValueError:
                tmp['unknown'] = tmp.get('unknown',0) + 1
    return tmp

# <codecell>

print titanic_function(data)

# <markdowncell>

# ###What percent of males survived? Females?

# <codecell>

def titanic_function(data):
    M = {}
    F = {}
    for d in data:
        try:
            if d[3] == 'male':
                if int(d[0]) == 1:
                    M['survived'] = M.get('survived',0) + 1
                else:
                    M['not survived'] = M.get('not survived',0) + 1
            elif d[3] == 'female':
                if int(d[0]) == 1:
                    F['survived'] = F.get('survived',0) + 1
                else:
                    F['not survived'] = F.get('not survived',0) + 1
            else:
                pass
        except ValueError:
            pass
    return {'male': M, 'female': F}

# <codecell>

val = titanic_function(data)

# <codecell>

print val['male']['survived']/float( val['male']['survived'] + val['male']['not survived'])*100

# <codecell>

print val['female']['survived']/float(val['female']['survived'] + val['female']['not survived'])*100

# <codecell>


# <codecell>


