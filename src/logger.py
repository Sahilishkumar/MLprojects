import logging
import os
from datetime import datetime

LOG_FILE_PATH = os.path.join(os.getcwd(),"logs")
log_path = os.path.join(LOG_FILE_PATH,datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
os.makedirs(LOG_FILE_PATH,exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging started")
