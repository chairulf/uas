# coding: utf-8

# In[4]:


import nltk


# stemming tries different methods to find the stem of a word

# In[5]:


raw = """i have to tell the world that im not sure if i like any of you. just gimme all your hoes and and money and leave me alone.
i promise i will give you the hoes back when im done"""


# In[10]:


tkn = nltk.tokenize.word_tokenize(raw)


# In[11]:


tkn


# In[12]:


porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()


# In[16]:


[porter.stem(t) for t in tkn]


# In[17]:


tk2 = nltk.tokenize.word_tokenize(raw)
[lancaster.stem(t) for t in tk2]


# lemmetization tries to reduce a word to its dictionary form

# In[18]:


tk3 = nltk.tokenize.word_tokenize(raw)


# In[20]:


wnl = nltk.WordNetLemmatizer()


# In[21]:


[wnl.lemmatize(t) for t in tk3]