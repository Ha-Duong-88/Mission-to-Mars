# Flask and Mongo

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
# Flask routes bind URLs to functions. These route can be embedded in web app and accessed via links or buttons.
# index.html = default HTML file that we'll use to display the content we scraped.
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# Add another route
# scrape() --> function to set up our scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


# Run Flask
if __name__ == "__main__":
   app.run()