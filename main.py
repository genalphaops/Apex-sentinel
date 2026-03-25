import streamlit as st
import requests
import json

# --- 1. THE NVIDIA ARCHITECTURE (BLACK & LIME GREEN) ---
st.set_page_config(page_title="APEX OMNI RTX", page_icon="💚", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&family=Source+Code+Pro:wght@400;900&display=swap');
    
    .stApp {
        background-color: #0b0b0b;
        color: #76b900; /* NVIDIA GREEN */
        font-family: 'Source Code Pro', monospace;
    }

    /* THE FOUNDER'S LOGO */
    .rtx-header {
        font-family: 'Roboto Condensed', sans-serif;
        font-weight: 700;
        font-size: 3.5rem;
        letter-spacing: -1px;
        color: #ffffff;
        text-align: left;
        border-left: 8px solid #76b900;
        padding-left: 20px;
        margin-bottom: 0px;
        text-transform: uppercase;
    }

    /* TITANIUM MODULES */
    .gpu-card {
        background: linear-gradient(145deg, #1a1a1a, #000000);
        border: 1px solid #333333;
        padding: 30px;
        border-radius: 4px; /* Sharp, professional corners */
        box-shadow: 10px 10px 20px #050505, -5px -5px 15px #1a1a1a;
        margin-bottom: 25px;
    }

    /* THE 'FORCE' BUTTON */
    .stButton>button {
        width: 100%;
        background-color: #76b900;
        color: black;
        border: none;
        border-radius: 2px;
        padding: 15px;
        font-family: 'Roboto Condensed', sans-serif;
        font-weight: 900;
        font-size: 1.2rem;
        transition: 0.3s;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        color: #000000;
        box-shadow: 0 0 30px rgba(118, 185, 0, 0.6);
    }

    /* INPUT OVERRIDE */
    input, textarea {
        background-color: #111 !important;
        color: #fff !important;
        border: 1px solid #76b900 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE CORE KERNEL (API) ---
def compute_engine(query, system_prompt):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": query}]
        }
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))
        return r.json()['choices'][0]['message']['content']
    except:
        return "ERROR: SYSTEM THERMAL THROTTLING. RECONNECTING..."

# --- 3. THE CONTROL PANEL ---
st.markdown("<h1 class='rtx-header'>APEX OMNI <span style='color:#76b900;'>RTX</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#555; margin-left:30px;'>GEFORCE ACADEMIC SERIES | PUNE DISTRO</p>", unsafe_allow_html=True)

st.divider()

# STATS BAR
c1, c2, c3, c4 = st.columns(4)
c1.metric("CORE CLOCK", "5.2 GHz")
c2.metric("MEMORY", "16 GB")
c3.metric("STREAK", "🔥 7")
c4.metric("TEMP", "OPTIMAL")

st.divider()

# MODULES
choice = st.radio("SELECT MODE", ["OVERCLOCK (SOLVER)", "RAY-TRACING (TUTOR)", "LICENSE (PRO)"])

if choice == "OVERCLOCK (SOLVER)":
    st.markdown("<div class='gpu-card'><h3>[ FAST SOLVE MODE ]</h3><p>Deconstruct exam papers with 0ms latency.</p></div>", unsafe_allow_html=True)
    task = st.text_area("LOAD DATA:")
    if st.button("RENDER SOLUTION"):
        with st.status("Computing via NVIDIA Kernels..."):
            ans = compute_engine(task, "You are a high-performance exam solver. Solve this Grade 6 question perfectly. Bold the final result.")
            st.success(ans)

elif choice == "RAY-TRACING (TUTOR)":
    st.markdown("<div class='gpu-card'><h3>[ VISUAL LOGIC MODE ]</h3><p>Trace the logic of any concept back to its source.</p></div>", unsafe_allow_html=True)
    concept = st.text_input("QUERY CONCEPT:")
    if st.button("TRACE LOGIC"):
        with st.spinner("Ray-tracing concept pathways..."):
            ans = compute_engine(concept, "Explain this Grade 6 NCERT concept with ultra-clear logic and professional examples.")
            st.info(ans)

elif choice == "LICENSE (PRO)":
    st.markdown("<div class='gpu-card' style='border-color: #ffffff;'><h2>ACTIVATE FULL LICENSE</h2><p>Unlock Ray-Tracing and Overclock limits.</p><h3>TRANSFER ₹49 TO: <code>apex.pune@upi</code></h3></div>", unsafe_allow_html=True)

st.divider()
st.caption("Powered by APEX NVIDIA-STREAMS | Version 18.0.4")
