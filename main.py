from apscheduler.schedulers.blocking import BlockingScheduler
from fetch_utils import fetch_fng_data
from db_utils import save_fng_to_db
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_and_save(limit):
    logging.info("fetch and save ")
    fng_data_list = fetch_fng_data(limit)
    if fng_data_list:
        save_fng_to_db(fng_data_list)
    else:
        logging.warning("Failed to fetch data")

# Scheduled task
def job():
    fetch_and_save(1)

if __name__ == '__main__':
    fetch_and_save(10000)
    scheduler = BlockingScheduler()

    scheduler.add_job(job, 'interval', hours=1)
    logging.info("Scheduler has started. The task will run every hour.")
    try:
        scheduler.start()
    except KeyboardInterrupt:
        logging.info("Scheduler has stopped.")
