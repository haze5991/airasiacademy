import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

st.write("# GaussianNB Iris Flower Prediction App")
st.write("This app predicts the **Iris flower** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4) # title, min_value, max_value, default_value
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("IrisGaussianNaiveBayes.h5", "rb"))
prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df) # shows the probability

st.subheader('Class labels and their corresponding index number')

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

