from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.logger.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo

from typing import List

from dotenv import load_dotenv
load_dotenv()

Mongo_DB_URL=os.getenv("MONGO_DB_URL")
print(Mongo_DB_URL)

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        try:
            self.config=config
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
        
    def export_collection_as_dataframe(self):
        try:
            self.data=pd.read_csv(self.config.file_path)
            return self.data
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        