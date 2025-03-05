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
| `0. My privileges!` | Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost). |
| `1. Root user` | Creates the MySQL server user user_0d_1. |
| `2. Read user` | Creates the database hbtn_0d_2 and the user user_0d_2. |
| `3. Always a name` | Creates the table force_name on your MySQL server. |
| `4. ID can't be null` | Creates the table id_not_null on your MySQL server. |
| `5. Unique ID` | Creates the table unique_id on your MySQL server. |
| `6. States table` | Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. |
| `7. Cities table` | Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server. |
| `8. Cities of California` | Lists all the cities of California that can be found in the database hbtn_0d_usa. |
| `9. Cities by States` | Lists all cities contained in the database hbtn_0d_usa. |
| `10. Genre ID by show` | Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. |
| `11. Genre ID for all shows` | Lists all shows contained in the database hbtn_0d_tvshows. |
| `12. No genre` | Lists all shows contained in hbtn_0d_tvshows without a genre linked. |
| `13. Number of shows by genre` | Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. |
| `14. My genres` | Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. |
| `15. Only Comedy` | Lists all Comedy shows in the database hbtn_0d_tvshows. |
| `16. List shows and genres` | Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. |

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
