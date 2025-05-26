# import sys
# import os
# sys.path.append(os.path.abspath('./src'))

from src.E2E_DS_PROJ.logger import logging
from src.E2E_DS_PROJ.exception import CustomException
from src.E2E_DS_PROJ.componenets.data_ingestion import DataIngestion, DataIngestionConfig
from src.E2E_DS_PROJ.componenets.data_transformation import DataTransformation
from src.E2E_DS_PROJ.componenets.model_trainer import ModelTrainerConfig, ModelTrainer
# from E2E_DS_PROJ.components.model_trainer import ...



import sys

if __name__=="__main__":
    logging.info("execution started")

    try: 
        data_ingestion=DataIngestion()
        train_data_path, test_data_path= data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        
        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(str(e),sys)