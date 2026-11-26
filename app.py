
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Data Cleaning Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }
    .stApp {
        background-color: #f5f7fb;
    }
    h1 {
        color: #172554;
    }
</style>
""", unsafe_allow_html=True)

# Dashboard header
st.title("📊 Data Cleaning Dashboard")
st.caption("Upload dataset")

st.divider()

# Dataset upload
st.subheader("Upload Dataset")

uploaded_file = st.file_uploader(
    "Choose your dataset",
    type=["csv", "xlsx", "xls", "json"],
    help="Upload CSV, Excel, or JSON files"
)

if uploaded_file is not None:

    try:
        file_name = uploaded_file.name

        # Read dataset
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)

        elif file_name.endswith(".json"):
            df = pd.read_json(uploaded_file)

        st.success(f"Successfully uploaded: {file_name}")
    except Exception as e:
        st.error(f"Error reading dataset: {e}")

else:
    st.info("👆 Please upload a dataset to get started.")

    st.markdown("""
    ### Supported File Formats
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    - JSON (.json)
    """)
