import logging
import os
from datetime import datetime

#datetime.now() : give real time
LOG_FILE=F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #. log file created with date time year
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #set log file path
os.makedirs(log_path,exist_ok=True) #make directry, it exist then true

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE) #combine log file, log path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

