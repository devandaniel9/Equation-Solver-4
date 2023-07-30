# Equation Solver

# List import
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import math
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(
    page_title="Equation Solver 4",
    page_icon="🧊",
)

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 15}

plt.rc('font', **font)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

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

def lisp(baris):
    hasil = baris.split(' ')
    return hasil[-1]

def check(text):
    text2 = list(text)[0]
    if text2 == 'T': return True
    else: return False

file = open("data.txt", "r")
baris = file.readlines()

digit = int(lisp(baris[0]))
example_check = check(lisp(baris[1]))
step = check(lisp(baris[2]))

from functions import *

# Konversi float ke int, contoh: 3.0 menjadi 3, 3.2 menjadi 3.2
def fungsi(angka):
    a = round(angka, digit)
    # if round(angka, digit) == round(angka, 0):
    if a == round(angka, 0):
        angka = int(a)
    else:
        angka = a
   
    return angka

def apx(hasil):
    if abs(hasil-fungsi(hasil)) < 1e-10:
        return '='
    else:
        return '\x5capprox'
    
st.markdown("# <font color='#80ffb0'>Persamaan Eksponensial</font>", unsafe_allow_html=True)
st.write('**Belum Selesai**')
st.write('')

col = st.columns(2)
with col[0]: open_image("exponential-equation.png")
with col[1]: st.write('**Persamaan Eksponensial** adalah persamaan dengan garis yang naik secara eksponensial. Rumusnya adalah a^(bx+c)=d.')
st.write('''Ada 4 variabel di persamaan eksponensial, yaitu a, b, c, d.
    Variabel a dan d adalah gradien x, b dan e adalah gradien y, dan c dan f adalah konstanta.
    Barisan pertama terdiri dari variabel a, b, c; dan barisan kedua terdiri dari variabel d, e, f.
''')
st.write('### **Rumus**')
st.latex(r"a^{bx+c} = d\text{, dengan } a, b \neq 0")
# st.latex(r"a \neq 0")
st.write('### **Masukkan angka**')
example_list = ['Contoh 1', 'Contoh 2', 'Contoh 3', 'Contoh 4', 'Contoh 5']
# example = st.radio('Pilih opsi2', example_list)
if example_check:
    example = st.radio('Pilih contoh', example_list)
else:
    example = example_list[0]

if example == example_list[0]:
    value = [2,1,0,8]
    if example_check: st.write(f"{example}: $2^x=8$")
if example == example_list[1]:
    value = [3,2,1,27]
    st.write(f"{example}: $3^{{2x+1}}=27$")
if example == example_list[2]:
    value = [4,2,3,128]
    st.write(f"{example}: $4^{{2x+3}}=128$")
if example == example_list[3]:
    value = [3,1,0,-1]
    st.write(f"{example}: $3^{{x+1}}=-1$")
if example == example_list[4]:
    value = [5,1,-1,2]
    st.write(f"{example}: $5^{{x-1}}=2$")

st.write('\n')
col1 = st.columns([3,1])
with col1[0]: st.write('##### **Ruas kiri**')
with col1[1]: st.write('##### **Ruas kanan**')
col2 = st.columns(4)
# with col2[0]: a = float(st.text_input("a (Default: 2)", value=value[0]))
with col2[0]: a = int(st.text_input("a (Default: 2)", value=value[0]))
with col2[1]: b = int(st.text_input("b (Default: 1)", value=value[1]))
with col2[2]: c = int(st.text_input("c (Default: 1)", value=value[2]))
with col2[3]: d = int(st.text_input("d (Default: 8)", value=value[3]))

st.write('## **Hasil Persamaan**')

# ruas_kiri = fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))}"
ruas_kiri = fr"{fungsi(a)}^{{{fungsi4(fungsi(b))}x {fungsi2(fungsi(c))}}}"
if c == 0:
    ruas_kiri += fr" = {fungsi(a)}^{{{fungsi4(fungsi(b))}x {fungsi6(fungsi(c))}}}"
ruas_kanan = f"{fungsi(d)}"
hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

st.latex(hasil_persamaan)

st.write('## Hasil Penyelesaian')

try:    
    if d > 0:
        hasil_log = np.log(d)/np.log(a)
        hasil = (hasil_log-c)/b

        rec = reciprocal(fungsi(hasil_log)-c,b)

        if fungsi(hasil_log) == int(hasil_log):
            st.latex(fr"x = \frac{{{rec[0]}}}{{{rec[1]}}}")
    else:
        st.write("x = Tidak ada")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
except:
    st.write("Ada yang bermasalah pada input persamaan")
    if a == 0:
        st.write("Variabel a tidak sama dengan 0")

    muncul_1 = False
    muncul_2 = False