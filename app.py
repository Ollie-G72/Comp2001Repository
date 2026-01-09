from flask import Flask
from flask_restful import Api

from models import db

from Users import(
    ReadAll,ReadUser,createNewUser,DeleteUser,
    DeleteActivity,CreateActivity
)


import os

app = Flask(__name__)
server = os.environ.get("DB_server",)


@app.route("/api/Users",methods=["GET"])
def GetAllUsers():
    return ReadAll()

@app.route("/api/Users/<int:UserID>",methods=["GET"])
def GetOneUser(UserID):
    return ReadUser(UserID)
    
@app.route("/api/Users",methods=["POST"])
def PostUser(NewUser):
    return createNewUser(NewUser)

@app.route("/api/Users/<int:UserID>",methods=["DELETE"])
def DeleteOneUser(UserID):
    return DeleteUser(UserID)

@app.route("/api/Users/<int:UserID>",methods=["DELETE"])
def DeleteOneActivity(ActivityID):
    return DeleteActivity(ActivityID)

@app.route("/api/Users/<int:UserID>",methods=["POST"])
def PostActivity(ActivityID):
    return CreateActivity(ActivityID)





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)