# Persamaan Linear

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

# st.write('# Bangun Datar') #ffd080
# st.markdown("# <font color='#ffd080'>Equation Solver</font> 🧊", unsafe_allow_html=True)
st.markdown("# <font color='#80ffb0'>Persamaan Linear</font>", unsafe_allow_html=True)
st.write('')

col = st.columns(2)
with col[0]: open_image("Linear Equation.png")
with col[1]: st.write('**Persamaan Linear** adalah persamaan dengan garis yang lurus dalam grafik. Rumusnya adalah ax+b=c.')
st.write('Ada 3 variabel di persamaan linear, yaitu a, b, c. Variabel a disebut juga gradien, sedangkan b dan c adalah konstanta.')
# st.write()

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

st.write('### Rumus')
# st.latex(r"ax + b = c")
st.latex(r"ax + b = c\text{, dengan } a \neq 0")
# st.latex(r"a \neq 0")
st.write('### Masukkan angka')
# abc = '$2x+1=5$'
example_list = ['Contoh 1', 'Contoh 2', 'Contoh 3']
# example = st.radio('Pilih opsi2', example_list)
if example_check:
    example = st.radio('Pilih contoh', example_list)
else:
    example = example_list[0]

if example == example_list[0]:
    value = [2,1,5]
    if example_check: st.write(f"{example}: $2x+1=5$")
if example == example_list[1]:
    value = [3,-1,4]
    st.write(f"{example}: $3x-1=4$")
if example == example_list[2]:
    value = [5,2,8]
    st.write(f"{example}: $5x+2=8$")

col = st.columns(3)

with col[0]: a = float(st.text_input("a (Default: 2)", value=value[0]))
with col[1]: b = float(st.text_input("b (Default: 1)", value=value[1]))
with col[2]: c = float(st.text_input("c (Default: 5)", value=value[2]))

st.write('## Hasil Persamaan')

ruas_kiri = fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b))}"
ruas_kanan = fungsi(c)

hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

st.latex(hasil_persamaan)

st.write('## Hasil Penyelesaian')

try:
    hasil = (c - b) / a
    rec1, rec2, rec3 = reciprocal2(int(c-b),int(a))
    rec21, rec22, rec23 = reciprocal3(int(c-b),int(a))
    # print(rec2)
    if rec3 == 1:
        st.latex(f"x = {fungsi(hasil)}")
    else:
        if rec21 == 0:
            st.latex(fr"x = {rec1}\frac{{{rec2}}}{{{rec3}}} {apx(hasil)} {fungsi(hasil)}")
        else:
            st.latex(fr"x = {rec1}\frac{{{rec2}}}{{{rec3}}} = {rec21}\frac{{{rec22}}}{{{rec23}}} {apx(hasil)} {fungsi(hasil)}")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
except:
    st.write("Ada yang bermasalah pada input persamaan")
    if a == 0:
        st.write("Variabel a tidak sama dengan 0")

    muncul_1 = False
    muncul_2 = False

if muncul_1:
    st.write('## Langkah Penyelesaian')

    nomor = 1
    st.write(f"### {nomor}")
    if step: st.write("Siapkan inputnya")
    st.latex(fr"{hasil_persamaan}")
    nomor += 1
    st.write(f"### {nomor}")
    if step: st.write("Buatlah pengurangan ruas kiri dan kanan")
    st.latex(fr"{ruas_kiri} - {fungsi(b)} = {ruas_kanan} - {fungsi(b)}")
    nomor += 1
    st.write(f"### {nomor}")
    if step: st.write("Kurangkan kedua ruas")
    st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b)}")
    if fungsi(a) != 1:
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Buatlah pembagian ruas kiri dan kanan")
        st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}}x = \frac{{{fungsi(c - b)}}}{{{fungsi(a)}}}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Bagikan kedua ruas")
        st.latex(fr"x = {fungsi(hasil)}")

if muncul_2:
    st.write('## Grafik')

    jarak = -5
    batas = 5
    ukuran = 0.01

    plt.style.use('seaborn-whitegrid')

    x = np.arange(jarak, batas + 1e-14, ukuran)
    plt.figure(figsize=(10,10))

    y1 = a*x + b
    plt.plot(x,y1,lw=5,color='blue')

    y2 = 0*x + c
    plt.plot(x,y2,lw=5,color='green')

    plt.xlabel("x",)
    plt.ylabel("y",)
    #plt.title("Grafik Penyelesaian", size=20)
    plt.legend([ruas_kiri, ruas_kanan])

    plt.savefig('Preview.png')
    img = Image.open('Preview.png')
    st.image(img, width=500)

    with open("Preview.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="Grafik.png"
        )
