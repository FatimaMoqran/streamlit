import streamlit as st
import ktrain
st.write(""" # Application de classification d'emails """)
new_text = new_text = st.text_area("Enter Text","Type here")
st.button('Classify')

#loading the model
predictor = ktrain.load_predictor('/content/drive/My Drive/notebooks_chefdoeuvre_deep/model_corps_mail_bert')
prediction = predictor.predict(new_text)
st.write(prediction)
