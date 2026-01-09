
from flask import request,jsonify
from models import db,UserProfile,UserLocation,Activity,UserActivity
from datetime import datetime

def ReadAll():
    Users = UserProfile.query.all()
    totalInfo = []

    for User in Users:
        UserInfo = {
            "UserID": User.UserID,
            "UserName": User.UserName,
            "FirstName": User.FirstName,
            "SecondName": User.SecondName,
            "Email": User.Email,
            "DOB": User.DOB,
            "Location":[
                {
                    "LocationID": locate.LocationID,
                    "UserID":locate.UserID,
                    "City":locate.UserID,
                    "County":locate.County,
                    "Country":locate.Country,
                    "PostCode":locate.PostCode
                }
                for locate in User.Location
            ],
            "UserActivity":[
                {
                    "UserActivityID": UserA.UserActivity,
                    "UserID": UserA.UserID,
                    "ActivityID":UserA.ActivityID
                }
                for UserA in User.UserActivity
            ]
        }
        totalInfo.append(UserInfo)

    return jsonify(UserInfo)


def ReadUser(UserID):
    Users = UserProfile.query.get(UserID)

    UserInfo = {
            "UserID": Users.UserID,
            "UserName": Users.UserName,
            "FirstName": Users.FirstName,
            "SecondName": Users.SecondName,
            "Email": Users.Email,
            "DOB": Users.DOB,
            "Location":[
                {
                    "LocationID": locate.LocationID,
                    "UserID":locate.UserID,
                    "City":locate.UserID,
                    "County":locate.County,
                    "Country":locate.Country,
                    "PostCode":locate.PostCode
                }
                for locate in User.Location
            ],
            "UserActivity":[
                {
                    "UserActivityID": UserA.UserActivity,
                    "UserID": UserA.UserID,
                    "ActivityID":UserA.ActivityID
                }
                for UserA in User.UserActivity
            ]
        }
    
    return jsonify(UserInfo)


def createNewUser(NewUser):
    User = UserProfile(
        UserID= NewUser["UserID"],
        UserName = NewUser["UserName"],
        FirstName= NewUser["FirstName"],
        SecondName= NewUser["SecondName"],
        Email = NewUser["Email"],
        DOB= NewUser["DOB"],
    )

    db.session.add(User)

    NewLocation = UserLocation(
        LocationId= User["LocationID"],
        UserID = NewUser["UserID"],
        City= NewUser["City"],
        County= NewUser["County"],
        Country= NewUser["Country"],
        PostCode= NewUser["PostCode"]
    )

    db.session.add(NewLocation)
    db.session.commit()


def DeleteUser(UserID):
    User = UserProfile.query.get(UserID)

    if User != None:
        db.session.delete(User)
        db.session.commit()


def DeleteActivity(ActivityID):
    ActivityChoice = Activity.query.get(ActivityID)

    if ActivityChoice != None:
        db.session.delete(ActivityChoice)
        db.session.commit()


def CreateActivity(NewActivity):
    ActivityAdd = Activity(
        ActivityID = NewActivity["ActivityID"],
        ActivityName = NewActivity["ActivityName"],
        ActivityDescription = NewActivity["ActivityDescription"]
    )
    db.session.add(ActivityAdd)
    db.session.commit()

