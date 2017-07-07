import psycopg2 as p


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
    for r in rows:
        print(r)


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
    print("\n\nTop 3 authors")
    print("Author         |articles        |views")
    for r in rows:
        print(r)


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
        print(r)


query3()
