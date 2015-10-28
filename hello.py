import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'SIGCHI-UIUC lapcounter backend'

@app.route('/info/users')
def user_info():
	return 'an array of all users /user/info'

@app.route('/info/users/data')
def user_data():
	return jsonify({ 'Name': 'James Lee', 'year': 2018, 'registered': 2015, 'Average Lap Completion Time': 20, 
		'Average Speed': 10, 'Fastest Lap Time': 10, 'Total Laps Completed': 20, 'Total Distance Ran': 10, 'Total time spent running':30  }
	#return jsonify( Name = g.user.username,)
	#return 'all information of a specific user'

@app.route('/session/info')
def session_info():
	return 'all information of a specific running session'


