import streamlit as st
import joblib

model = joblib.load("model.joblib")

st.title("Iris Flower Prediction")

sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

if st.button("Predict"):

    prediction = model.predict([[sepal_length,
                                 sepal_width,
                                 petal_length,
                                 petal_width]])

    species = ["Setosa", "Versicolor", "Virginica"]

    st.success("Predicted Flower: " + species[prediction[0]])