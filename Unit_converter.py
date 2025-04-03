import streamlit as st

def converter_units(value, unit_from, unit_to):
    conversations = {
        "meter": 1,  
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "micrometer": 1e-6,
        "nanometer": 1e-9,
        "mile": 1609.34
    }
    
    if unit_from in conversations and unit_to in conversations:
        conversion = value * (conversations[unit_from] / conversations[unit_to])
        return conversion
    else:
        return "Conversion not supported"

st.title("Unit Converter")

value = st.number_input("Enter the value:", min_value=0.0, step=0.1)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile"])

if st.button("Convert"):
    result = converter_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")
