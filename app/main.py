import streamlit as st
import requests
import os
import time

# Page configuration
st.set_page_config(
    page_title="DiaClassifier | Advanced Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom header with emoji and colored text using markdown
st.markdown("""
# 🩺 DiaClassifier 
### *Precision Machine Learning for Diabetes Risk Prediction*
---
""", unsafe_allow_html=True)

# Sidebar for metadata and status
with st.sidebar:
    st.title("System Configuration")
    
    # Environment Selection
    env_mode = st.radio(
        "Select Engine Environment",
        ["Production (Render)", "Local / Development"],
        help="Choose 'Production' for the cloud API or 'Local' if running the FastAPI server locally."
    )
    
    if env_mode == "Production (Render)":
        API_URL = "https://diaclassifier-api.onrender.com"
    else:
        # Allow custom URL or default to localhost
        API_URL = st.text_input("Engine URL", value=os.getenv("API_URL", "http://127.0.0.1:8000"))
    
    # Clean the URL
    API_URL = API_URL.strip().rstrip("/")

    st.divider()
    st.markdown("### System Status")
    
    try:
        # Avoid proxy issues by specifying empty proxies
        metadata_res = requests.get(
            f"{API_URL}/metadata", 
            timeout=5, 
            proxies={'http': None, 'https': None}
        )
        if metadata_res.status_code == 200:
            meta = metadata_res.json()
            st.success(f"✅ Engine Online")
            st.metric("Model Version", meta.get('version', 'N/A'))
            st.caption(f"**Archive:** {meta.get('model_name', 'N/A')}")
        else:
            st.error(f"❌ Engine Error ({metadata_res.status_code})")
    except requests.exceptions.ConnectionError as e:
        st.error("❌ Connection Failed")
        st.caption(f"Could not reach engine at {API_URL}.")
        st.info("💡 **Tip:** If the backend is running, try switching the URL between `http://127.0.0.1:8000` and `http://localhost:8000` or disable your VPN.")
        st.code(f"Error detail: {str(e)}")
    except Exception as e:
        st.error(f"❌ unexpected Error: {str(e)}")
    
    st.divider()
    st.info("""
    **Recall Optimized**
    This model is calibrated to minimize false negatives, ensuring potential risks are flagged early.
    """)
    
    st.divider()
    st.markdown("### 🔗 Connect")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/MohammedBabaqi/DiaClassifier-Benchmarking-ML-Models)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/MohammedBabaqi)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/mohammedbabaqi/)")

    st.info("💡 **Local Run:** Download this repository to run the engine locally for faster performance.")

# Main UI Structure using Tabs
tab1, tab2 = st.tabs(["📋 Patient Assessment", "ℹ️ About the Model"])

