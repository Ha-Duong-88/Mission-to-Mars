#!/usr/bin/env python
# coding: utf-8

# ### Scrape Mars Data: The News
# 

# In[13]:


# 10.3.3
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[2]:


# Set the executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


####################################################
# --- Breakdown of code ----
# browser.is_element_present_by_css('div.list_text', wait_time=1) --> Search for elements with a specific combination
# of tag (div) and attribute (list_text).
# Secondly, we're also telling our browser to wait one second before searching for components. This is our parent element.
####################################################


# In[4]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


####################################################
#--- Breakdown of code ---
# Create an HTML object
# Use BeautifulSoup to parse the HTML object
# We've assigned slide_elem as the variable to look for the <div /> tag and its descendent (the other tags within 
# the <div /> element).
# This is our Parent element = this element holds all of the o ther elements within it, and we'll reference it 
# when we want to filter results even further.
# The . is used for selecting classes, such as list_text, so the code 'div.list_text' pinpoints the <div /> tag 
# with the class of list_text. 
# CSS works from right to left, such as returning the last item on the list instead of the first. 
# Because of this, when using select_one, the first matching element returned will be a <li /> element with
# a class of slide and all nested elements within it.
# We want to collect from this website the most recent news article along with its summary.
# This code will be eventually used in an app that will scrape live data with the click of a button.
####################################################


# In[5]:


# Assign the title and summary text to variables we'll reference later
# Begin scraping

slide_elem.find('div', class=_'content_title')

####################################################
# --- Breakdown of code ---
# We chained .find onto our previously assigned variable, slide_elem.
# The data we're looking for is the content title, which we've specified by saying, "The specific data is in 
# a <div /> with a class of 'content_title'."
####################################################


# In[6]:


# We want to get just the text
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


####################################################
# --- Breakdown of code ---
# We've added something new to our .find() method here: .get_text().
# When this new method is chained onto .find(), only the text of the element is returned. 
# This code returns only the title of the news article and not any of the HTML tags or elements.
# We have created a new variable for the title, added the get_text() method, and we’re searching within the parent 
# element for the title.
# <div/> is the tag
# class/attribute = 'content_title'
# The specific data is in a <div /> with a class of 'content_title'."
####################################################


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Output should only be the summary of the article


# ### Scrape Mars Data: Featured Image

# In[8]:


# 10.3.4 
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

####################################################
# --- Breakdown of code ---
# full_image_elem = this is a new variable to hold the scraping results
# browser.find_by_tag(‘button’) --> The browser finds an element by its tag
# The index is chained at the end of the first LOC to tell browser to click the second button
# full_image_elem.click() --> Splinter will "click" the image to view its full size
####################################################


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


####################################################
# --- Breakdown of code ---
# An img tag is nested within this HTML, so we've included it.
# .get('src') pulls the link to the image.
# We've told BeautifulSoup to look inside the <img /> tag for an image with a class of fancybox-image.
# We're pulling the link to the image by pointn BS4 to where the image will be instead of grabbing the URL directly.
# mportant to note that the value of the src will be different every time the page is updated, so we can't 
# simply record the current value.
####################################################


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Scrape Mars Data: Mars Facts
# 

# In[14]:


# 10.3.5
# Instead of scraping each row or the data in the </td/> tag (tag for each table row), scrape the entire table with
# pandas
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


####################################################
# --- Breakdown of code ---
# df = pd.read_htmldf = pd.read_html('https://galaxyfacts-mars.com')[0] --> We're creating the new DataFrame
# from the HTML table.
# read_html() Pandas function --> specifically searches for and returns a list of tables found in the HTML.
# By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item 
# in the list. 
# Then, turn the table into a DataFrame.

# df.columns=['description', 'Mars', 'Earth'] --> Assign columns to the new DF 

# df.set_index('description', inplace=True) --> By using the .set_index() function --> turning the Description 
# column into the DataFrame's index.
# inplace=True means that the updated index will remain in place, without having to reassign the DataFrame to a 
# new variable.
####################################################


# In[15]:


# Add DataFrame to a web application
df.to_html()

# This is a <table/> element with a lot of nested elements


# In[20]:


# Quite automated browser session
browser.quit()


# ### Export to Python

# In[ ]:


# 10.3.6
# We pulled article summaries and titles, a table of facts, and a featured image 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




