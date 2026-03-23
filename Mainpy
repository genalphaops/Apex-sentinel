import streamlit as st
import pandas as pd
import requests
import json
import os
from datetime import datetime

# --- 1. THE STEALTH CONFIG ---
st.set_page_config(page_title="APEX SENTINEL", page_icon="🌑", layout="wide")
# Database (Locked & Private)
DB_FILE = "apex_data.csv"
if not os.path.exists(DB_FILE):
    pd.DataFrame(columns=["Email", "Points", "Streak", "Status", "Icons"]).to_csv(DB_FILE, index=False)

# --- 2. THE OPENROUTER "DIRECT-HIT" ENGINE ---
def call_openrouter(query):
    # This keeps the AI focused. NO ADVICE. NO TIPS.
    api_key = st.secrets["OPENROUTER_API_KEY"]
    instruction = "You are the Apex Solver. Solve the math/science problem INSTANTLY. Bold the final answer. No tips."
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        data=json.dumps({
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": [{"role": "system", "content": instruction}, {"role": "user", "content": query}]
        })
    )
    return response.json()['choices'][0]['message']['content']

# --- 3. UI: THE "GHOST" THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .stButton>button { border: 1px solid #ffffff; background: none; color: white; width: 100%; }
    .stButton>button:hover { background: #ffffff; color: black; }
    .xp-display { font-size: 24px; font-weight: bold; border-left: 5px solid #ffffff; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE CORE LOGIC ---
with st.sidebar:
    st.title("🌑 APEX OS")
    u_mail = st.text_input("Enter Ghost ID (Gmail)")
    st.divider()
    menu = st.radio("Mode", ["🎯 Neural Solve", "🔥 Streak & Shop", "📊 Pune Rankings"])

if u_mail:
    df = pd.read_csv(DB_FILE)
    if u_mail in df[df['Status'] == 'ACTIVE']['Email'].values:
        # --- SOLVER MODE ---
        if menu == "🎯 Neural Solve":
            st.markdown("<p class='xp-display'>STATUS: OPERATIONAL</p>", unsafe_allow_html=True)
            doubt = st.text_area("Transmit Question (NCERT/CBSE)")
            if st.button("DECONSTRUCT"):
                with st.spinner("🛰️..."):
                    st.write(call_openrouter(doubt))
                    st.balloons()
        
        # --- STREAK & SHOP (NO REAL MONEY ADS) ---
        elif menu == "🔥 Streak & Shop":
            st.title("🔥 The Vault")
            st.write("Current Points: 450")
            st.button("🧊 Buy Streak Freeze (100 Pts)")
            st.button("💠 Equip 'Hacker' Icon (500 Pts)")
            
    else:
        # --- THE PAYWALL (NO ADS, JUST DIRECT UPI) ---
        st.error("🔒 ACCESS DENIED")
        st.write("### Unlock Apex Pro")
        st.write("To enter the Ghost Network, pay ₹49 to the UPI below.")
        st.code("apex.intel.pune@upi")
        st.info("Send a screenshot of payment to the Admin to activate.")
        
