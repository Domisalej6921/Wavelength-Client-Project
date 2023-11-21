CREATE TABLE Users (
    UserID int NOT NULL PRIMARY KEY,
    Name text,
    Email text,
    Password text,
    Salt text,
    ProfilePictureID int,
    BackgroundID int,
    LastLogin int,
    Created int
  );