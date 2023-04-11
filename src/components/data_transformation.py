import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.logger import logging
from src.exception import customException
import os
from sklearn.preprocessing import LabelEncoder


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            
            categorical_columns = ['type']

            
            cat_pipeline=Pipeline(

                steps=[
                    ("Label Encoding", LabelEncoder()),
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
         

            preprocessor=ColumnTransformer(
                [
                    ("cat_pipelines",cat_pipeline,categorical_columns)

                ]
            )
            return preprocessor
        
        except Exception as e:
            raise customException(e,sys)
        

    def initiate_data_transformation(self,train_path,test_path):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()

            # print(train_df.columns)
            # print(test_df.columns)
            
            X = ['use_of_ip','abnormal_url', 'count.', 'count-www', 'count@',
                'count_dir', 'count_embed_domain', 'short_url', 'count%', 'count?', 'count-', 'count=', 'url_length', 'count_https',
                'count_http', 'hostname_length', 'sus_url', 'fd_length', 'tld_length', 'count_digits',
                'count_letters']

            target_column_name="type_code"

            logging.info(
                f"Applying preprocessing object on training Dataframe and testing Dataframe."
            )
            
            # print(train_df["type_code"])
            
            input_feature_train_df = train_df[X]
            input_feature_test_df = test_df[X]

            input_feature_train_arr = np.array(input_feature_train_df)
            input_feature_test_arr = np.array(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(train_df["type_code"])
            ]

            test_arr = np.c_[input_feature_test_arr, np.array(test_df["type_code"])]

            logging.info(f"Saved preprocessing object.")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            raise customException(e,sys)  