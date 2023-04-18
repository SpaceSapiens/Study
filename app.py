import streamlit as st

# Set background color and image
page_bg_img = '''
<style>
body {
background-image: url("https://gumlet.assettype.com/swarajya%2F2021-12%2F886904c7-7e9f-4933-a9e9-121d1c4b7cb5%2F3191ce98_5936_4228_a8ac_462050554f0d.jpg?q=75&auto=format%2Ccompress&w=400&dpr=2.6");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

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
