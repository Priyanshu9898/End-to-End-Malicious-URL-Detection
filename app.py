from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import os
from src.pipeline.predict_pipeline import PredictPipeline

app = Flask(__name__)

# get the path to the models folder
model_path = "./artifacts/Best Model"

# load the model
with open(os.path.join(model_path, 'Decision Tree.pkl'), 'rb') as f:
    model = pickle.load(f)

# print(model)
pred = PredictPipeline()

# CORS(app, origins='https://main.d3ic9i6whelr8c.amplifyapp.com')

cors = CORS(app, resources={r"/api/*": {"origins": "https://main.de8n33yv46tnz.amplifyapp.com"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello World!</h1>"

@app.route('/api/predict', methods=['POST'])
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
   app.run()