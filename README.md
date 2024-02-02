# README

# **General Practices**
- Use of Camel casing for variable, file and function names.
- The variable names must clearly outline what is stored.
- Use of Pascal casing for class names.
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
- **Database** must be initialised by running the dbImport.py file in the root directory.


\`\`\`plantuml

Your PlantUML goes here

\`\`\`

To create a Use Case, put the name of the use case in parentheses.

```plantuml
(Order Book)

```

Alternatively, you can use the keyword 'usecase', but the name needs to be quoted.

```plantuml
(Order Book)
usecase "Search for book"

```

To add an actor, surround a phrase with colons, or use the keyword 'actor' (again quoting the name of the actor)

```plantuml
:Customer:
actor "Delivery Driver"

```

To link an actor to a use case, we place an arrow between the items as " --> "

```plantuml
(Order Book)
usecase "Search for book"
:Customer:
actor "Delivery Driver"

Customer --> (Order Book)

```

To make it easier to form the links, we can put short aliases on use-cases and actors using "as"

```plantuml
(Order Book) as order
usecase "Search for book" as search
:Customer:
actor "Delivery Driver" as driver

Customer --> order


```

