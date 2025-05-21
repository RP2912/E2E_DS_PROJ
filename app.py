from src.E2E_DS_PROJ.logger import logging
from src.E2E_DS_PROJ.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("execution started")

    try: 
        a=1/10
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)