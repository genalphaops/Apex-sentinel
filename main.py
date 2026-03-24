import streamlit as st
import requests
import json
import time

# --- 1. APEX NEON CORE (THE LOOK) ---
st.set_page_config(page_title="APEX OMNI V15", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top, #001220 0%, #000000 100%);
        color: #00d2ff;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* THE GHOST LOGO */
    .logo {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(to bottom, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 10px 20px rgba(0, 210, 255, 0.3);
        margin-bottom: 0px;
    }

    /* GLASS-MORPHISM MODULES */
    .module-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 210, 255, 0.2);
        padding: 25px;
        border-radius: 24px;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-top: 20px;
    }

    /* THE ADDICTIVE BUTTON */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00d2ff, #0052d4);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 18px;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.1rem;
        transition: 0.4s;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px #00d2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE NEURAL LINK (GEMINI FLASH 2.0) ---
def apex_brain(prompt, persona):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": [
                {"role": "system", "content": persona},
                {"role": "user", "content": prompt}
            ]
        }
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))
        return r.json()['choices'][0]['message']['content']
    except:
        return "⚠️ SIGNAL LOST. RECONNECTING TO PUNE GHOST NODE..."

# --- 3. THE INTERFACE ---
st.markdown("<h1 class='logo'>APEX OMNI V15</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa;'>The 1% Advantage. Developed for the Elite.</p>", unsafe_allow_html=True)

# DASHBOARD STATS
c1, c2, c3 = st.columns(3)
with c1: st.markdown("🏆 **RANK:** #1 PUNE")
with c2: st.markdown("🔥 **STREAK:** 5 DAYS")
with c3: st.markdown("🔋 **AI POWER:** 100%")

# MODULE SELECTION
choice = st.selectbox("", ["🎯 THE PAPER CRUSHER", "⚽ ISAGI AI TUTOR", "🔓 UNLOCK PRO ACCESS"])

if choice == "🎯 THE PAPER CRUSHER":
    st.markdown("<div class='module-box'><h3>🎯 Paper Crusher</h3><p>Paste your textbook notes. I will give you the 3 points that will be in the exam.</p></div>", unsafe_allow_html=True)
    txt = st.text_area("Input Paragraph:", height=200, placeholder="Paste your text here...")
    if st.button("DESTROY PAPER"):
        with st.spinner("Crushing..."):
            ans = apex_brain(txt, "You are an Exam Specialist. Give 3 short bullet points a 6th grader can memorize instantly. Use emojis.")
            st.info(ans)

elif choice == "⚽ ISAGI AI TUTOR":
    st.markdown("<div class='module-box'><h3>⚽ Egoist Tutor</h3><p>Learn Math & Science like a Blue Lock striker.</p></div>", unsafe_allow_html=True)
    topic = st.text_input("What is your doubt?")
    if st.button("AWAKEN EGO"):
        with st.spinner("Analyzing Field..."):
            ans = apex_brain(topic, "You are Isagi Yoichi. Explain this study concept like a soccer strategy. Be intense and helpful.")
            st.success(ans)

elif choice == "🔓 UNLOCK PRO ACCESS":
    st.markdown("<div class='module-box' style='border-color: #ffd700;'><h2>💎 APEX PRO</h2><p>Unlimited searches + 24/7 Exam Support.</p><h3>Pay ₹49 to: <code>apex.pune@upi</code></h3><p>Send screenshot to CEO to activate.</p></div>", unsafe_allow_html=True)

# --- 4. GUEST LOCK ---
st.divider()
st.caption("Ghost Network v15.0 | Secure Node: Pune-Maharashtra")

        
