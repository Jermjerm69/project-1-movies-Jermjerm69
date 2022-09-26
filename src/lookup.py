#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


small_basics = pd.read_csv('../data/small.basics.tsv', sep='\t')
small_rat = pd.read_csv('../data/small.ratings.tsv', sep='\t')
large_basics = pd.read_csv('../data/title.basics.tsv', sep='\t')
large_rat = pd.read_csv('../data/title.ratings.tsv', sep='\t')


# In[ ]:


small_basics.head()


# In[ ]:


import time
def to_dict_fun(dataset,rats):
    start = time.time()
    # do jobs here
    small_basics_dict = dataset.to_dict()
    end = time.time()
    print('reading data/small.basics.tsv into dict...')
    print('elapsed time (s): '+str(end - start))
    
    start = time.time()
    smal_rate = rats.to_dict()
    end = time.time()
    print(' ')
    print('reading data/small.ratings.tsv into dict...')
    print('elapsed time (s): '+str(end - start))
    
    print(' ')
    print('Total movies: '+str(dataset.index.stop))
    print('Total ratings: '+str(rats.index.stop))
    print(' ')
    return small_basics_dict


# In[ ]:


lookup(small_basics,'tt0033467')


# In[ ]:


def lookup(dataset,ids):
    start = time.time()
    dat = dataset.where(small_basics['tconst'] == ids).dropna()
    if len(dataset) == 0:
        print('No match found!')
    else:
        a = list(dat.to_records())[0]
        for i in a:
            i = str(i).capitalize()
        print(gettitle(dataset))
        print(a)
        end = time.time()
        print('elapsed time (s): '+str(end - start))


# In[ ]:


lookup(small_basics,'tt0111161')


# In[ ]:




