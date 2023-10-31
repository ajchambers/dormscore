import psycopg2
import psycopg2.extras

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host='localhost',
        dbname='dormscore_v1',
        user='postgres',
        password='coffee',
        port=5432
    )

    def create_dorm_table(conn):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('drop table if exists dorm')

        create_script = ''' create table if not exists dorm(
                            id  serial primary key,
                            dorm_name text not null,
                            university text not null,
                            address text,
                            avg_score int,
                            url text,
                            number_of_reviews int)'''

        cur.execute(create_script)

    def insert_dorm_records(conn, records):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        insert_script = 'INSERT INTO dorm (dorm_name, university, address, avg_score, url, number_of_reviews) VALUES(%s, %s, %s, %s, %s, %s)'

        for record in records:
            cur.execute(insert_script, record)

    def fetch_dorms_by_university(conn, university):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT dorm_name, address FROM dorm WHERE university = %s", (university,))
        return cur.fetchall()

    def fetch_all_dorms(conn):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM dorm")
        return cur.fetchall()

    create_dorm_table(conn)

    insert_values = [
        ('emmons', 'Central Michigan University', '500 Ojibway Ct, Mt Pleasant, MI 48858', 0, 'https://www.cmich.edu/student-life/housing/living-on-campus/housing-communities/east-community', 0),
        ('herring', 'Central Michigan University', '403 E Broomfield St, Mt Pleasant, MI 48858', 0, 'https://www.cmich.edu/student-life/housing/living-on-campus/housing-communities/east-community', 0),
        ('saxe', 'Central Michigan University', 'Saxe Hall, Mt Pleasant, MI 48858', 0, 'https://www.cmich.edu/student-life/housing/living-on-campus/housing-communities/east-community', 1)
    ]

    insert_dorm_records(conn, insert_values)

    university = 'Central Michigan University'
    dorms = fetch_dorms_by_university(conn, university)
    for record in dorms:
        print(record)

    all_dorms = fetch_all_dorms(conn)
    for record in all_dorms:
        print(record['dorm_name'], record['avg_score'])

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
