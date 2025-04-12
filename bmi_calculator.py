import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to right, #ff66ff, #d966ff, #99ffff);
        color: white;
    }
    .main {
        color: #3f4bf6;
            }
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    .stButton > button {
        background-color: #4b33ff;
        color: white
        border-radius: 12px;
        padding: 0.5em 1em;
        transition: 0.3s;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #ff6666;
        transform: scale(1.05);
        color: #fff;
    }
    .stNumberInput label {
        font-weight: bold;
        font-size: 16px;
        color: #000066;
    }
    </style>
""", unsafe_allow_html=True)

# App Title and Description with Emojis
st.title("💪 BMI Calculator 🧮")
st.write("📏 Enter your **height** and **weight** to calculate your BMI!")

# Inputs
height = st.number_input(
    "📏 Height (in meters)", min_value=0.5, max_value=4.0, value=1.75
)
weight = st.number_input(
    "⚖️ Weight (in kilograms)", min_value=10, max_value=90, value=70
)

# Button
if st.button("✨ Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"🎯 Your BMI is **{bmi:.2f}**")

        # BMI Categories with emojis
        if bmi < 18.5:
            st.warning("🥗 You are underweight. Consider a nutritious diet!")
        elif 18.5 <= bmi < 24.9:
            st.success("🏋️ You have a normal weight. Keep it up!")
        elif 25 <= bmi < 29.9:
            st.warning("🍔 You are overweight. Some exercise could help!")
        else:
            st.error("🚨 You are obese. Consider consulting a healthcare professional.")
    else:
        st.error("⚠️ Please enter valid height and weight values.")
