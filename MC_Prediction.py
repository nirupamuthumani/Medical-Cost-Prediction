{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "880769c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import make_pipeline\n",
    "\n",
    "# Load the trained model\n",
    "with open('rf_model.pkl', 'rb') as file:\n",
    "    model_rf = pickle.load(file)\n",
    "\n",
    "\n",
    "st.title('Insurance Charges Prediction')\n",
    "\n",
    "# Input fields for the features\n",
    "age = st.number_input('Age', min_value=18, max_value=100)\n",
    "sex = st.selectbox('Sex', ['male', 'female'])\n",
    "bmi = st.number_input('BMI', min_value=10.0, max_value=50.0)\n",
    "children = st.number_input('Children', min_value=0, max_value=10)\n",
    "smoker = st.selectbox('Smoker', ['yes', 'no'])\n",
    "region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])\n",
    "\n",
    "\n",
    "if st.button('Predict Charges'):\n",
    "    # Create a DataFrame from the inputs\n",
    "    input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],\n",
    "                              columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])\n",
    "    \n",
    "    # Use the model to make a prediction\n",
    "    prediction = model_rf.predict(input_data)[0]  # [0] to get the single prediction value\n",
    "    \n",
    "    # Display the prediction\n",
    "    st.subheader(f'Predicted Charges: ${prediction:,.2f}')\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
