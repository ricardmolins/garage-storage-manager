from psycopg2 import sql
import psycopg2
import yaml

VAULT_OBJECT_ID = 1
HOME_OBJECT_ID = 2

DB_OBJECT_ID_INDEX = 0
DB_OBJECT_NAME_INDEX = 1

"""
CREATE TABLE objects (
    object_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    parent_object_id INT REFERENCES objects(object_id) -- self-referencing foreign key
);
"""

def GetObjectsInId(object_id):
    """
    Returns a list of objects in the given object_id
    """
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            SELECT
                object_id,
                name,
                parent_object_id
            FROM
                objects
            WHERE
                parent_object_id = %s
        """)
        cursor.execute(query, (object_id,))

        # Get all the results from the query
        result = cursor.fetchall()

    return result

def GetObjectsById(object_id):
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            SELECT
                object_id,
                name,
                parent_object_id
            FROM
                objects
            WHERE
                object_id = %s
        """)
        cursor.execute(query, (object_id,))
        result = cursor.fetchone()

    return result

def GetObjectsInVault():
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            SELECT
                object_id,
                name
            FROM
                objects
            WHERE
                parent_object_id = %s
        """)
        cursor.execute(query, (VAULT_OBJECT_ID,))

        # Get all the results from the query
        result = cursor.fetchall()

    return result

def AddObjectToVault(object_name):
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            INSERT INTO
                objects
                (name, parent_object_id)
            VALUES
                (%s, %s)
        """)
        cursor.execute(query, (object_name, VAULT_OBJECT_ID))

    connection.commit()

def DeleteObjectFromVault(object_id):
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            DELETE FROM
                objects
            WHERE
                object_id = %s
        """)
        cursor.execute(query, (object_id,))

    connection.commit()

def EditObject(object_id, object_name):
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            UPDATE
                objects
            SET
                name = %s
            WHERE
                object_id = %s
        """)
        cursor.execute(query, (object_name, object_id))

    connection.commit()

def GetNameOfObject(object_id):
    with connection.cursor() as cursor:
        # Using a parameterized query to avoid SQL injection
        query = sql.SQL("""
            SELECT
                name
            FROM
                objects
            WHERE
                object_id = %s
        """)
        cursor.execute(query, (object_id,))
        result = cursor.fetchone()

    return result[0]

# Read the database connection parameters from the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

db_params = {
        'host': config['host'],
        'database': config['database'],
        'user': config['user'],
        'password': config['password'],
    }

 # Replace these with your PostgreSQL connection details

connection = None
try:
    connection = psycopg2.connect(**db_params)

except psycopg2.Error as e:
    print(f"Error: {e}")





 