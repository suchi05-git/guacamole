import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Product Governance Benchmark", layout="wide")

st.title("📊 Product Governance Assistant Benchmarking Dashboard")
st.markdown("Compare Cognizant's workflow with global bank practices across governance, compliance, automation, and product health.")

# Load benchmarking data
with open("data/benchmarking_data.json", "r") as f:
    data = json.load(f)

# Display comparison table
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# Downloadable slide deck
try:
    with open("assets/Benchmarking_Comparison_Presentation.pptx", "rb") as file:
        st.download_button(label="📥 Download Benchmarking Slide Deck", data=file,
                           file_name="Benchmarking_Comparison_Presentation.pptx",
                           mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
except FileNotFoundError:
    st.warning("Slide deck not found. Please add Benchmarking_Comparison_Presentation.pptx to the assets folder.")
