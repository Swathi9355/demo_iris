from urllib import request
import streamlit as st
import requests

st.title("🌼Iris Flower Species prediction🌼")

st.sidebar.write("Enter your inputs")

sl=st.sidebar.slider("Sepal_length",0.0,10.0)

sw=st.sidebar.slider("sepal_",0.0,10.0)

pl=st.sidebar.slider("petal_length",0.0,10.0)

pw=st.sidebar.slider("petal_width",0.0,10.0)

btn=st.sidebar.button("Submit")

#data={
#   "sepal_length":sl,
#    "sepal_width":sw,
#    "petal_length":pl,
#    "petal_width":pw
#}

if btn:
    st.write("Sepal length : ",sl)
    st.write("Sepal width : ",sw)
    st.write("petal length : ",pl)
    st.write("petal width : ",pw)

p=st.button("Predict")

data={
    "sepal_length":sl,
    "sepal_width":sw,
    "petal_length":pl,
    "petal_width":pw
}

res=requests.post("http://127.0.0.1:8000 ",json=data)
result=res.json()
st.write(result["Predicted_species"])