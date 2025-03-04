<div align= "center">
  <h1>SQL - More queries</h1>
</div>

## General
`How to create a new MySQL user`  
Use the command CREATE USER followed by the username and password.  
`How to manage privileges for a user to a database or table`  
Use the command GRANT to give privileges and REVOKE to remove them.  
`What’s a PRIMARY KEY`  
A PRIMARY KEY is a column that uniquely identifies each record in a table.  
`What’s a FOREIGN KEY`  
A FOREIGN KEY is a column that links two tables by referring to the primary key in another table.  
`How to use NOT NULL and UNIQUE constraints`    
- `NOT NULL`: Ensures a column cannot have a NULL value.  
- `UNIQUE`: Ensures all values in a column are unique.

`How to retrieve data from multiple tables in one request`  
Use JOIN to combine rows from multiple tables based on a related column.

`What are subqueries`  
Subqueries are queries nested inside another query.

`What are JOIN and UNION`
- `JOIN`: Combines rows from two or more tables based on a related column.
- `UNION`: Combines the results of two or more SELECT queries into a single result set.

## Requirements

- Allowed editors: `vi, vim, emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT, WHERE`…)
- A `README.md file`, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## Exercices

| Filename | Description |
| -------- | ----------- |
| `0. List databases` | Lists all databases of your MySQL server.|
| `1. Create a database` | Creates the database hbtn_0c_0 in your MySQL server.|
| `2. Delete a database` | Deletes the database hbtn_0c_0 in your MySQL server..|
| `3. List tables` | Lists all the tables of a database in your MySQL server..|
| `4. First table` | Creates a table called first_table in the current database in your MySQL server.|
| `5. Full description` | Prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.|
| `6. List all in table ` | Lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. |
| `7. First add ` | Inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. |
| `8. Count 89 ` | Displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.|
| `9. Full creation` | Creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.|
| `10. List by best ` | Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.|
| `11. Select the best ` | Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| `12. Cheating is bad ` | Updates the score of Bob to 10 in the table second_table.|
| `13. Score too low ` | Removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| `14. Average ` | Computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.|
| `15. Number by score ` | Lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server. |
| `16. Say my name ` | Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. |



<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
