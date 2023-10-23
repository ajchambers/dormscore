import psycopg2
import psycopg2.extras


conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'dormscore_v1',
        user = 'postgres',
        password = 'coffee',
        port = 5432)
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('drop table if exists dorm')

    create_script = ''' create table if not exists dorm(
                                        id  int primary key,
                                        dorm_name text not null,
                                        university text not null,
                                        address text,
                                        avg_score int,
                                        url text,
                                        number_of_reviews int)'''

    cur.execute(create_script)

    insert_script = 'INSERT INTO dorm (id, dorm_name, university, address, avg_score, url, number_of_reviews) VALUES(%s, %s, %s, %s, %s, %s, %s)'

    insert_values = [(1, 'example_dorm', 'Central Michigan University', '123 University Drive, Mount Pleasant, MI', 4.3, 'https://www.google.com', 451), (2, 'example_dorm2', 'Central Michigan University', '543 University Drive, Mount Pleasant, MI', 1.3, 'https://www.google.com', 12)]

    for records in insert_values:
        cur.execute(insert_script, records)



    cur.execute('select * from dorm')

    for record in cur.fetchall():
        print(record)

    #uses dictionary to fetch by column name
    for record in cur.fetchall():
        print(record['dorm_name'], record['avg_score'])
    



    conn.commit()


    

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


