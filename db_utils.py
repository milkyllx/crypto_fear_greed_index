import logging
import pymysql

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': '',
    'charset': 'utf8'
}

# Create database connection
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# Save Fear and Greed Index data to the database
def save_fng_to_db(fng_data_list):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # 去重数据，确保唯一性
            unique_data = {fng_data['timestamp']: fng_data for fng_data in fng_data_list}
            new_data = list(unique_data.values())

            if new_data:
                sql_insert = """
                    INSERT INTO index_fear_greed (value, value_classification, timestamp)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                        value = VALUES(value),
                        value_classification = VALUES(value_classification)
                """
                insert_values = [
                    (fng_data['value'], fng_data['value_classification'], fng_data['timestamp'])
                    for fng_data in new_data
                ]
                cursor.executemany(sql_insert, insert_values)
                conn.commit()
                logging.info(f"Successfully inserted or updated {len(insert_values)} records")
            else:
                logging.info("No new data to insert")
    except Exception as e:
        logging.error(f"Database operation failed: {e}")
    finally:
        conn.close()
