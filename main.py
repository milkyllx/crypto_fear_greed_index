from apscheduler.schedulers.blocking import BlockingScheduler
from fetch_utils import fetch_fng_data
from db_utils import save_fng_to_db
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Scheduled task
def job():
    logging.info("Starting task execution...")
    fng_data_list = fetch_fng_data()
    if fng_data_list:
        save_fng_to_db(fng_data_list)
    else:
        logging.warning("Failed to fetch data")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', hours=1)
    logging.info("Scheduler has started. The task will run every hour.")
    try:
        scheduler.start()
    except KeyboardInterrupt:
        logging.info("Scheduler has stopped.")
