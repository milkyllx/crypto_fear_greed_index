import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetch Fear and Greed Index data
def fetch_fng_data():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    url = 'https://api.alternative.me/fng/'
    params = {'limit': 1, 'format': 'json'}
    try:
        response = session.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            logging.info("Successfully fetched Fear and Greed Index data")
            return data['data']
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
    except Exception as e:
        logging.error(f"Unknown error: {e}")
    return None
