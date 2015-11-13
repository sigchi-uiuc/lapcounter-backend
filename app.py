from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lab_counter_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://igsusmnkuuuiff:aJMRa9Tw81so2ncyhLvDED6prS@ec2-107-21-222-62.compute-1.amazonaws.com:5432/dflphcsocv57hu'
db = SQLAlchemy(app)


# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

#ran array of all users
@app.route('/info/users')
def user_info():
    foos = User.query.all()
    results = [ foo.as_dict() for foo in foos ]
    return jsonify({'results': results})

#return all information of a specific user
@app.route('/info/<input_users>/data')
def user_data(input_users):
    result = db.session.query(User).filter(User.name == input_users).one()
    return jsonify(result.data.serialize)

#return all information of a specific running session
@app.route('/session/info')
def session_info():
    return jsonify({ 'Average_Lap_Speed':100 ,'Fastest_Lap_Speed':20, 'Duration_Session':30, 'Start_Session':'2:20', 'End_Session':'1:10'})

# Save e-mail to database and send to success page
@app.route('/upload', methods=['POST'])
def upload():
    name = None
    registered = None
    avg_lap_completed_time = None
    avg_speed = None
    fastest_lap_time  = None
    total_laps_completed = None
    total_distance_ran = None
    total_time_spent_running = None

    if request.method == 'POST':
        name = request.form['name']
        registered = request.form['registered']
        alct = request.form['alct']
        avg_speed = request.form['avg_speed']
        fastest_lap_time = request.form['fastest_lap_time']
        tlc = request.form['tlc']
        tdr = request.form['tdr']
        ttsr = request.form['ttsr']

        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.name == name).count():
            reg_data = Data(alct, avg_speed, fastest_lap_time, tlc, tdr, ttsr)
            reg_user = User(name, registered, reg_data)
            db.session.add(reg_user)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()