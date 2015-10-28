import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'SIGCHI-UIUC lapcounter backend'

#ran array of all users
@app.route('/info/users')
def user_info():
	return jsonify({ '1': 'user1', '2':'user2', '3':'user3'})

#return all information of a specific user
@app.route('/info/users/data')
def user_data(name):
	return jsonify({ 'Name': 'James Lee', 'year': 2018, 'registered': 2015, 'Average_Lap_Completion_Time': 20, 
		'Average_Speed': 10, 'Fastest_Lap_Time': 10, 'Total_Laps_Completed': 20, 'Total_Distance_Ran': 10, 'Total_time_spent_running':30 })

#return all information of a specific running session
@app.route('/session/info')
def session_info():
	return jsonify({ 'Average_Lap_Speed':100 ,'Fastest_Lap_Speed':20, 'Duration_Session':30, 'Start_Session':'2:20', 'End_Session':'1:10'})
