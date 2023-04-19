
# Malicious URL Detection System Using Machine Learning, Deep Learning and NLP

## Website URL: https://main.d3ic9i6whelr8c.amplifyapp.com/

## Project Description:

    The Malicious URL Detection System is a comprehensive and powerful platform for detecting and preventing access to malicious websites using machine learning, deep learning, and natural language processing (NLP) techniques. 
    
    The system's primary goal is to identify and categorize URLs into safe or malicious, thereby safeguarding users from cyber threats and enhancing overall internet security.

    The project's frontend is developed using React, a popular JavaScript library for building user interfaces, while the backend is built using the Flask web framework.
    
    The entire model pipeline, from data ingestion and preprocessing to model building, is implemented in Python, with extensive logging and custom exception handling to ensure optimal performance and maintainability. 
    
    The frontend is deployed on AWS Amplify, and the backend is deployed using Azure, offering seamless integration and scalability.


## Features


- #### Data Ingestion:

    Data ingestion involves collecting, importing, and processing raw data from various sources, such as public and private datasets of URLs, web scraping, and real-time data streams. This data is used to train and validate the machine learning and deep learning models.

- #### Data Preprocessing:

    The data preprocessing stage includes data cleaning, feature extraction, and feature engineering to transform the raw data into a format suitable for modeling. This stage involves handling missing or inconsistent data, tokenization, and extraction of relevant features from URLs, such as domain names, subdomains, and URL lengths.

- #### Model Building:

    The project utilizes machine learning, deep learning, and NLP techniques to build multiple models for malicious URL detection. These models include traditional ML algorithms (e.g., decision trees, SVM), deep learning models (e.g., CNN, RNN), and NLP-based models (e.g., transformers, word embeddings). The models are trained and validated using the preprocessed data and evaluated based on their accuracy, precision, recall, and F1-score.

- #### Model Integration:
    The selected models are integrated into the Flask backend, which serves as an API for the React frontend. The API receives URL inputs from users, processes them using the trained models, and returns the classification results (i.e., safe or malicious) to the frontend.

- #### Logging and Custom Exception Handling:
    The system incorporates extensive logging and custom exception handling mechanisms to monitor the application's performance, detect issues, and ensure a seamless user experience. These mechanisms provide detailed information on errors, warnings, and system events, enabling developers to troubleshoot and improve the system continuously.

- #### Frontend Deployment on AWS Amplify:
    The React frontend is deployed using AWS Amplify, a development platform for building and deploying secure and scalable web applications. Amplify provides a range of features, including authentication, storage, and serverless functions, allowing the frontend to be easily and securely hosted in the cloud.

- #### Backend Deployment on Azure:
    The Flask backend is deployed using Azure, Microsoft's cloud computing platform. Azure offers a range of services for hosting, scaling, and managing web applications, ensuring that the backend can handle increasing traffic and user demands.

## Tech Stack

**Frontend:** React, ChakraUI, Tsparticles

**Server:** Flask, Python, Machine Learning, Deep , NLP, Text processing


## Prerequisites
- React.js
- Node.js
- Python 3
- Flask
- Azure account
- AWS Amplify account



## Installation

Clone the repository

```bash
  git clone https://github.com/Priyanshu9898/End-to-End-Malicious-URL-Detection.git
```

Change to the project's directory

```bash
  cd End-to-End-Malicious-URL-Detection
```

Install the frontend dependencies

```bash
  cd frontend
  npm install
```

Install the Backend dependencies

```bash
  cd backend
  pip install -r requirements.txt

```

## Usage
Start the frontend development server
```bash
  cd frontend
  npm start

```

Start the backend development server
```bash
  cd backend
  python app.py

```

Open your browser and visit http://localhost:3000 to access the frontend of the web application.
## API Reference

#### Get all items

```http
  POST api/predict
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` |  URL to prediction |




## Screenshots

![App Screenshot](https://i.postimg.cc/3J50R6Gn/Malicious-URL-Detection-Brave-19-04-2023-21-46-14.png)


![App Screenshot](https://i.postimg.cc/xTvJbRyY/Malicious-URL-Detection-Brave-19-04-2023-21-46-23.png)


![App Screenshot](https://i.postimg.cc/SxVngxvv/Malicious-URL-Detection-Brave-19-04-2023-21-47-06.png)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Priyanshu9898/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priyanshumalaviya/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Priyanshu2281)
[![Medium](https://img.shields.io/badge/medum-1DA1F2?style=for-the-badge&logo=medium&logoColor=black)](https://medium.com/@priyanshumalaviya9210)
## Demo

Insert gif or link to demo


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## License

[MIT](https://choosealicense.com/licenses/mit/)

