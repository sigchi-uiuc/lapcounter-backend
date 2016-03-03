from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True;
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
    start = None
    end = None
    duration = None
    if request.method == 'POST':
        name = request.form['name']
        registered = request.form['registered']
        start = request.form['start']
        end = request.form['end']
        duration = start - end

        # # Check that name does not already exist (not a great query, but works)
        # if not db.session.query(User).filter(User.name == name).count():
        lap = Lap(start= start, end= end, duration=end)
        user = User(name=name, registered=registered, laps=[lap])
        print lap
        print user
        db.session.add(user)
        db.session.add(lap)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')

# Create table of users on database
class User(db.Model):
    # __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    registered = db.Column(db.String(20))
    laps = db.relationship("Lap", backref='user', lazy='dynamic')

    def __init__(self, name, registered):
        self.name = name
        self.registered = registered

    def __repr__(self):
        return '<Name %r>' % self.name

class Lap(db.Model):
    # __tablename__ = "laps"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    def __init__(self, start, end , duration):
        self.start = start
        self.end = end
        self.duration = duration;

    def __repr__(self):
        return '<id %r>' % self.id


if __name__ == '__main__':
    app.debug = True
    app.run()
