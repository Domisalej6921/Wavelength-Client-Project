CREATE TABLE Files(
    FileID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name text,
    Extension text,
    Description text,
    Created integer
    );

CREATE TABLE Users (
    UserID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name text,
    Username text,
    Email text,
    Password text,
    Salt text,
    isMentor integer,
    awaitingApproval integer,
    ProfilePictureID integer REFERENCES Files(FileID),
    BackgroundID integer REFERENCES Files(FileID),
    LastLogin integer,
    Created integer
  );

CREATE TABLE VerificationCodes (
    UserID integer NOT NULL REFERENCES Users(UserID),
    Code text,
    isPasswordCode integer,
    Created integer
  );

CREATE TABLE SitePermissions (
    UserID integer NOT NULL REFERENCES Users(UserID),
    ManageTokens integer,
    ManageUsers integer,
    ManageReports integer,
    Created integer
);

CREATE TABLE Entities (
    EntityID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name text,
    Description text,
    ProfilePictureID integer REFERENCES Files(FileID),
    BackgroundID integer REFERENCES Files(FileID),
    isCompany integer,
    Created integer
);

CREATE TABLE EntityMembers (
    EntityID integer NOT NULL REFERENCES Entities(EntityID),
    UserID integer NOT NULL REFERENCES Users(UserID),
    Role text,
    isAdmin integer,
    Created integer
);

CREATE TABLE Tokens (
    TokenID text NOT NULL PRIMARY KEY,
    OwnerID integer REFERENCES Entities(EntityID),
    OwnerType integer,
    Created integer
);

CREATE TABLE Transactions (
    TransactionID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    TokenID text REFERENCES Tokens(TokenID),
    SenderID integer REFERENCES Entities(EntityID),
    ReceiverID integer REFERENCES Entities(EntityID),
    isDonation integer,
    Created integer
);

CREATE TABLE Sessions (
    SessionID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    MenteeID integer REFERENCES Users(UserID),
    MentorID integer REFERENCES Users(UserID),
    isComplete integer,
    Notes text,
    Created integer
);

CREATE TABLE Reviews (
    ReviewID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    SessionID text REFERENCES Sessions(SessionID),
    isSatisfied integer,
    Comment text,
    Created integer
);