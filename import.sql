CREATE TABLE Files(
    FileID int NOT NULL PRIMARY KEY,
    Name text,
    Extension text,
    Created int
    );

CREATE TABLE Users (
    UserID int NOT NULL PRIMARY KEY,
    Name text,
    Username text,
    Email text,
    Password text,
    Salt text,
    isMentor int,
    awaitingApproval int,
    ProfilePictureID int REFERENCES Files(FileID),
    BackgroundID int REFERENCES Files(FileID),
    LastLogin int,
    Created int
  );

CREATE TABLE VerificationCodes (
    UserID int NOT NULL REFERENCES Users(UserID),
    Code text,
    isPasswordCode int,
    Created int
  );

CREATE TABLE SitePermissions (
    UserID int NOT NULL REFERENCES Users(UserID),
    ManageTokens int,
    ManageUsers int,
    ManageReports int,
    Created int
);

CREATE TABLE Entities (
    EntityID int NOT NULL PRIMARY KEY,
    Name text,
    Description text,
    ProfilePictureID int REFERENCES Files(FileID),
    BackgroundID int REFERENCES Files(FileID),
    isCompany int,
    Created int
);

CREATE TABLE EntityMembers (
    EntityID int NOT NULL REFERENCES Entities(EntityID),
    UserID int NOT NULL REFERENCES Users(UserID),
    Role text,
    isAdmin int,
    Created int
);

CREATE TABLE Tokens (
    TokenID text NOT NULL PRIMARY KEY,
    OwnerID int REFERENCES Entities(EntityID),
    OwnerType int,
    Created int
);

CREATE TABLE Transactions (
    TransactionID int NOT NULL PRIMARY KEY,
    TokenID text REFERENCES Tokens(TokenID),
    SenderID int REFERENCES Entities(EntityID),
    ReceiverID int REFERENCES Entities(EntityID),
    isDonation int,
    Created int
);

CREATE TABLE Sessions (
    SessionID int NOT NULL PRIMARY KEY,
    MenteeID int REFERENCES Users(UserID),
    MentorID int REFERENCES Users(UserID),
    isComplete int,
    Notes text,
    Created int
);

CREATE TABLE Reviews (
    ReviewID int NOT NULL PRIMARY KEY,
    SessionID text REFERENCES Sessions(SessionID),
    isSatisfied int,
    Comment text,
    Created int
);