import requests
import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="Operação Britain", layout="wide")

# Title and spacing
st.title("Operação Britain")
st.markdown("<br>", unsafe_allow_html=True)

# Fetch data from the Django API
try:
    response = requests.get("http://127.0.0.1:8000/dash/data")
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from API: {e}")
    st.stop()

# Display data as a table
st.subheader("Tabela do Banco de Dados")
st.dataframe(df, use_container_width=True)

# Create a downloadable Excel file
try:
    with pd.ExcelWriter("temp_database_export.xlsx", engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)

    # Add a button to download the spreadsheet
    with open("temp_database_export.xlsx", "rb") as file:
        st.download_button(
            label="Baixar Planilha",
            data=file,
            file_name="database_export.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
except Exception as e:
    st.error(f"Error creating download file: {e}")

