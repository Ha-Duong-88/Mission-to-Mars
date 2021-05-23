#!/usr/bin/env python
# coding: utf-8

# ### Scrape Mars Data: The News
# Separate scraping code into its own function

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# Connect to Mongo and establish communication between our code and the database we're using.
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    # This dictionary does two things: It runs all of the functions we've created and stores all of the results.
    # When we create the HTML template, we'll create paths to the dictionary's values, which lets us present our data on our template.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(), 
        "hemispheres": mars_hemisphere(browser),
        "last_modified": dt.datetime.now()
    }
    # Create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image.
    hemisphere = {}
        
        
    # Stop webdriver and return data
    browser.quit()
    return data

# When we add the word "browser" to our function, we're telling Python that we'll be using the browser variable we defined outside the function.
def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    # Print title and paragraph from the function so they can be used outside of it
    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-responsive")


# Create a function that will scrape the hemisphere data by using your code from the Mission_to_Mars_Challenge.py file.
def mars_hemisphere(browser):
    
    # Scrape the Mars hemisphere data
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Create empty list to hold image urls and titles
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.
    links = browser.find_by_css('a.product-item img')
    print(links)

    for i in range(len(links)):
        hemisphere_item = {}
    
        link = browser.find_by_css('a.product-item h3')[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere_item["image"] = sample_elem["href"]
        title = browser.find_by_css('h2.title')
        hemisphere_item["title"] = title.text
        hemisphere_image_urls.append(hemisphere_item)
        browser.back()
        print(hemisphere_image_urls[0])

    #print(i)
    return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































