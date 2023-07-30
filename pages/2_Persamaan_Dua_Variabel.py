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
    
st.markdown("# <font color='#80ffb0'>Persamaan Dua Variabel</font>", unsafe_allow_html=True)
st.write('')
    
col = st.columns(2)
with col[0]: open_image("simultaneous-linear-equations.png")
with col[1]: st.write('**Persamaan 2 Variabel** adalah persamaan kompleks yang terdiri dari 2 variabel dan 2 baris. Tujuannya untuk mencari solusi x dan y.')
st.write('''Ada 6 variabel di persamaan 2 variabel, yaitu a, b, c, d, e, f.
    Variabel a dan d adalah gradien x, b dan e adalah gradien y, dan c dan f adalah konstanta.
    Barisan pertama terdiri dari variabel a, b, c; dan barisan kedua terdiri dari variabel d, e, f.
''')
st.write('### Rumus')
st.latex(r"ax + by = c\\dx + ey = f")

# st.latex(r"a \neq 0, a \neq 0, a \neq 0, d \neq 0")
st.write('### Masukkan angka')
st.write('Barisan pertama')
col1 = st.columns(3)
with col1[0]: a = float(st.text_input("a (Default: 1)", value=2))
with col1[1]: b = float(st.text_input("b (Default: 1)", value=1))
with col1[2]: c = float(st.text_input("c (Default: 5)", value=5))
st.write('Barisan kedua')
col2 = st.columns(3)
with col2[0]: d = float(st.text_input("d (Default: 3)", value=3))
with col2[1]: e = float(st.text_input("e (Default: -2)", value=-2))
with col2[2]: f = float(st.text_input("f (Default: 4)", value=4))

st.write('## Hasil Persamaan')

ruas_kiri_1 = fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(b)))}y"
ruas_kanan_1 = fungsi(c)
ruas_kiri_2 = fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}y"
ruas_kanan_2 = fungsi(f)
persamaan_1 = fr"{ruas_kiri_1} = {ruas_kanan_1}"
persamaan_2 = fr"{ruas_kiri_2} = {ruas_kanan_2}"
persamaan = fr"{persamaan_1}\\{persamaan_2}"
st.latex(persamaan)

st.write('## Hasil Penyelesaian')

try:
    # hasil_y = (d*c-a*f)/(d*b-a*e)
    # hasil_x = (c-b*hasil_y)/a
    hasil_y = (a*f-c*d)/(a*e-b*d)
    hasil_x = (c*e-b*f)/(a*e-b*d)

    st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
except:
    st.write("Ada yang bermasalah pada input persamaan")

    muncul_1 = False
    muncul_2 = False

