<div align= "center">
  <h1>RESTful API</h1>
</div>

### Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

### Learning Objectives:
- HTTP/HTTPS Basics: Grasp the foundational principles of the web’s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.

- API Consumption with Command Line: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.

- API Consumption with Python: Elevate your data fetching skills by leveraging Python’s capabilities, allowing for more advanced processing and data manipulation.

- API Development with http.server: Understand the basics of crafting an API from scratch using Python’s built-in modules, setting a solid foundation.

- API Development with Flask: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.

- API Security & Authentication: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.

- API Standards & Documentation with OpenAPI: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

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
