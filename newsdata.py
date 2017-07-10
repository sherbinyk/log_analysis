#!/usr/bin/env python3
import psycopg2 as p


def connect(news):
    try:
        db = p.connect("dbname={}".format(news))
        cur = db.cursor()
        return db, cur
    except psycopg2.Error as e:
        print
        'Unable to connect to database'
        raise e


def query1():
    """Most popular three articles of all time"""
    db, cur = connect('news')
    cur.execute(
        "SELECT title, COUNT(*) AS views_count FROM articles "
        "JOIN log ON "
        "articles.slug = (regexp_split_to_array(log.path, E'/article/'))[2] "
        "GROUP BY slug, title ORDER BY views_count DESC LIMIT 3;"
    )

    rows = cur.fetchall()
    print("\nTop 3 Articles")
    for article in rows:
        print("Article: {0}     | {1} views"
              .format(article[0], article[1])
              )


def query2():
    """Most popular article authors of all time"""
    db, cur = connect('news')
    cur.execute(
        "SELECT authors.name, COUNT(authors.name) AS views FROM articles "
        "JOIN authors ON "
        "authors.id = articles.author "
        "JOIN log ON log.path LIKE '%' || articles.slug "
        "GROUP BY authors.name ORDER BY views DESC;"
    )

    rows = cur.fetchall()
    print("\n\nTop authors")
    for author in rows:
        print("Author name: {0}  | {1} views"
              .format(author[0], author[1])
              )


def query3():
    """Show on which days did more than 1% of requests lead to errors"""
    db, cur = connect('news')
    cur.execute(
        "SELECT f.date AS date, "
        "(f.count::float) *100 / (a.count::float) AS percent "
        "FROM fail AS f JOIN total AS a ON f.date = a.date "
        "WHERE (f.count::float) *100 / (a.count::float) > 1 "
        "ORDER BY percent DESC;"
    )

    rows = cur.fetchall()
    print("\n\nErrors in Percent")
    for r in rows:
        print("Date: {0:%B %d, %Y}  | Error in Percentage: {1:.2f}%"
              .format(r[0], r[1])
              )


if __name__ == "__main__":
    query1()
    query2()
    query3()
