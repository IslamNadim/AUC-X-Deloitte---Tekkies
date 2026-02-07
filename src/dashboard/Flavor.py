import streamlit as st
import pandas as pd
import numpy as np
import requests

# ---------------------------
# API CONFIG
# ---------------------------
API_URL = "http://127.0.0.1:5001"
API_KEY = "supersecretkey"

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="FlavorCraft Menu Pricing Intelligence",
    layout="wide"
)

# ---------------------------
# Load REAL inventory from API
# ---------------------------
@st.cache_data
def load_inventory():
    try:
        headers = {"x-api-key": API_KEY}
        response = requests.get(f"{API_URL}/api/inventory/items", headers=headers)

        if response.status_code != 200:
            st.error("API error: could not load inventory")
            return pd.DataFrame()

        data = response.json()
        df = pd.DataFrame(data)

        if df.empty:
            st.warning("No menu items found in database.")
            return df

        # Temporary analytics until ML model added
        df["Sales_Volume"] = np.random.randint(20, 150, size=len(df))
        df["Revenue"] = df["avg_price"] * df["Sales_Volume"]
        df["Margin"] = df["avg_price"] - df["avg_cost"]
        df["Profit"] = df["Margin"] * df["Sales_Volume"]
        df["Price_Sensitivity"] = np.random.uniform(0.2, 0.8, size=len(df))

        return df

    except Exception as e:
        st.error(f"Connection error: {e}")
        return pd.DataFrame()


df = load_inventory()

# Stop if no data
if df.empty:
    st.stop()

# ---------------------------
# Title & Intro
# ---------------------------
st.title("🍽 FlavorCraft Menu Pricing Intelligence Dashboard")

st.markdown("""
This dashboard helps FlavorCraft management decide  
which menu items should have their prices raised, lowered, or kept the same  
based on **real database performance**.
""")

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🔎 Filters")

selected_items = st.sidebar.multiselect(
    "Select Menu Items",
    options=df["title"].unique(),
    default=df["title"].unique()
)

filtered_df = df[df["title"].isin(selected_items)]

# ---------------------------
# KPI Section
# ---------------------------
st.subheader("📊 Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"{filtered_df['Revenue'].sum():,.0f}")
col2.metric("Total Profit", f"{filtered_df['Profit'].sum():,.0f}")
col3.metric("Avg Margin", f"{filtered_df['Margin'].mean():.1f}")

# ---------------------------
# Table
# ---------------------------
st.subheader("📋 Menu Performance")

st.dataframe(
    filtered_df[[
        "title", "avg_price", "avg_cost",
        "Sales_Volume", "Revenue", "Profit", "Price_Sensitivity"
    ]],
    use_container_width=True
)

# ---------------------------
# Charts
# ---------------------------
st.subheader("📈 Sales vs Profit")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(filtered_df.set_index("title")["Sales_Volume"])

with col2:
    st.bar_chart(filtered_df.set_index("title")["Profit"])

# ---------------------------
# Scatter
# ---------------------------
st.subheader("🎯 Price Sensitivity vs Profit")

st.scatter_chart(
    filtered_df,
    x="Price_Sensitivity",
    y="Profit",
    size="Sales_Volume"
)

# =====================================================
# 🧠 AI MENU ASSISTANT  (FINAL PRODUCT FEATURE)
# =====================================================
st.markdown("---")
st.header("🧠 Ask FlavorCraft AI")

API_CHAT_URL = f"{API_URL}/api/menu/chat"

question = st.text_input("Ask a question about menu performance:")

if st.button("Ask AI") and question:

    payload = {
        "place_id": 1,
        "question": question
    }

    try:
        response = requests.post(
            API_CHAT_URL,
            json=payload,
            headers={"x-api-key": API_KEY},
            timeout=15
        )

        if response.status_code == 200:
            answer = response.json()["answer"]