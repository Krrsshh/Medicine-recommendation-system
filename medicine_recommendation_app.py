import streamlit as st
import pickle
import pandas as pd


def recommend(medicine):
    medicine_index = medicines[medicines['product_name'] == medicine].index[0]
    similar_medicines = sorted(list(enumerate(similarity[medicine_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicine = []
    for i in similar_medicines:
        recommended_medicine.append(medicines.iloc[i[0]].product_name)
    return recommended_medicine

medicine_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicine_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Medicine Recommender System')

selected_medicine_name = st.selectbox(
    'Select a medicine',
    medicines['product_name'].values )

if st.button('Recommend'):
    recommedations = recommend(selected_medicine_name)
    for i in recommedations:
        st.write(i)