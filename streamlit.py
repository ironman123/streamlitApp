import streamlit as st
import time

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

# Set page title and layout
st.set_page_config(page_title="Largest Number Finder", layout="centered")

# Page header with animation
st.title("🔍 Find the Largest Number")
st.markdown("Enter three numbers and discover the **largest** among them.")

# Input fields for three numbers
num1 = st.number_input("Enter the First number:")
num2 = st.number_input("Enter the Second number:")
num3 = st.number_input("Enter the Third number:")

# Button with animation
if st.button("Find The Largest!"):
    with st.spinner("Calculating....."):
        time.sleep(1)  # Simulating calculation delay

    st.markdown("---")  # Divider for a clean transition

    # Check for equality
    if num1 == num2 == num3:
        st.error("All three are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: **{largest}**")

        # Animated emoji
        st.write("🎉🥳🎊")
