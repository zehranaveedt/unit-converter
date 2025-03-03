import streamlit as st

st.title("🔄 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("🚀 Welcome to Unit Converter! Easily convert between different units with just a few taps. 🌍📏")

#
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":  
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time": 
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24 


def get_user_input(category):
    if category == "Length":
        unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers"])
    elif category == "Weight":
        unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
    elif category == "Time":
        unit = st.selectbox("⏲ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
    
    value = st.number_input("Enter the value to convert", min_value=0.0)
    return value, unit


value, unit = get_user_input(category)


if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The Result is {result:.2f}")
