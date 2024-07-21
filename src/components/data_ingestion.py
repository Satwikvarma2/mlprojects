import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.modelTraining import ModelTrainerConfig
from src.components.modelTraining import ModelTrainer

@dataclass
class DataIngestionConfig:
    trainDataPath : str = os.path.join('artifact','train.csv')
    testingDataPath : str = os.path.join('artifact','test.csv')
    rawDataPath  : str = os.path.join('artifact','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("entered the session")
        try:
            df=pd.read_csv("/Users/satwik/Documents/MlProjects/notebook/data/StudentsPerformance.csv")
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.trainDataPath), exist_ok=True)
 # basically creates a directory names artifacts 
            df.to_csv(self.ingestion_config.rawDataPath,index=False,header =True)
            logging.info("train test split has beein intialised ok")
            train_data, test_data =train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.ingestion_config.trainDataPath,index=False,header=True)
            test_data.to_csv(self.ingestion_config.testingDataPath,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.trainDataPath,
                self.ingestion_config.testingDataPath 
            )

        except Exception as e:
            raise CustomException(e,sys)
            pass

if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))









   