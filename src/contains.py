#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


small_basics = pd.read_csv('../data/small.basics.tsv', sep='\t')
small_rat = pd.read_csv('../data/small.ratings.tsv', sep='\t')
#large_basics = pd.read_csv('../data/title.basics.tsv', sep='\t')
#large_rat = pd.read_csv('../data/title.ratings.tsv', sep='\t')


# In[4]:


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


# In[5]:


def gettitle(dataset):
    titles= []
    for i in dataset.columns:
        titles.append(i.capitalize())
    return titles


# In[ ]:


small_basics


# In[22]:


def contains(dataset,stri):
    print(dataset.loc[dataset['primaryTitle'] == stri].to_dict())


# In[25]:


start = time.time()
contains(small_basics,'Avengers: Infinity War')
contains(small_basics,'Natural Born Killers')
contains(small_basics,'WXYZ')
contains(small_basics,'The Shawshank Redemption')
contains(small_basics,'Showgirls')
contains(small_basics,'Strange Days')
end = time.time()
print('elapsed time (s): '+str(end - start))


# In[ ]:




