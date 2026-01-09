# Comp2001Repository
Repository for Comp2001 Report

A RESTful API microservice using Flask and SQLAlchemy for managing a profile for a trail service that manages user data, such as usernames, location, other personal information and their prefereed activites wether that be hiking, mountain biking , etc.

Includes DOCKER support,
database relationship using SQLAlchemy
CRUD operations for main UserProfile information, User location and Activites.

Uses:
Flask == 3.0.0
Flask-RESTFUL==0.3.10
FLASK-SQLAlchemy==3.1.1
pyodbc==5.0.1
python-dateutil==2.8.2

API Methods:
GET /api/Users (for all UserData with their locations and activities)
GET /api/Users/<UserID> (For a specific User)
POST /api/Users (Creates New User)
DELETE /api/Users/<UserID> (Deletes User)

POST /api/Activites (Adds new Activity)
DELETE /api/Activities (Deletes Activity)


