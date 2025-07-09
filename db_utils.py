import logging
import pymysql

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': '',
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
            timestamps = [fng_data['timestamp'] for fng_data in fng_data_list]
            # Query existing timestamps
            sql_check = "SELECT timestamp FROM index_fear_greed WHERE timestamp IN (%s)" % ','.join(
                ['%s'] * len(timestamps))
            cursor.execute(sql_check, timestamps)
            existing_timestamps = {row[0] for row in cursor.fetchall()}

            # Insert new data that doesn't already exist
            new_data = [
                (fng_data['value'], fng_data['value_classification'], fng_data['timestamp'])
                for fng_data in fng_data_list if fng_data['timestamp'] not in existing_timestamps
            ]
            if new_data:
                sql_insert = "INSERT INTO index_fear_greed (value, value_classification, timestamp) VALUES (%s, %s, %s)"
                cursor.executemany(sql_insert, new_data)
                conn.commit()
                logging.info(f"Successfully inserted {len(new_data)} new records")
            else:
                logging.info("No new data to insert")
    except Exception as e:
        logging.error(f"Database operation failed: {e}")
    finally:
        conn.close()
