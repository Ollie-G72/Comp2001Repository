CREATE SCHEMA CW2;
GO

CREATE TABLE CW2.UserProfile(
    UserID INT NOT NULL UNIQUE,
    UserName VARCHAR(50) NOT NULL UNIQUE,
    FirstName VARCHAR(20) NOT NULL,
    SecondName VARCHAR(20) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    DOB DATE NOT NULL,
    UserHeight DECIMAL(5,2),
    UserWeight DECIMAL(5,2),
    UnitPreference BIT,
    PRIMARY KEY(UserID),
);

CREATE TABLE CW2.UserLocation(
    LocationID INT NOT NULL UNIQUE,
    UserID INT NOT NULL,
    City VARCHAR(100) NOT NULL,
    County VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostCode VARCHAR(20) NOT NULL,
    PRIMARY KEY(LocationID),
    FOREIGN KEY(UserID) REFERENCES CW2.UserProfile(UserID),
);

CREATE TABLE CW2.Activites(
    ActivityID INT NOT NULL UNIQUE,
    ActivityName VARCHAR(100) NOT NULL,
    ActivityDescription VarCHar(255),
    PRIMARY KEY (ActivityID),
);

CREATE TABLE CW2.UserActivites(
    UserActivityID INT NOT NULL UNIQUE,
    UserID INT NOT NULL,
    ActivityID INT NOT NULL,
    PRIMARY KEY (UserActivityID),
    FOREIGN KEY(UserID) REFERENCES CW2.UserProfile(UserID),
    FOREIGN KEY(ActivityID) REFERENCES CW2.Activites(ActivityID),
);