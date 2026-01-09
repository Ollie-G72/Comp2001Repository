from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = "UserProfile"
    __table_args__ = {"schema":"CW2"}

    UserID = db.Column(db.Integer,primary_key=True,nullable=False)
    UserName = db.Column(db.String(50),unique=True,nullable=False)
    FirstName = db.Column(db.String(20),nullable=False)
    SecondName = db.Column(db.String(20),nullable=False)
    Email = db.Column(db.String(50),nullable=False)
    DOB = db.Column(db.Date,nullable=False)
    UserHeight = db.Column(db.Numeric(5,2))
    UserWeight = db.Column(db.Numeric(5,2))
    UnitPreference = db.Column(db.Boolean)

    Locations = db.relationship("UserLocation",back_populates="user")
    UsersActivities = db.relationship("UserActivity",back_populates="user")

class UserLocation(db.Model):
    __tablename__ = "UserLocation"
    __table_args__ = {"schema":"CW2"}

    LocationID = db.Column(db.Integer,primary_key=True,nullable=False)
    UserID = db.Column(db.Integer,db.ForeignKey("CW2.UserProfile.UserID"),nullable=False)
    City = db.Column(db.String(100),nullable=False)
    County = db.Column(db.String(100),nullable=False)
    Country = db.Column(db.String(100),nullable=False)
    PostCode = db.Column(db.String(20),nullable=False)

    user = db.relationship("UserProfile",back_populates="Locations")

class Activity(db.Model):
    __tablename__ = "Activites"
    __table_args__ = {"schema":"CW2"}

    ActivityID = db.Column(db.Integer,primary_key=True,nullable=False)
    ActivityName = db.Column(db.String(100),nullable=False)
    ActivityDescription = db.Column(db.String(100))

    UserChoice = db.relationship("UserActivity",back_populates="ActivityChoice")

class UserActivity(db.Model):
    __tablename__ = "UserActivites"
    __table_args__ = {"schema":"CW2"}

    UserActivityID = db.Column(db.Integer,primary_key = True,nullable=False)
    UserID = db.Column(db.Integer,db.ForeignKey("CW2.UserProfile.UserID"),nullable=False)
    ActivityID = db.Column(db.Integer,db.ForeignKey("CW2.Activites.ActivityID"),nullable=False)

    user = db.relationship("UserProfile",back_populates="UsersActivities")
    ActivityChoice = db.relationship("Activity",back_populates="UserChoice")

    