with tab1:
    st.write("### Input Patient Clinical Profile")
    st.caption("Please fill in the details below. Most features are binary (Yes/No).")
    
    # Form for cleaner interaction
    with st.form("assessment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            with st.expander("🩺 Clinical & Medical History", expanded=True):
                high_bp = st.radio("High Blood Pressure?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)
                high_chol = st.radio("High Cholesterol?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)
                chol_check = st.checkbox("Cholesterol checked in last 5 years?", value=True)
                stroke = st.selectbox("History of Stroke?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
                heart_disease = st.selectbox("Heart Disease or Attack?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
                diff_walk = st.selectbox("Serious Difficulty Walking?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        
        with col2:
            with st.expander("🏃 Lifestyle & Environment", expanded=True):
                smoker = st.radio("Smoker?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)
                hvy_alcohol = st.radio("Heavy Alcohol Consumption?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True)
                phys_activity = st.checkbox("Physical activity in past 30 days?", value=True)
                gen_hlth = st.slider("General Health Rating", 1, 5, 3, help="1: Excellent ... 5: Poor")
                ment_hlth = st.number_input("Days of poor Mental Health (last 30)", 0, 30, 0)
                phys_hlth = st.number_input("Days of poor Physical Health (last 30)", 0, 30, 0)

        with st.expander("📊 Demographics & Metrics"):
            d_col1, d_col2, d_col3 = st.columns(3)
            with d_col1:
                bmi = st.number_input("BMI (Body Mass Index)", 10.0, 70.0, 25.0)
                sex = st.radio("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male", horizontal=True)
            with d_col2:
                age = st.slider("Age Group Category", 1, 13, 5, help="1=18-24, ... 13=80+")
                education = st.slider("Education Level", 1, 6, 4)
            with d_col3:
                income = st.slider("Income Level", 1, 8, 5)

        # Form Submit
        submitted = st.form_submit_button("� RUN ANALYSIS", use_container_width=True)

    # Result logic triggered by form submission
    if submitted:
        payload = {
            "HighBP": float(high_bp), "HighChol": float(high_chol), "DiffWalk": float(diff_walk),
            "HeartDiseaseorAttack": float(heart_disease), "PhysActivity": 1.0 if phys_activity else 0.0,
            "HvyAlcoholConsump": float(hvy_alcohol), "CholCheck": 1.0 if chol_check else 0.0,
            "Smoker": float(smoker), "Stroke": float(stroke), "Sex": float(sex),
            "BMI": float(bmi), "Age": float(age), "Income": float(income),
            "GenHlth": float(gen_hlth), "MentHlth": float(ment_hlth),
            "PhysHlth": float(phys_hlth), "Education": float(education)
        }

        try:
            with st.spinner("Analyzing data through XGBoost pipeline..."):
                response = requests.post(
                    f"{API_URL}/predict", 
                    json=payload,
                    proxies={'http': None, 'https': None}
                )
            
            if response.status_code == 200:
                res = response.json()
                prob = res['probability']
                risk_pct = prob * 100
                pred = res['prediction']
                threshold = res['threshold_used']
                
                st.divider()
                st.write("## 🧬 Diagnostic Output")
                
                r_col1, r_col2 = st.columns([1, 1])
                
                with r_col1:
                    if pred == 1:
                        st.error("### RISK DETECTED")
                        st.write(f"The model has flagged this profile as **High Risk** for Diabetes.")
                        st.warning("Immediate clinical review is recommended.")
                    else:
                        st.success("### NO RISK DETECTED")
                        st.write("Current clinical indicators suggest a **Low Risk** profile.")

                with r_col2:
                    # Metric with a delta showing distance from threshold
                    delta_val = prob - threshold
                    st.metric(
                        label="Confidence Score (Probability)", 
                        value=f"{risk_pct:.1f}%",
                        delta=f"{delta_val:+.2f} relative to threshold",
                        delta_color="inverse" if pred == 1 else "normal"
                    )
                    st.progress(prob)
                    st.caption(f"Engine used optimized decision threshold: **{threshold:.4f}**")

            else:
                st.error(f"Engine Error: {response.text}")
        except Exception as e:
            st.error(f"Connectivity Failure: Is the FastAPI engine running at {API_URL}?")

with tab2:
    st.write("### Model Intelligence Overview")
    st.markdown("""
    DiaClassifier uses an **XGBoost Classifier** that has been:
    1. **Preprocessed** with class balancing (SMOTEmoke).
    2. **Calibrated** to provide accurate probability estimates.
    3. **Threshold-Optimized** for Recall, prioritizing the detection of true diabetes cases.
    
    #### Required Features
    The model evaluates 17 key indicators including:
    - **Clinical**: BP, Cholesterol, Heart Disease, Stroke, Difficulty Walking.
    - **Lifestyle**: Smoking, Alcohol, Activity, General/Mental/Physical Health.
    - **Demographic**: BMI, Age, Sex, Education, Income.
    """)
    
    st.info("The frontend is built using **Native Streamlit** components for speed, reliability, and clean aesthetics.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d;">
    © 2026 DiaClassifier Professional Suite | Prepared by <b>Mohammed Babaqi</b><br>
    <a href="https://github.com/MohammedBabaqi/DiaClassifier-Benchmarking-ML-Models" target="_blank">Repository</a> | 
    <a href="https://github.com/MohammedBabaqi" target="_blank">GitHub</a> | 
    <a href="https://www.linkedin.com/in/mohammedbabaqi/" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
