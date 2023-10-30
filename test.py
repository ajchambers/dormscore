import unittest
import psycopg2
import psycopg2.extras

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = psycopg2.connect(
            host='localhost',
            dbname='dormscore_v1',
            user='postgres',
            password='coffee',
            port=5432
        )
        cls.cur = cls.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_table_creation(self):
        self.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name = 'dorm'")
        self.assertEqual(self.cur.rowcount, 1, "Table 'dorm' not created")

    def test_data_insertion(self):
        self.cur.execute("SELECT COUNT(*) FROM dorm")
        initial_count = self.cur.fetchone()['count']

        # Insert data
        insert_values = [(6, 'new_dorm', 'Test University', 'Test Address', 0, 'test_url', 0)]
        insert_script = 'INSERT INTO dorm (id, dorm_name, university, address, avg_score, url, number_of_reviews) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        for record in insert_values:
            self.cur.execute(insert_script, record)
        self.conn

        self.cur.execute("SELECT COUNT(*) FROM dorm")
        new_count = self.cur.fetchone()['count']
        self.assertEqual(new_count, initial_count + 1, "Data insertion failed")

    def test_data_retrieval(self):
        self.cur.execute("SELECT dorm_name, address FROM dorm WHERE university = 'Central Michigan University'")
        records = self.cur.fetchall()
        self.assertGreaterEqual(len(records), 2, "Data retrieval failed")

if __name__ == '__main__':
    unittest.main()
