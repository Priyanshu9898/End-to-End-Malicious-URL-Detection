from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import os
from src.pipeline.predict_pipeline import PredictPipeline

application = Flask(__name__)

# get the path to the models folder
model_path = "./artifacts/Best Model"

# load the model
with open(os.path.join(model_path, 'Decision Tree.pkl'), 'rb') as f:
    model = pickle.load(f)

pred = PredictPipeline()

cors = CORS(application, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@application.route('/api/predict', methods=['POST'])
def predict():
    url = request.json['url']
    print("URL: " + url)
    
    transform_url = pred.transformURL(url)

    transform_url = transform_url.reshape(1, -1)

    # print("transform_url" , transform_url)

    prediction = model.predict(transform_url)
    
    # 'benign', 'defacement','phishing','malware'
    if(prediction == 0):
        res = 'benign'
    elif(prediction == 1):
        res = 'defacement'
    elif(prediction == 2):
        res = 'phishing'
    else:
        res = 'malware'

    return jsonify({'prediction': res})

if __name__ == '__main__':
    application.run(debug=True)