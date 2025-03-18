import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("potato_tomato_pests_diseases_expanded.csv")  # Ensure this file is in the same directory

df = load_data()

def predict_treatment(disease_name):
    """Searches for pesticides and herbicides for a given disease name from the CSV file."""
    disease_row = df[df["Disease"].str.lower() == disease_name.lower()]  # Case-insensitive match
    
    if disease_row.empty:
        return None, None  # Return None if disease not found
    
    pesticide = disease_row["Pesticide"].values[0]
    herbicide = disease_row["Herbicide"].values[0]
    return pesticide, herbicide

# Streamlit UI
st.title("Plant Disease Treatment Finder 🌱")
st.write("Enter a disease name to find the recommended pesticide and herbicide.")

# User Input
disease = st.text_input("Enter the disease name:")

# Button to trigger search
if st.button("Find Treatment"):
    if disease:
        pesticide, herbicide = predict_treatment(disease)
        
        if pesticide and herbicide:
            st.success(f"**Disease:** {disease}")
            st.info(f"**Recommended Pesticide:** {pesticide}")
            st.info(f"**Recommended Herbicide:** {herbicide}")
        else:
            st.error("Disease not found in the dataset. Please check the spelling or try another disease.")
    else:
        st.warning("Please enter a disease name.")

