from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lab_counter_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://igsusmnkuuuiff:aJMRa9Tw81so2ncyhLvDED6prS@ec2-107-21-222-62.compute-1.amazonaws.com:5432/dflphcsocv57hu'
db = SQLAlchemy(app)

# Set "homepage" to index.html
@app.route('/')
def index():
    render_data = {'data' : "15"}
    resp = make_response(render_template("index.html", name = render_data))
    return resp

#ran array of all users
@app.route('/info/users')
def user_info():
    return jsonify({ '1': 'user1', '2':'user2', '3':'user3'})

#return all information of a specific user
@app.route('/info/users/data')
def user_data():
    return jsonify({ 'Name': 'James Lee', 'year': 2018, 'registered': 2015, 'Average_Lap_Completion_Time': 20, 
        'Average_Speed': 10, 'Fastest_Lap_Time': 10, 'Total_Laps_Completed': 20, 'Total_Distance_Ran': 10, 'Total_time_spent_running':30 })

#return all information of a specific running session
@app.route('/session/info')
def session_info():
    return jsonify({ 'Average_Lap_Speed':100 ,'Fastest_Lap_Speed':20, 'Duration_Session':30, 'Start_Session':'2:20', 'End_Session':'1:10'})


# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    registered = db.Column(db.String(20))
    avg_lap_completed_time = db.Column(db.Integer)
    avg_speed = db.Column(db.Integer)
    fastest_lap_time  = db.Column(db.Integer)
    total_laps_completed = db.Column(db.Integer)
    total_distance_ran = db.Column(db.Integer)
    total_time_spent_running = db.Column(db.Integer)

    def __init__(self, name, registered, avg_lap_completed_time, avg_speed, fastest_lap_time, total_laps_completed, total_distance_ran, total_time_spent_running):
        self.name = name
        self.registered = registered
        self.avg_lap_completed_time = avg_lap_completed_time
        self.avg_speed = avg_speed
        self.fastest_lap_time = fastest_lap_time
        self.total_laps_completed = total_laps_completed
        self.total_distance_ran = total_distance_ran
        self.total_time_spent_running = total_time_spent_running

    def __repr__(self):
        return '<Name %r>' % self.name

# Save user's information to database and send to success page
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
            reg = User(name, registered, alct, avg_speed, fastest_lap_time, tlc, tdr, ttsr)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()