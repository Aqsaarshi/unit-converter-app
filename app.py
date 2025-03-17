import streamlit as st  # type: ignore

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stTitle {
            color: #1E88E5;
            text-align: center;
        }
        .stMarkdown {
            text-align: center;
            font-size: 18px;
            color: #555;
        }
        .stButton button {
            background-color: #1E88E5;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #1565C0;
        }
        .stSelectbox {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("✨ Unit Converter App ✨")
st.markdown("### 🚀 Instantly Convert Length, Weight & Time")
st.write("Welcome! Select a category and enter your value below.")

# User selects category
category = st.selectbox("📌 Choose a category:", ["Length", "Weight", "Time"])

# Define unit options based on category
if category == "Length":
    unit = st.selectbox("🔄 Select Conversion:", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("🔄 Select Conversion:", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("🔄 Select Conversion:", ["Seconds to Minutes", "Minutes to Seconds",
                                                  "Minutes to Hours", "Hours to Minutes",
                                                  "Hours to Days", "Days to Hours"])

# Input value
value = st.number_input("🔢 Enter your value:", min_value=0.0, format="%.2f")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None  # In case of an invalid selection

# Convert button
if st.button("🔄 Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ The result is **{result:.2f}**")
    else:
        st.error("⚠ Invalid conversion")

