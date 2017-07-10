# Udacity Log Analaysis Project

### Requirments
1. Install [Vagrant](https://www.vagrantup.com/downloads.html "vagrant") and [VirtualBox](https://www.virtualbox.org/wiki/Downloads "VirtualBox").


### Steps
1. Start Vagrant and run `vagrant up` to download  the Linux file systems.
2. Log in to Vagrant by `vagrant ssh`.
3. Install [Python3](https://www.python.org/downloads/ "Python3").
4. Install [PostgreSQL](https://www.postgresql.org/download/ "PostgreSQL").
5. Install [Psycopg2] (http://initd.org/psycopg/download/ "Psycopg").
6. Download the database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.).
7. Unzip the database file.
8. Connect to the database by `psql -d news -f newsdata.sql`

### How tp run the program?
- Run `python3 newsdata.py`

### About the project
This is project is for Udacity Full Stack Nanoegree and we are required to solve 3 problems in order to finish this project.

#### Query 1
What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

#### Query 2
Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

#### Query 3
On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.

**Create Views Statments**

`CREATE VIEW fail AS SELECT date(time), COUNT(status) FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time);`
`SELECT f.date AS date, f.count AS Fail_Req, a.count AS All_Req FROM fail AS f JOIN total AS a ON f.date = a.date;`

