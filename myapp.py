import streamlit as st
import pandas as pd
import pickle 

st.title(""" PROJECT 13 - CLICK TRHOUG RATE PREDICTION  - Vijay Kumar           """)
st.write("Click through rate prediction for Advertisement:")

def prediction(inputdf):
	ctr_model = pickle.load(open('ctrmodel.pkl','rb'))
	x=ctr_model.predict(inputdf)
	if x[0] < 0.2:
		return 'The Ad will likely to be not clicked'
	else:
		return 'The Ad is likely to be CLICKED'
		
datafile = st.file_uploader("Upload CSV FILE ", type = ["csv"])
if datafile is not None:
	inputdata = pd.read_csv(datafile)
	st.dataframe(inputdata)

if st.button("Predict"):
	pred=prediction(inputdata)
	st.write('Here is the prediction based on the input dataset')
	st.success(pred)
	