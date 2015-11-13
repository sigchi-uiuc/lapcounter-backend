import datetime
from app import db

# Create table of users on database 
class User(db.Model):
    __tablename__ = "users_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    registered = db.Column(db.String(20))
    data_id = db.Column(db.Integer, db.ForeignKey('data_table.id'))
    # define relationship
    data = db.relationship('Data', uselist=False, backref="users_table")


    def __init__(self, name, registered, data):
        self.name = name
        self.registered = registered
        self.data = data

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
    avg_lap_completed_time = db.Column(db.Integer)
    avg_speed = db.Column(db.Integer)
    fastest_lap_time  = db.Column(db.Integer)
    total_laps_completed = db.Column(db.Integer)
    total_distance_ran = db.Column(db.Integer)
    total_time_spent_running = db.Column(db.Integer)

    def __init__(self, avg_lap_completed_time, avg_speed, fastest_lap_time, total_laps_completed, total_distance_ran, total_time_spent_running):
        self.avg_lap_completed_time = avg_lap_completed_time
        self.avg_speed = avg_speed
        self.fastest_lap_time = fastest_lap_time
        self.total_laps_completed = total_laps_completed
        self.total_distance_ran = total_distance_ran
        self.total_time_spent_running = total_time_spent_running

    def __repr__(self):
        return '<id %r>' % self.id

    @property
    def serialize(self):
        return {'avg_lap_completed_time' : self.avg_lap_completed_time, 'avg_speed': self.avg_speed, 
        'fastest_lap_time': self.fastest_lap_time, 'total_laps_completed': self.total_laps_completed, 
        'total_distance_ran': self.total_distance_ran, 'total_time_spent_running': self.total_time_spent_running}
