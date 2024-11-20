import psycopg2


class ConnectionDB:
    @staticmethod
    def connect_db():
        connection_params = {"dbname": "inventory_db",
                             "port": "5432",
                             "user": "postgres",
                             "host": "localhost",
                             "password": "12345"}
        conn = psycopg2.connect(**connection_params)
        conn.autocommit = True
        return conn

    @staticmethod
    def execute_query(query):
        cursor = ConnectionDB.connect_db().cursor()
        cursor.execute(query)
        return cursor