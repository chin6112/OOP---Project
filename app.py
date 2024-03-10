import streamlit as st
import random
import string
from PIL import Image
import base64

bg_image_path = "HeavenBurnsRed 14_2_2566 21_53_48.png"
with open(bg_image_path, "rb") as img_file:
    bg_image = img_file.read()
bg_image_base64 = base64.b64encode(bg_image).decode()
page_bg_img = f'''
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
        }}
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def random_number_generator(min_value, max_value):
    return random.randint(min_value, max_value)

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_float(min_value, max_value,decimal_places):
    random_num = round(random.uniform(min_value, max_value),decimal_places)
    return "{:.{}f}".format(random_num, decimal_places)

def random_sequence(length, min_value, max_value, number):
    return [random.randint(min_value, max_value) for _ in range(number)]

def main():
    menu1 = ["Number", "String", "Float", "Sequence"]
    choice = st.sidebar.selectbox('Menu', menu1)
    
    if choice == 'Number':
        st.title("```Random Number Generator```")
        # Sidebar
        st.sidebar.header("Settings")
        min_value = st.sidebar.number_input("Minimum Value", min_value=0, max_value=1000, value=0)
        max_value = st.sidebar.number_input("Maximum Value", min_value=0, max_value=1000, value=100)
        # Generate random number button
        if st.button("Generate Random Number"):
            random_number = random_number_generator(min_value, max_value)
            st.write(f"```Random Number: {random_number}```")

    if choice == 'String':
        st.title("```Random String Generator```")
        Number = st.sidebar.number_input("Number", min_value=0, max_value=1000,value=0)
        # สร้างตัวอักษรสุ่ม
        if st.button("Generate Random String"):
            random_str = random_string(Number)  # สร้างสตริงที่มีความยาว 10 ตัว
            st.write(f"```Random String: {random_str}```")

    if choice == 'Float':
        st.title("```Random Float Generator```")
        st.sidebar.header("Settings")
        min_value = st.sidebar.number_input("Minimum Value", min_value=0, max_value=1000, value=0)
        max_value = st.sidebar.number_input("Maximum Value", min_value=0, max_value=1000, value=100)
        decimal_places = st.sidebar.number_input("Decimal Places", min_value=0, max_value=10, value=2)

        if st.button("Generate Random Float"):
            random_float_num = random_float(min_value, max_value,decimal_places)  # สร้างตัวเลขทศนิยมในช่วง 0.0 ถึง 1.0
            st.write(f"```Random Float: {random_float_num}```")

    if choice == 'Sequence':
        st.title("```Random Sequence Generator```")
        # Sidebar
        st.sidebar.header("Settings")
        min_value = st.sidebar.number_input("Minimum Value", min_value=0, max_value=1000, value=0)
        max_value = st.sidebar.number_input("Maximum Value", min_value=0, max_value=1000, value=100)
        number = st.sidebar.number_input("Number", min_value=0, max_value=1000, value=0)

        if st.button("Generate Random Sequence"):
            random_seq = random_sequence(number, min_value, max_value, number)
            st.write(f"```Random Sequence: {random_seq}```")

if __name__ == "__main__":
    main()
