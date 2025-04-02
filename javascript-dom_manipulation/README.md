<div align= "center">
  <h1>JavaScript DOM manipulation</h1>
</div>


# General

`How to select HTML elements in JavaScript`  
Use document.querySelector() for selecting a single element or document.querySelectorAll() for multiple elements.

`What are the differences between ID, class, and tag name selectors?`  
 ID selectors target unique elements, class selectors apply to multiple elements sharing the same class, and tag name selectors target all elements of a specific type (e.g., <div>).

`How to modify the style of an HTML element`  
 Use the style property to set or update CSS styles of an element.

`How to retrieve and update the content of an HTML element`  
 Use innerHTML to get or set the HTML content of an element.

`How to modify the DOM `  
Add, Remove, or change elements using methods like appendChild() or removeChild().

`How to make a request using XmlHTTPRequest`  
 Create an instance of XMLHttpRequest, open a connection, send the request, and handle the response in the onreadystatechange event.

`How to make a request using the Fetch`  
 API Use the fetch() function to send an HTTP request and handle the response with Promises.

`How to listen/bind to DOM events`  
 Use addEventListener() to attach an event handler to an element or the document.

`How to listen/bind to user events Bind event listeners like`  
 click, keydown, or submit to elements using addEventListener().



# Requirements 

#### Python Scripts

- Allowed editors: All of them.
- All your files will be interpreted on Chrome browser (version 57.0 or later)
- All your files should end with a new line
- A mandatory `README.md` file with meaningful information about the content, should be placed at the root folder of the project.
- Your code should be `semistandard` compliant
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…



# Exercices

| Filename | Description |
| -------- | ----------- |
|`0. Color Me`|Create a JavaScript script that changes the header element's text color to red (#FF0000) using document.querySelector to select the HTML element.|
|`1. Click and turn red`|Create a JavaScript script that changes the header element's text color to red (#FF0000) upon clicking the element with the id "red_header". Use document.querySelector() and add a click event listener.|
|`2. Add ".red" class`|Create a JavaScript script that adds the class red to the header element when the user clicks on the tag with id red_header.|
|`3. Toggle classes`|Create a JavaScript script that toggles the class of the <header> element between red and green when the user clicks on the element with the id="toggle_header". The <header> must always have one of these two classes, never both or none.|
|`4. List of elements`|Create a JavaScript script that adds a <li> element to the <ul> list with class my_list when the user clicks on the element with id="add_item". The new element should be <li>Item</li>.|
|`5. Change the text`|Create a JavaScript script that changes the text of the <header> element to "New Header!!!" when the user clicks on the element with the id="update_header".|
|`6. Star wars character`|Create a JavaScript script that uses the Fetch API to retrieve the character name from the URL https://swapi-api.hbtn.io/api/people/5/?format=json. Display the retrieved name in the HTML tag with id="character".|
|`7. Star Wars movies`|Create a JavaScript script that uses the Fetch API to retrieve and list the titles of all movies from https://swapi-api.hbtn.io/api/films/?format=json. The titles should be added as <li> elements to the <ul> element with the id="list_movies".|
|`8. Say Hello!`|Create a JavaScript script that fetches data from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello (translated to French) in the HTML element with id="hello". The script must be compatible with being imported from the <head> tag.|

<br>

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
