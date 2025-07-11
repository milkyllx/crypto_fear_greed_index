# Fear and Greed Index Project Installation and Run Guide

This document will guide you on how to install and run the project. The project is designed to fetch Fear and Greed Index data from an external API, store it in a local database, and support scheduled tasks for periodic data updates.

---

## System Requirements

1. **Operating System**: Supports Windows, Linux, or macOS.
2. **Python Version**: Python 3.8 or later is recommended.
3. **Database**: MySQL 5.7 or later.
4. **Network Access**: Requires access to `https://api.alternative.me/fng/`.

---

## Installation Steps

### 1. Clone the Project
Use the following commands to clone the project to your local machine:
```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

**Note**: If the project does not include a `requirements.txt` file, manually install the following dependencies:
```bash
pip install pymysql requests apscheduler
```

### 4. Configure the Database
#### 4.1 Create the Database
Run the following SQL command in MySQL to create the database:
```sql
CREATE DATABASE crypto_bot CHARACTER SET utf8 COLLATE utf8_general_ci;
```

#### 4.2 Create the Table
Run the following SQL script to create the required table:
```sql
CREATE TABLE `index_fear_greed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(10) NOT NULL,
  `value_classification` varchar(50) NOT NULL,
  `timestamp` bigint(20) NOT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `timestamp` (`timestamp`)
);
```

#### 4.3 Configure Database Connection
Edit the `db_utils.py` file in the project and ensure the `DB_CONFIG` settings are correct:
```python
DB_CONFIG = {
    'host': 'localhost',          # Database host
    'user': 'root',               # Database username
    'password': '<YOUR_PASSWORD>',  # Database password
    'database': 'crypto_bot',  # Database name
    'charset': 'utf8'             # Character set
}
```

---

## Running the Project

### 1. Run Data Fetch Manually
Run the following command to manually fetch data and store it in the database:
```bash
python main.py
```

### 2. Start the Scheduled Task
The project is configured to fetch data every hour and store it in the database. Use the following command to start the scheduled task:
```bash
python main.py
```

Once the scheduler starts, you will see the following log message:
```
Scheduler has started. The task will run every hour.
```

---

## Project Structure

- **db.txt**: Contains the database table schema.
- **db_utils.py**: Database utility for connecting and saving data to the database.
- **fetch_utils.py**: Utility for fetching Fear and Greed Index data from the external API.
- **main.py**: Main entry point for the project, including logic for scheduled tasks and manual execution.

---

## FAQ

### 1. Database Connection Failed
**Solution**:
- Ensure the MySQL service is running.
- Verify the `DB_CONFIG` settings in `db_utils.py`.
- Ensure the user has access rights to the `crypto_follow` database.

### 2. Data Fetch Failed
**Solution**:
- Check if the network connection is stable.
- Verify that `https://api.alternative.me/fng/` is accessible.

### 3. Scheduled Task Not Running
**Solution**:
- Check the log output for error messages.
- Ensure the terminal running the script has not been closed.

---

## Conclusion

Following the steps above, you should be able to successfully install and run the project. If you encounter any issues, feel free to contact the developer or submit an issue to the project's GitHub repository.
If you have any questions, please contact me: milkyllx2020@gmail.com


