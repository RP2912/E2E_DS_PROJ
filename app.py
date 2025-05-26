from src.E2E_DS_PROJ.logger import logging
from src.E2E_DS_PROJ.exception import CustomException
from src.E2E_DS_PROJ.componenets.data_ingestion import DataIngestion, DataIngestionConfig
from src.E2E_DS_PROJ.componenets.data_transformation import DataTransformation
import sys

if __name__=="__main__":
    logging.info("execution started")

    try: 
        data_ingestion=DataIngestion()
        train_data_path, test_data_path= data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(str(e),sys)