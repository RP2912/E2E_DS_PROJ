import os
import sys
from src.E2E_DS_PROJ.exception import CustomException
from src.E2E_DS_PROJ.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql
import pickle
import numpy as np
from sqlalchemy import create_engine
load_dotenv()


# Load DB credentials from .env
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')



def read_sql_data():
    logging.info("Reading sql database started")
    try:
       mydb=pymysql.connect(
          host=host,
          user=user,

          password=password,
          db=db
       ) 
       engine = create_engine("mysql+pymysql://rinke:pass@localhost/mydb")

       # connecting database from mydb
       logging.info("Connection established",mydb)
       df=pd.read_sql_query("select * from students",mydb)
       print(df.head())


       return df



       pass
    except Exception as ex:
       raise CustomException(str(ex), sys)
   