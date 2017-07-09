#!/usr/bin/env python3
import psycopg2 as p

dbname = "news"

def connect(news):
    try:
        db = p.connect("dbname={}".format(news))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print
        'Unable to connect to database'
        raise e
    db, c = connect()


# Most popular three articles of all time
def query1():
    db = p.connect("dbname='news'")
    cur = db.cursor()
    cur.execute(
        "SELECT title, COUNT(*) AS views_count FROM articles "
        "JOIN log ON articles.slug = (regexp_split_to_array(log.path, E'/article/'))[2] "
        "GROUP BY slug, title ORDER BY views_count DESC LIMIT 3;"
    )

    rows = cur.fetchall()
    print("\nTop 3 Articles")
    for article in rows:
        print "Article: {0}     | {1} views".format(article[0], article[1])


query1()


#  Most popular article authors of all time
def query2():
    db = p.connect("dbname='news'")
    cur = db.cursor()
    cur.execute(
        "SELECT authors.name, COUNT(authors.name) AS views FROM articles "
        "JOIN authors ON authors.id = articles.author "
        "JOIN log ON log.path LIKE '%' || articles.slug "
        "GROUP BY authors.name ORDER BY views DESC;"
    )

    rows = cur.fetchall()
    print("\n\nTop authors")
    for author in rows:
        print "Author name: {0}  | {1} views".format(author[0], author[1])


query2()


# Show on which days did more than 1% of requests lead to errors
def query3():
    db = p.connect("dbname='news'")
    cur = db.cursor()
    cur.execute(
        "SELECT f.date AS date, f.count AS Fail_Req, a.count AS All_Req, "
        "(f.count::float) *100 / (a.count::float) AS percent "
        "FROM fail AS f JOIN total AS a ON f.date = a.date "
        "WHERE (f.count::float) *100 / (a.count::float) > 1 "
        "ORDER BY percent DESC;"
    )

    rows = cur.fetchall()
    print("\n\nErrors in Percent")
    for r in rows:
        print "Date: {0}  | Failed Requests: {1}   | Total Requests: {2} | Error in Percentage: {3}%".format(r[0], r[1], r[2], r[3])


query3()
