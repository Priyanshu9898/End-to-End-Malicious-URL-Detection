import os
import sys
import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score, make_scorer
from src.logger import logging
import glob
from src.exception import customException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):


    try:
        report_train = {}
        report_test = {}

        # Set up the scoring metric
        scoring_metric = make_scorer(accuracy_score)

        k = 0
       
        for i in range(len(list(models))):

            k += 1
            if(k <= 3):
                continue
        
            else:
                model = list(models.values())[i]

                para = param[list(models.keys())[i]]

                model_name_list = list(models.keys())

                model_name = model_name_list[i]

                # Set up the cross-validation method
                cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

                print(f"Tuning hyperparameters for {model_name}...")

                logging.info(f"Tuning hyperparameters for {model_name}...")

                gs = GridSearchCV(model, para,scoring = scoring_metric, cv=cv)
                gs.fit(X_train,y_train)

                model.set_params(**gs.best_params_)

                logging.info(f"Best Parameters for {model_name} are {gs.best_params_}...")


                logging.info(f"Fitting the {model_name} with best parameters...")
                model.fit(X_train, y_train)

                # Prediction on the Training Data
                y_train_pred = model.predict(X_train)

                # Calculate performance metrics for Train Data
                train_accuracy = accuracy_score(y_train, y_train_pred)
                train_precision = precision_score(y_train, y_train_pred, average='weighted')
                train_recall = recall_score(y_train, y_train_pred, average='weighted')
                train_f1 = f1_score(y_train, y_train_pred, average='weighted')

                report_train[model_name] = {
                    "accuracy" : train_accuracy,
                    "precision" : train_precision,
                    "recall" : train_recall,
                    "f1 score": train_f1
                }

                logging.info(f"Training Report for model on Train Data{model_name} ===> {report_train[model_name]}")

                # Prediction on the Test Data
                y_test_pred = model.predict(X_test)

                # Calculate performance metrics for Test Data
                test_accuracy = accuracy_score(y_test, y_test_pred)
                test_precision = precision_score(y_test, y_test_pred, average='weighted')
                test_recall = recall_score(y_test, y_test_pred, average='weighted')
                test_f1 = f1_score(y_test, y_test_pred, average='weighted')

                report_test[model_name] = {
                    "accuracy" : test_accuracy,
                    "precision" : test_precision,
                    "recall" : test_recall,
                    "f1 score": test_f1
                }

                logging.info(f"Training Report for model on Test Data{model_name} ===> {report_test[model_name]}")
                
                pickle.dump(model, open(f'./artifacts/Models/{model_name}.pkl', 'wb'))
                logging.info(f"Pickle file has been created for {model_name} in artifact folder")


        train_res = pd.DataFrame(report_train).T
        test_res = pd.DataFrame(report_test).T

        train_res.to_csv("./artifacts/Train_Result2.csv")
        test_res.to_csv("./artifacts/Test_Result2.csv")

        logging.info(f"Training Report and Test report has been saved to CSV file in artifact folder")
        
        return report_train, report_test

    except Exception as e:
        raise customException(e, sys)



def get_result(X_train, y_train, X_test, y_test):
    try:
        model_path = "./artifacts/Models"
        report_train = {}
        report_test = {}

        # Get all .pkl files in the folder
        files = glob.glob(model_path + '/*.pkl')

        # Print the list of files
        for file_path in files:
            if(file_path != "none"):
                model_name = file_path.split("\\")[1][0: -4]

                model = load_object(file_path)

                # Prediction on the Training Data
                y_train_pred = model.predict(X_train)

                # Calculate performance metrics for Train Data
                train_accuracy = accuracy_score(y_train, y_train_pred)
                train_precision = precision_score(y_train, y_train_pred, average='weighted')
                train_recall = recall_score(y_train, y_train_pred, average='weighted')
                train_f1 = f1_score(y_train, y_train_pred, average='weighted')

                report_train[model_name] = {
                    "accuracy" : train_accuracy,
                    "precision" : train_precision,
                    "recall" : train_recall,
                    "f1 score": train_f1
                }

                logging.info(f"Best Model finding- Training Report for model on Train Data{model_name} ===> {report_train[model_name]}")

                # Prediction on the Test Data
                y_test_pred = model.predict(X_test)

                # Calculate performance metrics for Test Data
                test_accuracy = accuracy_score(y_test, y_test_pred)
                test_precision = precision_score(y_test, y_test_pred, average='weighted')
                test_recall = recall_score(y_test, y_test_pred, average='weighted')
                test_f1 = f1_score(y_test, y_test_pred, average='weighted')

                report_test[model_name] = {
                    "accuracy" : test_accuracy,
                    "precision" : test_precision,
                    "recall" : test_recall,
                    "f1 score": test_f1
                }

                logging.info(f"Best Model finding-Training Report for model on Test Data{model_name} ===> {report_test[model_name]}")

        train_res = pd.DataFrame(report_train).T
        
        # train_res.columns=["Model Name", "accuracy", "precision", "recall", "f1 score"]
        test_res = pd.DataFrame(report_test).T
        # test_res.columns=["Model Name", "accuracy", "precision", "recall", "f1 score"]

        train_res.to_csv("./artifacts/Train_Result.csv")
        test_res.to_csv("./artifacts/Test_Result.csv")

        logging.info(f"Best Model finding- Training Report and Test report has been saved to CSV file in artifact folder")        


    except Exception as e:
        raise customException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise customException(e, sys)


def get_best_model():
    try:
        train_result = pd.read_csv("./artifacts/Train_Result.csv")
        test_result = pd.read_csv("./artifacts/Test_Result.csv")


        train_result = train_result.rename(columns={'Unnamed: 0': 'Model Name'})
        test_result = test_result.rename(columns={'Unnamed: 0': 'Model Name'})


        # sort the DataFrame by the 'accuracy' column in descending order
        df_train = train_result.sort_values(by='accuracy', ascending=False)
        df_test = test_result.sort_values(by='accuracy', ascending=False)

        print(df_train)
        print(df_test)

        best_model = df_test.iloc[0]
        
        return best_model



    except Exception as e:
        raise customException(e, sys)