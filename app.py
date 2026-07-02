import streamlit as st
from src.test_genie import get_curated_resume_data

# Page configurations - Dark Mode Framework 
st.set_page_config(page_title="Portfolio-Genie-AI", page_icon="🧞", layout="centered")

# 🔥 PREMIUM CUSTOM STYLING & ANIMATIONS INJECTION (Cyberpunk Dark Tech Theme)
st.markdown("""
    <style>
    /* Global App Background Fade-In Animation */
    .stApp {
        background-color: #0d0f12;
        animation: fadeInBackground 1.2s ease-out;
    }
    @keyframes fadeInBackground {
        from { opacity: 0; } to { opacity: 1; }
    }

    /* Premium Futuristic Title Container */
    .premium-header {
        background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid #3b82f6;
        box-shadow: 0 8px 32px 0 rgba(59, 130, 246, 0.15);
        text-align: center;
        margin-bottom: 25px;
        animation: slideDownHeader 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes slideDownHeader {
        from { transform: translateY(-30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .premium-title {
        font-family: 'Inter', system-ui, sans-serif;
        font-weight: 800;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #f43f5e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        letter-spacing: -0.5px;
        margin-bottom: 5px;
    }

    /* Suggestion Chips/Buttons Hover Glow Transitions */
    div.stButton > button {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid #475569 !important;
        border-radius: 20px !important;
        padding: 8px 20px !important;
        font-weight: 500 !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    div.stButton > button:hover {
        border-color: #60a5fa !important;
        background-color: #0f172a !important;
        box-shadow: 0 0 15px rgba(96, 165, 250, 0.4) !important;
        transform: translateY(-2px) scale(1.02) !important;
    }

    /* Smooth Floating Response Cards for Chat Messages */
    .stChatMessage {
        animation: floatInResponse 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
    }
    @keyframes floatInResponse {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    /* Spinner Design Tweaks */
    .stSpinner > div {
        border-top-color: #a78bfa !important;
    }
    
    /* Clean layout divider line animation */
    hr {
        border-color: #1e293b !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FRONTEND UI ELEMENTS ---

# Premium Top Showcase Card
st.markdown("""
    <div class="premium-header">
        <div class="premium-title">PORTFOLIO GENIE AI</div>
        <p style="color: #94a3b8; font-size: 1.05rem; margin: 0; font-weight: 400;">
            Next-Gen Local LLM Core & Hybrid Guardrail Framework
        </p>
        <p style="color: #64748b; font-size: 0.85rem; margin-top: 5px; font-family: monospace;">
            Developer Pipeline Architecture by Aditya Raj Chourasiya
        </p>
    </div>
""", unsafe_allow_html=True)

# Quick Trigger System Configuration
st.write("✨ **Quick Exploration Matrix:**")
col1, col2, col3 = st.columns(3)
with col1:
    b1 = st.button("🚀 Who is Aditya?")
with col2:
    b2 = st.button("💻 Show Core Tech Skills")
with col3:
    b3 = st.button("🛠️ Architecture of Guard IQ")

# State Persistence Matrix
if "messages" not in st.session_state:
    st.session_state.messages = []

# Message Streaming
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_query = None
if b1: user_query = "Who is Aditya Raj Chourasiya?"
if b2: user_query = "What are the technical skills of Aditya?"
if b3: user_query = "Tell me about the project Guard IQ."

chat_input = st.chat_input("Query the pipeline regarding skills, benchmarks, or models...")
if chat_input:
    user_query = chat_input

# Synchronous Execution Block
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Genie parsing internal architecture layers... 🧠"):
            bot_response = get_curated_resume_data(user_query)
            
            if not bot_response:
                bot_response = "I am fine-tuned on Aditya's localized domain logs. Please query regarding specific tech matrices (React, Python, MLOps) or key projects."
            
            st.markdown(bot_response)
            
    st.session_state.messages.append({"role": "assistant", "content": bot_response})