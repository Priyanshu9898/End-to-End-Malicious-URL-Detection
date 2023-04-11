import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

from src.exception import customException
from src.logger import logging

from src.utils import save_object,evaluate_models, get_result, get_best_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train, X_test, y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "XGBoost": XGBClassifier(),
                "CatBoost": CatBoostClassifier(verbose=False),
                "AdaBoost": AdaBoostClassifier()
            }

            # Set up the hyper parameters to be tuned for each model
            # Set up the hyperparameters to be tuned for each model
            param_grid = {
                "Logistic Regression": {
                    "C": [0.1, 1.0, 10.0],
                    "penalty": ["l1", "l2"],
                    'multi_class': ['auto', 'ovr', 'multinomial']
                },
                "Decision Tree": {
                    "criterion": ["gini", "entropy"],
                    "max_depth": [None, 5, 10]
                },
                "Random Forest": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [None, 5, 10]
                },
                "Gradient Boosting": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [None, 5, 10]
                },
                "XGBoost": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [None, 5, 10],
                    "learning_rate": [0.01, 0.1, 0.5]
                },
                "CatBoost": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [None, 5, 10],
                    "learning_rate": [0.01, 0.1, 0.5]
                },
                "AdaBoost": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.5]
                }
            }


            # model_report_train, model_report_test = evaluate_models(
            #     X_train= X_train, 
            #     y_train = y_train,
            #     X_test=X_test,
            #     y_test=y_test,
            #     models = models, 
            #     param = param_grid
            # )
            
            # print(model_report_train)

            # print(model_report_test)

            logging.info(f"function to compare the models is initialized")
            get_result(X_train, y_train, X_test, y_test)

            logging.info(f"function to find the best model is initialized")
            best_model = get_best_model()

            logging.info(f"the best model is - {best_model}")
            best_model_name = best_model['Model Name']
            print(best_model_name)

            best_model_score = best_model['accuracy']

            if best_model_score<0.6:
                raise customException("No best model found")
            
            logging.info(f"Best found model on both training and testing dataset")

            
            
        except Exception as e:
            raise customException(e,sys)