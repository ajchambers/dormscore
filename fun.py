from jinja2 import Environment, FileSystemLoader
import psycopg2
import psycopg2.extras

conn = None
cur = None

def fetch_dorms_by_university(university):
    
    conn = psycopg2.connect(
        host='localhost',
        dbname='dormscore_v1',
        user='postgres',
        password='coffee',
        port=5432
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT dorm_name, address, url FROM dorm WHERE university = %s", (university,))
    dorms = cur.fetchall()
    conn.close()
    return dorms

def fetch_all_dorms():
   
    conn = psycopg2.connect(
        host='localhost',
        dbname='dormscore_v1',
        user='postgres',
        password='coffee',
        port=5432
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT dorm_name, avg_score FROM dorm")
    all_dorms = cur.fetchall()
    conn.close()
    return all_dorms

def fetch_dorm_data(dorm_name):
    return f'{dorm_name}.html'