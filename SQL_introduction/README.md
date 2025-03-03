<div align= "center">
  <h1>SQL - Introduction</h1>
</div>

### General
`Database:` Collection of structured information.

`Relational Database:` Stores and accesses related data points.

`SQL:` Structured Query Language.

`MySQL:` Open-source relational database management system.

`Create a Database:` CREATE DATABASE database_name;

`DDL and DML:`

`DDL:` Data Definition Language.

`DML:` Data Manipulation Language.

`Create or Alter a Table:`

`Create:` CREATE TABLE table_name (...);

`Alter:` ALTER TABLE table_name ADD column_name datatype;

`Select Data from a Table:` SELECT column1, column2, ... FROM table_name WHERE condition;

`Insert, Update, or Delete Data:`

`Insert:` INSERT INTO table_name (...) VALUES (...);

`Update:` UPDATE table_name SET ... WHERE condition;

`Delete:` DELETE FROM table_name WHERE condition;

`Subqueries:` Queries nested inside another query.

`MySQL Functions:` Perform operations on data.

# Requirements

- Allowed editors: `vi, vim, emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A `README.md file`, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Basics of HTTP/HTTPS` | Read resources to understand the differences between HTTP and HTTPS, explore the structure of HTTP requests and responses through browser developer tools, and create lists of common HTTP methods and HTTP status codes with their explanations and usage scenarios.|
| `1. Consume data from an API using command line tools (curl)` | Installe curl sur ton système, confirme son installation avec curl --version, utilise-le pour récupérer le contenu de pages web et des données d'API, puis explore l'utilisation des en-têtes et des requêtes POST avec des options telles que -I et -X POST.|
| `2. Consuming and processing data from an API using Python` | Creates a fetch_and_print_posts() function to retrieve and print post titles from JSONPlaceholder, and a fetch_and_save_posts() function to retrieve posts, structure them into dictionaries, and save them to a CSV file.|
| `3.  Develop a simple API using Python with the `http.server` module` |Use the http.server module to create a basic HTTP server, implement the do_GET method to handle GET requests by responding with plain text or JSON data, add a /status endpoint to check the status of the API, and handle errors for undefined endpoints by returning a 404 Not Found response.|
| `4. Develop a Simple API using Python with Flask` | Install Flask, create a Flask web server, define endpoints to serve JSON data and handle POST requests, then test them with a browser or curl.|
| `5. API Security and Authentication Techniques` | Installs Flask-HTTPAuth and Flask-JWT-Extended, configures basic authentication with @auth.login_required, configures JWT token-based authentication with @jwt_required(), and implements role-based access control to protect specific routes.|



<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
