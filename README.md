# README

# **General Practices**
- Use of Camel casing for variable names.
- The variable names must clearly outline what is stored.
- Use of Pascal casing for class and function names.
- {{Header | safe}} must be added to the the top of each html page for the navigation menu.
- {{Footer | safe}} must be added to the bottom of each html page for the footer.

# **File Paths**
- `~/data/example.py` for the python datahelper, e.g. searching/sorting algorithms.
- `~/logic/example.py` for all other python classes and functions.
- `~/blueprints/example.py` for all Flask blueprints for routes.
- `~/templates/example.html` for all html templates that are loaded with Flask.
- `~/static/styles/example.css` for css files to be served.
- `~/static/scripts/example.js` for javascript files to be served.
- `~/static/images/example.png` for images to be served.
- `~/static/uploads/example.js` for files that are uploaded by users.
- `~/snippets/example.html` for files that are stored for Flask to access. e.g. navbar varients
- `~/data/..` for stored user data (database, cache, etc).

# **App Configuration**
For the app to work successfully, the following must be done:
- The appsettings.json file must be created in the root directory.
- The file should use the template in the appsettings.Example.json file which is located in the root directory.
- For SMTP credentials the related fields can be left blank the server will instead:
  - Print out the email to the console.