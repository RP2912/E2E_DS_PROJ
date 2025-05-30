# Database ----> data reading from source ---> train test split

#mysqlworkbench-->traintest split--->dataset

import os
import sys #importing because need to handle custom ecception for logging
from src.E2E_DS_PROJ.exception import CustomException
from src.E2E_DS_PROJ.logger import logging
# we need to import both while creating any module

import pandas as pd
import numpy as np
from src.E2E_DS_PROJ.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            # df=pd.read_csv(os.path.join('notebook/data','raw.csv'))
            df=pd.read_csv(os.path.join('artifacts/notebook/data/raw.csv'))
            logging.info("Reading completed mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )


        except Exception as e:
            raise CustomException(str(e),sys)