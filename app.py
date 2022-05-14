# source venv/bin/activate  will start the virtual environment for this app. #
# use code below to run the app on a dev server

# export FLASK_APP=app.py      
# export FLASK_ENV=development
# flask run

import os 
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
	app = Flask(__name__)
	client = MongoClient(os.environ.get("MONGODB_URI"))
	app.db =  client.microblog # this is not good practice


	@app.route('/', methods=['GET', 'POST']) # this is the route for this particular page - is it oop so i don't have to build all pages here though? 
	def home():
		if request.method == 'POST':
			entry_content = request.form.get("content")
			formatted_date =  datetime.datetime.today().strftime("%Y-%m-%d")
			app.db.entries.insert({"content": entry_content, "date":formatted_date})

		entries_with_date = [
			(
				entry["content"], 
				entry["date"],
				datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime('%b %d')
			)
			for entry in app.db.entries.find({})
		]
		return render_template("home.html", entries=entries_with_date)
	return app
