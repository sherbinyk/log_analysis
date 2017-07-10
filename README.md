# Udacity Log Analaysis Project

### Requirments
1. Install Python3
2. Install Psycopg2

### How tp run the program?
- Run newsdata.py

### About the project
This is project is for Udacity Full Stack Nanoegree and we are required to solve 3 problems in order to finish this project.

#### Query 1
What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

#### Query 2
Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

#### Query 3
On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.

**Create Views Statments**

`CREATE VIEW server_not_found AS SELECT date(time), COUNT(status) FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time);`

`CREATE VIEW total AS SELECT date(time), COUNT(status) FROM log GROUP BY date(time);`

`SELECT f.date AS date, f.count AS Fail_Req, a.count AS All_Req FROM fail AS f JOIN total AS a ON f.date = a.date;`