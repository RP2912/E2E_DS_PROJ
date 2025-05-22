from src.E2E_DS_PROJ.logger import logging
from src.E2E_DS_PROJ.exception import CustomException
from src.E2E_DS_PROJ.componenets.data_ingestion import DataIngestion, DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("execution started")

    try: 
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(str(e),sys)