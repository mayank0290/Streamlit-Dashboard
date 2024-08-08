import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="CSV Insight Explorer", page_icon="📊", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #020617;
    }

    /* Title styling */
    .stApp h1 {
        color: #4b72b0;
        font-family: 'Segoe UI', sans-serif;
        font-size: 36px;
        text-align: center;
    }

    /* Subheader and header styling */
    .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
        margin-top: 20px;
    }

    /* General text and label styling */
    .stApp p, .stApp label, .stApp .stMarkdown {
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
    }


    /* Text and data styling */
    .stApp .stDataFrame, .stApp .stPlotlyChart, .stApp .stAltairChart, .stApp .stVegaLiteChart {
        border: 2px solid #4b72b0;
        border-radius: 10px;
        background-color: #ffffff; 
        padding: 10px;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4b72b0;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Button hover effect */
    .stButton>button:hover {
        background-color: #5a86d7;
        color: #ffffff;
    }

    </style>
    """, unsafe_allow_html=True)

# Title
st.title("CSV Insight Explorer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Data preview
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Data summary
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # Filter data section
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns) 
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Data plotting
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    
    if st.button("Generate Chart"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else: 
    st.write("Waiting for the file...")       
