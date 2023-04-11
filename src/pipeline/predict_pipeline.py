import sys
import pandas as pd
from src.exception import customException
from src.utils import load_object
import os
import numpy as np

from src.components.data_transformationComponents import transformationFunctions

class PredictPipeline:
    def __init__(self):
        pass

    def transformURL(self, url):
        try:
            obj = transformationFunctions()
            use_of_ip = obj.having_ip_address(url)
            abnormal_url = obj.abnormal_url(url)
            countDot = obj.count_dot(url)
            countWWW = obj.count_www(url)
            countATR = obj.count_atrate(url)
            count_dir= obj.no_of_dir(url)
            count_embed_domain = obj.no_of_embed(url)
            short_url = obj.shortening_service(url)
            countPercentage = obj.count_per(url)
            countQUES = obj.count_ques(url)
            countHyphen = obj.count_hyphen(url)
            countEqual = obj.count_equal(url)
            url_length = obj.url_length(url)
            count_https = obj.count_https(url)
            count_http = obj.count_http(url)
            hostname_length = obj.hostname_length(url)
            sus_url = obj.suspicious_words(url)
            fd_length = obj.fd_length(url)
            tld_length = obj.tld_length(url)
            count_digits = obj.digit_count(url)
            count_letters = obj.letter_count(url)

            custom_data_input_dict = {
                "use_of_ip": use_of_ip,
                "abnormal_url":abnormal_url,
                "countDot":countDot,
                "countWWW":countWWW,
                "countATR":countATR,
                "count_dir":count_dir,
                "count_embed_domain":count_embed_domain,
                "short_url":short_url,
                "countPercentage":countPercentage,
                "countQUES":countQUES,
                "countHyphen":countHyphen,
                "countEqual":countEqual,
                "url_length":url_length,
                "count_https":count_https ,
                "count_http": count_http,
                "hostname_length":hostname_length,
                "sus_url":sus_url,
                "fd_length":fd_length,
                "tld_length": tld_length,
                "count_digits":count_digits,
                "count_letters":count_letters,
            }

            ls = [use_of_ip,
            abnormal_url,
            countDot,
            countWWW,
            countATR,
            count_dir,
            count_embed_domain,
            short_url,
            countPercentage,
            countQUES,
            countHyphen,
            countEqual,
            url_length,
            count_https ,
            count_http,
            hostname_length,
            sus_url,
            fd_length,
            tld_length,
            count_digits,
            count_letters]

            arr = np.array(ls)

            return arr
            # return  custom_data_input_dict.values()

        except Exception as e:
            raise customException(e,sys)
        
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise customException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise customException(e, sys)