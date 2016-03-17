from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
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
    user = db.session.query(User).filter(User.name == input_users).one()
    data= db.session.query(Data).filter(User.id == user.id);
    return jsonify(data.serialize)

@app.route('/info/data'):
def all_data():
    data = Data.query.all()
    results = [ data.as_dict() for datam in data ]
    return jsonify({'results': results})

#return all information of a specific running session
@app.route('/session/info')
def session_info():
    return jsonify({ 'Average_Lap_Speed':100 ,'Fastest_Lap_Speed':20, 'Duration_Session':30, 'Start_Session':'2:20', 'End_Session':'1:10'})


@app.route('/api/<name>/<registered>/<start>/<end>',methods=['POST'])
def api(name, registered, start, end):
    if request.method == 'POST':
        duration = int(start)-int(end)
        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.name == name).count():
            reg_user = User(name,registered)
            reg_data = Data(start, end, duration, reg_user)
            db.session.add(reg_user)
            db.session.add(reg_data)
            db.session.commit()
            return render_template('success.html')
        else:
            reg_user = db.session.query(User).filter(User.name == name).one()
            reg_data = Data(start, end, duration, reg_user)
            db.session.add(reg_data)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

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
        start = int(request.form['start'])
        end = int(request.form['end'])
        duration = start-end
        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.name == name).count():
            reg_user = User(name, registered)
            reg_data = Data(start, end, duration, reg_user)
            db.session.add(reg_user)
            db.session.add(reg_data)
            db.session.commit()
            return render_template('success.html')
        else:
            reg_user = db.session.query(User).filter(User.name == name).one()
            reg_data = Data(start, end, duration, reg_user)
            db.session.add(reg_data)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

class User(db.Model):
    __tablename__ = "users_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    registered = db.Column(db.String(20))


    def __init__(self, name, registered):
        self.name = name
        self.registered = registered

    def __repr__(self):
        return '<Name %r>' % self.name

    def as_dict(self):
        obj_d = {
            'id': self.id,
            'name': self.name,
        }
        return obj_d

#Create table of user's data on database
class Data(db.Model):
    __tablename__ = "data_table"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    user = db.relationship('User', uselist=False, backref="data_table")

    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    duration  = db.Column(db.Integer)

    def __init__(self, start, end , duration, user):
        self.start = start
        self.end = end
        self.duration = duration
        self.user = user;

    def __repr__(self):
        return '<id %r>' % self.id

    @property
    def serialize(self):
        return {'user_id':self.user_id, 'start':self.start, 'end':self.end, 'duration':self.duration}


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
