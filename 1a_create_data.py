#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pyttsx3
import pandas as pd

from num2words import num2words
from IPython.display import Audio
from tqdm import tqdm


# In[3]:


for number in tqdm(range(1000)):
    text = num2words(number)
    text = text.replace('-', ' ')
    filename = text.replace(' ', '_') + '.mp3'
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.save_to_file(text, f'Data/spoken_numbers/recordings/{filename}')
    engine.runAndWait()
    engine.stop()


# In[4]:


data = []
for number in range(1000):
    text = num2words(number)
    text = text.replace('-', ' ')
    filename = text.replace(' ', '_') + '.mp3'
    data.append({'text': text, 'filename': filename})


# In[5]:


data = pd.DataFrame(data)
data.to_csv('Data/spoken_numbers/data.csv', index=False)


# In[6]:


Audio('Data/spoken_numbers/recordings/eighteen.mp3', rate=rate)


# In[ ]:




