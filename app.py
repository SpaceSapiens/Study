import streamlit as st

st.markdown("""
<style>
body {
    background-image: url("https://upload.wikimedia.org/wikipedia/en/thumb/6/69/IIT_Madras_Logo.svg/1200px-IIT_Madras_Logo.svg.png");
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

st.title('Find the Largest Number')

# Get user input for three numbers
num1 = st.number_input('Enter the first number:', value=0, step=1)
num2 = st.number_input('Enter the second number:', value=0, step=1)
num3 = st.number_input('Enter the third number:', value=0, step=1)

# Determine the largest number
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

# Display the largest number to the user
st.subheader(f'The largest number is {largest}.')
