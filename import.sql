CREATE TABLE Files(
    FileID text NOT NULL PRIMARY KEY,
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
    Description text,
    isMentor integer,
    awaitingApproval integer,
    ProfilePictureID text REFERENCES Files(FileID),
    BackgroundID text REFERENCES Files(FileID),
    LastLogin integer,
    Created integer
  );

CREATE TABLE Tags (
    TagID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    CreatedBy integer REFERENCES Users(UserID),
    Name text,
    Colour text,
    Created integer
);

CREATE TABLE AssignedTags (
    TagID integer REFERENCES Tags(TagID),
    UserID integer REFERENCES Users(UserID),
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
    ProfilePictureID text REFERENCES Files(FileID),
    BackgroundID text REFERENCES Files(FileID),
    isCompany integer,
    isApproved integer,
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
    isEntity integer,
    Created integer
);

CREATE TABLE Transactions (
    TransactionID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    TokenID text REFERENCES Tokens(TokenID),
    SenderID integer,
    isSenderEntity integer,
    ReceiverID integer,
    isReceiverEntity integer,
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