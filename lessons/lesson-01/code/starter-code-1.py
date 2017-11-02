
# coding: utf-8

# # Check to see if you're ready to go on Monday!
# 1. Run each block of code
# 2. Check for errors
# 3. When you think you're error free, flag down a teaching team member to confirm

# In[1]:


####This is what an error looks like
print ba


# # Objectives
# ### Get comfortable with IPython Notebook
# 
# * How to start IPython Notebook
# * How to read data into pandas
# * How to do simple manipulations on pandas dataframes
# 
# 
# ## Start a notebook:
# For each class, we'll be using a set of common data science libraries and tools, like the IPython notebook. You can start an IPython notebook by running
# 
# ```
# jupyter notebook $NAME_OF_FILE
# ```

# 
# ## Try it yourself!
# Read and run the block of code below by: 
# 1. Clicking on it and pressing the play button above or
# 2. Using a short cut- (help --> keyboard shortcuts)

# In[2]:


import os
os.getcwd()


# In[3]:


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

mpl.rcParams['figure.figsize'] = (15, 6)
pd.set_option('display.width', 4000)
pd.set_option('display.max_columns', 100)


# # First: Read in the data
# ### Review Simple Commands
# 
# Practice downloading and reading into sample data

# In[5]:


# Download and read the data (this may take more than 1 minute)
orig_data = pd.read_csv('./datasets/311-service-requests.csv', parse_dates=['Created Date'], low_memory=False)


# In[6]:


plt.scatter(orig_data['Longitude'], orig_data['Latitude'], marker='.', color="purple")


# ## Try this Example: 
# Graph the number of noise complaints each hour in New York

# In[7]:


complaints = orig_data[['Created Date', 'Complaint Type']]
noise_complaints = complaints[complaints['Complaint Type'] == 'Noise - Street/Sidewalk']
noise_complaints.set_index('Created Date').sort_index().resample('H', how=len).plot()


# # Second: Using IPython
# ### Review Python Basics
# 
# Test your skills by answering the following questions:

# #### Question 1.  Divide 10 by 20 and set the result to a variable named "A"

# In[4]:


### Insert your code here and then uncomment | print A | when you are ready to test it. 

#print(A)
a = 10.0 /20.0
print a


# In[ ]:


#### If you did not get a float (decimals), alter your equation to get the desired result (0.5)


# #### Question 2. Create a function called division that will divide any two numbers and prints the result (with decimals). 
# Call your function. Confirm that the results are as expected.

# In[6]:


# add your function here
def division(x,y):
    print float(x)/float(y)
    
division(25,5)


# #### Question 3. Using .split() split my string into separate words in a variable named words

# In[8]:


my_string = "the cow jumped over the moon"
# put your code here it should return ['the', 'cow', 'jumped', 'over', 'the', 'moon']
words = my_string.split()
print(words)


# #### Question 4. How many words are in my_string?

# In[12]:


print len(words)


# #### Question 5. Use a list comprehension to find the length of each word
# 
# result: [3, 3, 6, 4, 3, 4]

# In[16]:


print [len(n) for n in words]


# #### Question 6. Put the words back together in a variable called sentence using .join()
# result:
# the cow jumped over the moon

# In[21]:


print ' '.join(words)


# #### Bonus: Add a "||" between each word
# result: 
# the||cow||jumped||over||the||moon

# In[19]:


print '||'.join(words)

