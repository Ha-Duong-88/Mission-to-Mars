# Flask and Mongo
# This code allows us to use Flask and Mongo to create web app
# 10.5.1

# Import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# First line --> Use flask to render a template, redirecting to another URL, and creating a URL
# Second line --> Use PyMongo to interact with Mongo database
# Third line --> Use the scraping code by converting from Juypter Notebook to Python

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo
# App can reach Mongo through localhost server, using port 27017, using  a databased named mars_app

# Set up Flask routes
# Set up flask route for the main page when visiting the web app and one to scrape neew data
# Flask routes bind URLs to functions. These routes can be embedded in web app and accessed via links or buttons.
# index.html = default HTML file that we'll use to display the content we scraped.
# mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script. We will also assign that path to themars variable for use later.
# return render_template("index.html" tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.
# , mars=mars) tells Python to use the "mars" collection in MongoDB.
# This function is what links our visual representation of our work, our web app, to the code that powers it.
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# Add another route
# scrape() --> function to set up our scraping route
# Our next function will set up our scraping route. This route will be the "button" of the web application, the one that will scrape updated data when we tell it to from the homepage of our web app.
# This route, “/scrape”, will run the function that we create just beneath it.
# The next lines allow us to access the database, scrape new data using our scraping.py script, update the database, and return a message when successful.
# First, we define it with def scrape():.
# Next, we created a new variable to hold the newly scraped data: mars_data = scraping.scrape_all(). In this line, we're referencing the scrape_all function in the scraping.py file exported from Jupyter Notebook.
# we need to update the database using .update()
# We're inserting data, so first we'll need to add an empty JSON object with {} 
# Next, we'll use the data we have stored in mars_data.
# Finally, the option we'll include is upsert=True. This indicates to Mongo to create a new document if one doesn't already exist, and new data will always be saved
# Finally, we will add a redirect after successfully scraping the data: return redirect('/', code=302). This will navigate our page back to / where we can see the updated content.
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


# Run Flask
if __name__ == "__main__":
   app.run()