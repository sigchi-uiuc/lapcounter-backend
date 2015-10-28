import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'SIGCHI-UIUC lapcounter backend'

@app.route('/info/users')
def user_info():
	return 'an array of all users /user/info'

@app.route('/info/users/data')
def user_data():
	return 'all information of a specific user'

@app.route('/session/info')
def session_info():
	return 'all information of a specific running session'


