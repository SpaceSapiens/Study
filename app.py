import streamlit as st

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
st.write(f'The largest number is {largest}.')