if muncul_1:
    st.write('### **Langkah Penyelesaian**')

    jenis_list = ["Eliminasi", "Subsitusi", "Determinan"]
    jenis = st.selectbox("Pilih cara langkah penyelesaian:", jenis_list)

    if jenis == jenis_list[0]:
        nomor = 1
        st.write(f"### {nomor}")
        st.latex(fr"{persamaan}")
        nomor += 1
        st.write(f"### {nomor}")
        if step:
            st.write(f"Di Persamaan 1, kalikan kedua ruas dengan {fungsi(d)}")
            st.write(f"Di Persamaan 2, kalikan kedua ruas dengan {fungsi(a)}")
        st.latex(fr"{fungsi4(fungsi(d * a))}x {fungsi4(fungsi2(fungsi(d * b)))}y = {fungsi(d * c)}\\{fungsi4(fungsi(a * d))}x {fungsi4(fungsi2(fungsi(a * e)))}y = {fungsi(a * f)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Kurangkan persamaan atas dengan bawah")
        st.latex(fr"{fungsi4(fungsi(d * b))}y - {fungsi4(fungsi3(fungsi(a * e)))}y = {fungsi(d * c)} - {fungsi3(fungsi(a * f))}")
        st.latex(fr"{fungsi4(fungsi(d * b - a * e))}y = {fungsi(d * c - a * f)}")
        if fungsi(d * b - a * e) != 1:
            st.latex(fr"""\frac{{{fungsi(d * b - a * e)}}}{{{fungsi(d * b - a * e)}}} y = \frac{{{fungsi(d * c - a * f)}}}{{{fungsi(d * b - a * e)}}}""")
            st.latex(fr"y = {fungsi(hasil_y)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write(f"Subsitusikan y = {fungsi(hasil_y)} ke Persamaan 1")
        st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b))} \times {fungsi3(fungsi(hasil_y))} = {fungsi(c)}")
        st.latex(fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b * hasil_y))} = {fungsi(c)}")
        st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b * hasil_y))} - {fungsi3(fungsi(b * hasil_y))} = {fungsi(c)} - {fungsi3(fungsi(b * hasil_y))}")
        st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b * hasil_y)}")
        st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}} x = \frac{{{fungsi(c - b * hasil_y)}}}{{{fungsi(a)}}}")
        st.latex(fr"x = {fungsi(hasil_x)}")
        nomor += 1
        st.write(f"### {nomor}")
        st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

    if jenis == jenis_list[1]:
        nomor = 1
        st.write(f"### {nomor}")
        st.latex(fr"{persamaan}")
        nomor += 1
        st.write(f"### {nomor}")
        st.latex(fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(-a)))}x {fungsi4(fungsi2(fungsi(b)))}y = {fungsi4(fungsi(-a))}x {fungsi2(fungsi(c))}")
        nomor += 1
        st.write(f"### {nomor}")
        st.latex(fr"{fungsi4(fungsi(b))}y = {fungsi4(fungsi(-a))}x {fungsi2(fungsi(c))}")
        if fungsi(b) != 1:
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"\frac{{{fungsi(b)}}}{{{fungsi(b)}}}y = \frac{{{fungsi(-a)}}}{{{fungsi(b)}}}x {fungsi5(c)} \frac{{{fungsi(abs(c))}}}{{{fungsi(b)}}}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"y = {fungsi4(fungsi(-a / b))}x {fungsi2(fungsi(c / b))}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write(f"Subsitusikan y ke Persamaan 2")
        st.latex(fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}({fungsi4(fungsi(-a / b))}x {fungsi2(fungsi(c / b))}) = {fungsi(f)}")
        st.latex(fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e * -a / b)))}x {fungsi2(fungsi(e * c / b))} = {fungsi(f)}")
        st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x {fungsi2(fungsi(e * c / b))} = {fungsi(f)}")
        st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x {fungsi2(fungsi(e * c / b))} {fungsi2(fungsi(-e * c / b))} = {fungsi(f)} {fungsi2(fungsi(-e * c / b))}")
        st.latex(fr"{fungsi4(fungsi(d + e * -a / b))}x = {fungsi(f - e * c / b)}")
        if fungsi4(fungsi(d + e * -a / b)) != 1:
            st.latex(fr"\frac{{{fungsi(d + e * -a / b)}}}{{{fungsi(d + e * -a / b)}}}x = \frac{{{fungsi(f - e * c / b)}}}{{{fungsi(d + e * -a / b)}}}")
            st.latex(fr"x = {fungsi(hasil_x)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write(f"Subsitusikan x = {fungsi(hasil_x)} ke Persamaan 1")
        st.latex(fr"y = {fungsi3(fungsi(-a / b))} \times {fungsi3(fungsi(hasil_x))} {fungsi2(fungsi(c / b))}")
        st.latex(fr"y = {fungsi(-a / b * hasil_x)} {fungsi2(fungsi(c / b))}")
        st.latex(fr"y = {fungsi(hasil_y)}")
        nomor += 1
        st.write(f"### {nomor}")
        st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

    if jenis == jenis_list[2]:
        nomor = 1
        st.write(f"### {nomor}")
        st.latex(fr"{persamaan}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Ubah bentuk persamaan menjadi determinan")
        # st.latex(r"D = \begin{bmatrix}a & b\\c & d\end{bmatrix}")
        st.latex(fr"D = \begin{{bmatrix}}{fungsi(a)} & {fungsi(b)}\\{fungsi(d)} & {fungsi(e)}\end{{bmatrix}}")
        st.latex(fr"D_1 = \begin{{bmatrix}}{fungsi(c)} & {fungsi(b)}\\{fungsi(f)} & {fungsi(e)}\end{{bmatrix}}")
        st.latex(fr"D_2 = \begin{{bmatrix}}{fungsi(a)} & {fungsi(c)}\\{fungsi(d)} & {fungsi(f)}\end{{bmatrix}}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Gunakan rumus determinan")
        # st.latex(rf"D = ad - bc")
        st.latex(rf"D = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(d))}")
        st.latex(rf"D_1 = {fungsi3(fungsi(c))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(f))}")
        st.latex(rf"D_2 = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(f))} - {fungsi3(fungsi(c))} \times {fungsi3(fungsi(d))}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Hitungkan")
        st.latex(rf"D = {fungsi(a * e)} {fungsi2(fungsi(-b * d))}")
        st.latex(rf"D_1 = {fungsi(c * e)} {fungsi2(fungsi(-b * f))}")
        st.latex(rf"D_2 = {fungsi(a * f)} {fungsi2(fungsi(-c * d))}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Hitungkan")
        st.latex(rf"D = {fungsi(a*e-b*d)}")
        st.latex(rf"D_1 = {fungsi(c*e-b*f)}")
        st.latex(rf"D_2 = {fungsi(a*f-c*d)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Gunakan rumus persamaan dan determinan")
        st.latex(rf"x = \frac{{D_1}}{{D}} = \frac{{{fungsi(c*e-b*f)}}}{{{fungsi(a*e-b*d)}}}")
        st.latex(rf"y = \frac{{D_2}}{{D}} = \frac{{{fungsi(a*f-c*d)}}}{{{fungsi(a*e-b*d)}}}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Hitungkan")
        st.latex(rf"x = {fungsi(hasil_x)}")
        st.latex(rf"y = {fungsi(hasil_y)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Penyelesaian x dan y")
        st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

        # st.latex(r"a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)")
        # st.latex(rf"a + ar + a r^2 + a r^3 + \cdots + a r^{12-1} = \sum_{13}^{12-1} ar^k = a \left(\frac{31}{13}\right)")

if muncul_2:
    st.write('## **Grafik**')

    jarak = hasil_x - 5
    batas = hasil_x + 5
    ukuran = 0.01

    plt.style.use('seaborn-whitegrid')

    x = np.arange(jarak, batas + 1e-14, ukuran)
    plt.figure(figsize=(10,10))

    y1 = -a/b*x + c/b
    plt.plot(x,y1,lw=5,color='blue')

    y2 = -d/e*x + f/e
    plt.plot(x,y2,lw=5,color='green')

    plt.xlabel("x", size=20, )
    plt.ylabel("y",)
    plt.legend([persamaan_1, persamaan_2])

    plt.savefig('Preview.png')
    img = Image.open('Preview.png')
    st.image(img, width=500)

    with open("Preview.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="Grafik.png"
        )