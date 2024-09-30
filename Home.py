# Equation Solver 4

# List import
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import math
# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# from streamlit_modal import Modal

# Menjalankan program
# streamlit run 'Equation Solver 4 - 2.py'
# streamlit run Home.py

# @import fonts/Roboto-Regular.ttf;

st.set_page_config(
    page_title="Equation Solver 4",
    page_icon="🧊",
)

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 15}

plt.rc('font', **font)

aaa = """
<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}

    [data-testid="stSidebar"] {
        background-color: #ffffff20;
    }
</style>
"""

def color(text, c):
    return f"<font color={c}>{text}</font>"

# st.markdown(streamlit_style, unsafe_allow_html=True)
# st.write(f"The next word is {color('red','yellow')}", unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

t = """
<div>Hello there my
<span class='blue'>yo</span>"""

# st.markdown(t, unsafe_allow_html=True)

# Buka gambar
def open_image(nama):
    try:
        img2 = Image.open(f'images/{nama}')
        wid, hgt = img2.size
        # im = Image.new('RGB', (resolution,resolution))
        img = Image.new('RGB', size=(wid,hgt), color='white')
        draw = ImageDraw.Draw(img)
        # img = Image.open(f"{bentuk}.png")
        img.paste(img2)
        # st.image(img, width=200)
        st.image(img, width=320)
    except FileNotFoundError:
        img = ""

# Streamlit
# st.title('Equation Solver')
st.markdown("# <font color='#80ffb0'>Equation Solver</font> 🧊", unsafe_allow_html=True)
# st.write('#### **Made by Devan Daniel - Kelas 8 Betania**')
st.write('**Made by Devan Daniel - Kelas 9**')
st.write('')
stw(f"**{color('Equation Solver','#a0ff60')}** adalah persamaan matematika yang bertujuan untuk menyelesaikan persamaan dari variabelnya.")
st.markdown('''
- Program ini dapat menyelesaikan persamaan **Linear**, **2 Variabel**, dan **Kuadrat**
- Program ini juga dapat menampilkan langkah penyelesaian dan grafik solusi dari soal
- Silahkan masukkan jenis persamaan dan variabelnya di menu bawah
- Agar bisa melihat informasi, klik tombol informasi program ini

Version: 1.4.1<br>
Last updated: 30 Sept 2024 (Untuk dapat mengakses link ini)
Last updated: 31 Juli 2023 (Perubahan isi program ini)

<style>
.myDiv {
  background-color: #805030;
  padding: 10px;
}
</style>
<div class="myDiv">
<font size=4><b>Link:</b></font>
<br>
Link website saya:<br>
<a href=https://devandaniel9.github.io/index.html>Website Saya</a><br>
Link program geometri:<br>
<a href=https://devandaniel9-geometry-3.streamlit.app/>Program Geometri</a>
</div>
''', unsafe_allow_html=True)

# st.info('This is a purely informational message', )

# st.download

def add_bg_from_local(image_file):
    import base64
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local('background.jpg')

st.write('')

st.write('## **Pengaturan**')

# lisp = line_split

def lisp(baris):
    hasil = baris.split(' ')
    return hasil[-1]

def check(text):
    # if text == 'True' or text == 'true': return True
    text2 = list(text)[0]
    if text2 == 'T': return True
    else: return False

file = open("data.txt", "r")
baris = file.readlines()

digit_default = int(lisp(baris[0]))
example_default = check(lisp(baris[1]))
step_check = check(lisp(baris[2]))
# print(f"{check(lisp(baris[3]))}aaa")
# st.write(bool('hahaha'))

st.write('### **Digit Precision**')
digit = int(st.number_input("Digit (2-10)", value=digit_default, min_value=2, max_value=10))
st.write('### **Contoh Soal**')
example_check = st.checkbox(label="Dengan contoh", value=example_default)
st.write('### **Langkah Penyelesaian**')
step = '''step_list = ['Tidak ada penjelasan', 'Dengan penjelasan']
step = st.radio('Pilih opsi', step_list)
step_check'''
step = st.checkbox(label="Dengan penjelasan", value=step_check)

# st.write('### **Lanjutan**')
# st.write('[Coming Soon]')
st.write('### **Reset**')
st.write('Reset Settings untuk mengembalikan pengaturan ke semula')
reset = st.button('Reset Settings', key='RunBtn', on_click=None)
if reset:
    file = open("data_default.txt", "r")
    baris = file.readlines()
    # st.write(baris)
    # st.write(lisp(baris[0]))
    file2 = open("data.txt", "w")
    teks = f"""digit_default: {lisp(baris[0])}example_default: {lisp(baris[1])}step_check: {lisp(baris[2])}
    """
    file2.write(teks)

teks = f"""digit_default: {digit}
example_default: {example_check}
step_check: {step}
"""

# st.write(teks)

file = open("data.txt", "w")
file.write(teks)
file = open("data.txt", "r")

# st.write('a')

# st.chat_input("Your message")
# st.chat_message("user")
