import logging
import os
from datetime import datetime

# 1. Generate a unique log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create a 'logs' directory path inside the current working directory
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# 3. Define the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 4. Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")
    