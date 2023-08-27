import streamlit as st
import time

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

# Set page title and layout
st.set_page_config(page_title="Largest Number Finder", layout="wide")

# Define custom CSS for the background image
background_style = """
<style>
body {
    background-image: url('https://img.goodfon.com/original/1920x1080/8/70/anime-girl-sexy-bikini-drinking-poolside-hot.jpg');
    background-size: cover;
}
</style>
"""
# Insert the custom CSS using Markdown
st.markdown(background_style, unsafe_allow_html=True)

# Page header with animation
st.title("🔍 Find the Largest Number")
st.markdown("Enter three numbers and discover the **largest** among them.")

# Input fields for three numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

# Button with animation
if st.button("Find Largest"):
    with st.spinner("Calculating..."):
        time.sleep(2)  # Simulating calculation delay

    st.markdown("---")  # Divider for a clean transition

    # Check for equality
    if num1 == num2 == num3:
        st.error("All three numbers are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: **{largest}**")

        # Party emojis animation
        st.write("🎉🥳🎊")
import streamlit as st
import time

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

# Set page title and layout
st.set_page_config(page_title="Largest Number Finder", layout="wide")

# Define custom CSS for the background image
background_style = """
<style>
body {
    background-image: url('.jpg');
    background-size: cover;
}
</style>
"""
# Insert the custom CSS using Markdown
st.markdown(background_style, unsafe_allow_html=True)

# Page header with animation
st.title("🔍 Find the Largest Number")
st.markdown("Enter three numbers and discover the **largest** among them.")

# Input fields for three numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

# Button with animation
if st.button("Find Largest"):
    with st.spinner("Calculating..."):
        time.sleep(2)  # Simulating calculation delay

    st.markdown("---")  # Divider for a clean transition

    # Check for equality
    if num1 == num2 == num3:
        st.error("All three numbers are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: **{largest}**")

        # Party emojis animation
        st.write("🎉🥳🎊")
