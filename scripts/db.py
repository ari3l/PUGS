import sqlite3
import time

DB_FILE = "db.sqlite"

class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)

    def store(self, domain):
        # Check if domain exists in db
        sql_check = "SELECT * FROM pwds WHERE domain = '" + domain  + "'"
        cur = self.conn.cursor().execute(sql_check)
        timestamp = int(time.time())
        if len(cur.fetchall()) >= 1:
            update_sql = "UPDATE pwds SET timestamp = "+ str(timestamp) + " WHERE domain = '" + domain + "'"
            self.conn.cursor().execute(update_sql)
            self.conn.commit()
        else:
            values = "('%s',%d)" % (domain, timestamp)
            insert_sql = "INSERT INTO pwds (domain, timestamp)  VALUES %s" % values
            self.conn.cursor().execute(insert_sql)
            self.conn.commit()

    def retrieve(self, domain):
        try:
            sql = "SELECT * FROM pwds WHERE domain = '%s'" % domain
            c =  self.conn.cursor().execute(sql)
            rows = c.fetchall()
            return rows[0][2]
        except Exception as e:
            return ""


    def create_db(self):
        create_table = "CREATE TABLE IF NOT EXISTS pwds (id integer PRIMARY KEY, domain VARCHAR(255), timestamp integer)"
        try:
            c = self.conn.cursor()
            c.execute(create_table)
        except Exception as e:
            print(e)
