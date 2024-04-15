# Medical-Cost-Prediction

This project explores and predicts individual medical costs billed by health insurance using a dataset sourced from Kaggle. The aim is to uncover hidden patterns and determine key factors that significantly impact medical charges, such as age, BMI, smoking status, and other demographic variables.

Key Highlights:
Dataset Overview: The dataset includes demographic information (age, sex), health-related attributes (BMI, smoking status, number of children), geographical data (region), and insurance charges (target variable).

Exploratory Data Analysis (EDA): The analysis highlighted age, BMI, and smoking status as critical determinants of insurance charges, revealing distinct patterns and correlations within the data.

Predictive Modeling: Various regression models (Linear Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost Regressor) were considered and evaluated. The Random Forest Regressor emerged as the most effective model for predicting medical costs.

Deployment with Streamlit: The project includes a Streamlit web application ('Prediction.py') that leverages a pre-trained Random Forest model to predict insurance charges based on user inputs (age, sex, BMI, children, smoker status, region).

How to Use:
Clone this repository.
Install the required Python packages (pip install -r requirements.txt).
Run the Streamlit application: streamlit run Prediction.py.
Enter your details and click "Predict Charges" to see the estimated insurance costs based on the trained model.
