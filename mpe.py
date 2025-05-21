#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as pa
import time

pa.PAUSE = 1

pa.press('win')
pa.write("Microsoft Edge")
pa.press('Enter')
time.sleep(2)
pa.click(x=1008, y=30)
pa.write("Youtube.com", interval=0.5)
pa.press('Enter')
time.sleep(5)
pa.click(x=531, y=103)
pa.write("skyrim ambient music everness")
pa.press("enter")
pa.click(x=527, y=271)


# In[ ]:




