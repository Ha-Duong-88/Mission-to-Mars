# Mission-to-Mars
Module 10 - Web Scraping with HTML/CSS

# Overview
The objective of this project is to extract the most recently published Mars articles' title and summary by finding the HTML components from multiple scraping-friendly websites.

This reciprocity presents a web application on Mars data including live data from NASA, Jet Propulsion Laboratory, GalaxyFacts.com, and the Astrogeology Science Center. Using DevTools to inspect the HTML elements and structure, Splinter to automate the web browser, BeautifulSoup to parse and extract HTML data, MongoDB to hold the scraped data, and Flask to present, the delivered web application includes different types of data including live text, tables, and images that can be updated with a click of a button. The Flask application also includes Bootstap components for styling and appearance.

# Steps
The following were the steps taken to design, develop and deploy the web application to present the scraped live data.

1) Using DevTools, examine the webpages from each website and search and pinpoint specific HTML components and data to extract.

2) Set up Splinter to automate a browswer and interact with webpages.

3) Create scraping code using BeautifulSoup in Jupyter Notebook to test the code as it is written and Splinter to automate the browser. By using Jupyter Notebook, "chunks" of code can be tested and run independently. The code as written is designed to scrape the most recent data meaning each each the script is run, it will pull the newest data available.  

4) Convert the Jupyter Notebook ipynb scraping, Splinter and Flask code to Python scripts. Jupyter Notebook file cannot automate the browser. Automation of the browser and the scraping functions requires Python. 

5) Initiate a Mongo database instance and create a Mongo database to store the scraped data, allowing it to be accessed and retrieved as needed. 

6) Use flask to create a web applicatio to present the live data scraped from scraping-friendly websites. This step involved building the framework for the application using Flask and Mongo together.

7) In order to integrate the scraping code with Flask, add functions and error handling. These functions will also help the performance of the web application.

8) Integrate Mongo into the web application created. The scraping script will update the data stored in Mongo each time that it is run. In order to accomplish this, create function to initialize the browser, create a data dictionary, and end the WebDriver and return the scraped data.

9) Finally, use Bootstrap to stylize the appearance of the web application, such as making the webpages responsive to different device factors and screen sizes, changing the color of the scrape button, adding thumbnails, and customizing the table.


 

