import psycopg2
from config import DB_PARAMS
import logging
import psycopg2.extras

def create_db():
    try:
        connection = psycopg2.connect(user= DB_PARAMS["user"],
                                      password= DB_PARAMS["password"],
                                      host= DB_PARAMS["host"],
                                      port= DB_PARAMS["port"],
                                      database= DB_PARAMS["default_database"])
        connection.autocommit = True
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        logging.debug(connection.get_dsn_parameters())

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        logging.debug("You are connected to - " + str(record))

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname =  '" + DB_PARAMS["database"] + "'")
        exists = cursor.fetchone()
        if not exists:
            sql_create_database="create database " + DB_PARAMS["database"] + ";"
            cursor.execute(sql_create_database)

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        logging.error("Error while connecting to PostgreSQL" + error)


def create_tables():
    try:
        connection = psycopg2.connect(user= DB_PARAMS["user"],
                                      password= DB_PARAMS["password"],
                                      host= DB_PARAMS["host"],
                                      port= DB_PARAMS["port"],
                                      database= DB_PARAMS["database"])
        connection.autocommit = True
        cursor = connection.cursor()

        sql_drop_table="DROP TABLE IF EXISTS shipment_lines;"
        cursor.execute(sql_drop_table)
        cursor.execute("commit")
        sql_create_table="""
            CREATE TABLE public.shipment_lines (
                    shipment_id VARCHAR NOT NULL,
                    shipment_date DATE,
                    order_id VARCHAR,
                    order_source VARCHAR,
                    product_code VARCHAR,
                    product_quantity INTEGER
            );
            """
        cursor.execute(sql_create_table)
        connection.commit()
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        logging.error("Error while connecting to PostgreSQL" + error)


def load_shipping_lines_table(all_shipment_lines):
    connection = psycopg2.connect(user=DB_PARAMS["user"],
                                  password=DB_PARAMS["password"],
                                  host=DB_PARAMS["host"],
                                  port=DB_PARAMS["port"],
                                  database=DB_PARAMS["database"])
    cursor = connection.cursor()

    psycopg2.extras.execute_batch(cursor, """
                                    INSERT INTO shipment_lines VALUES (
                                        %(shipment_id)s,
                                        %(shipment_date)s,
                                        %(order_id)s,
                                        %(order_source)s,
                                        %(product_code)s,
                                        %(product_quantity)s
                                    );
                                """, all_shipment_lines)
    connection.commit()
    cursor.close()
    connection.close()

def main():
    logging.basicConfig(level=logging.DEBUG)
    create_db()
    create_tables()

if __name__ == "__main__":
    main()