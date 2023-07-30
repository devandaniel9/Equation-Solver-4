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
    
st.markdown("# <font color='#80ffb0'>Persamaan Kuadrat</font>", unsafe_allow_html=True)
st.write('')

col = st.columns(2)
with col[0]: open_image("quadratic-formula.png")
with col[1]: st.write('**Persamaan Kuadrat** adalah persamaan dengan garis yang melengkung dalam grafik. Persamaan ini bisa membentuk parabola. Rumusnya adalah ax^2+bx+c=0.')
st.write('''Ada 6 variabel di persamaan 2 variabel, yaitu a, b, c, d, e, f.
    Variabel a dan d adalah gradien x, b dan e adalah gradien y, dan c dan f adalah konstanta.
    Barisan pertama terdiri dari variabel a, b, c; dan barisan kedua terdiri dari variabel d, e, f.
''')
st.write('### Rumus')
st.latex(r"ax^2 + bx + c = 0\text{, dengan } a \neq 0")
# st.latex(r"a \neq 0")

with st.expander("Tampilkan rumus lebih banyak"):
    st.write('### Mencari Variabel x')
    # g1 = fr"\sqrt{{{fungsi3(fungsi(b))}^2 - 4 \times {fungsi3(fungsi(a))} \times {fungsi3(fungsi(c))}}}"
    st.latex(r"x_{1,2} = \frac{-b\pm\sqrt{b^2-4ac}}{2a}")
    st.write('### Diskriminan')
    st.latex(r"D = b^2-4ac")
    st.write('### Jumlah Solusi')
    st.write('Jumlah solusi 2, jika D > 0')
    st.write('Jumlah solusi 1, jika D = 0')
    st.write('Jumlah solusi 0, jika D < 0')
    st.write('### Titik Puncak')
    st.latex(r"x = -\frac{b}{2a}")
    st.latex(r"y = -\frac{b^2-4ac}{4a}")
    # st.latex(fr"y = -\frac{{{fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}}}{{4 \times {fungsi(a)}}}")

st.write('### Masukkan angka')
example_list = ['Contoh 1', 'Contoh 2', 'Contoh 3', 'Contoh 4', 'Contoh 5']
# example = st.radio('Pilih opsi2', example_list)
if example_check:
    example = st.radio('Pilih contoh', example_list)
else:
    example = example_list[0]

if example == example_list[0]:
    value = [1,3,2]
    if example_check: st.write(f"{example}: $x^2+3x+2=0$")
if example == example_list[1]:
    value = [2,-5,2]
    st.write(f"{example}: $2x^2-5x+2=0$")
if example == example_list[2]:
    value = [6,-7,-3]
    st.write(f"{example}: $6x^2-7x-3=0$")
if example == example_list[3]:
    value = [1,3,3]
    st.write(f"{example}: $x^2+x+3=0$")
if example == example_list[4]:
    value = [4,-12,9]
    st.write(f"{example}: $4x^2-12x+9=0$")

col = st.columns(3)
with col[0]: a = float(st.text_input("a (Default: 1)", value=value[0]))
with col[1]: b = float(st.text_input("b (Default: 3)", value=value[1]))
with col[2]: c = float(st.text_input("c (Default: 2)", value=value[2]))

st.write('## Hasil Persamaan')

ruas_kiri = fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))}"
ruas_kanan = "0"

hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

st.latex(hasil_persamaan)

st.write('## Hasil Penyelesaian')

try:
    # Hasil Penyelesaian
    d = b ** 2 - 4 * a * c

    # Hasil 2 Solusi
    hasil_x1 = (-b + d ** 0.5) / (2 * a)
    hasil_x2 = (-b - d ** 0.5) / (2 * a)

    # Mencari Jumlah Solusi
    if d > 0: e = 2
    elif d == 0: e = 1
    elif d < 0: e = 0

    # Titik Puncak
    f1 = -b / (2*a)
    f2 = -b**2 / (4*a) + c
    
    # st.write(d)
    
    if d < 0:
        check_rec = False
    else:
        check_rec = int(d**0.5+1e-10) == fungsi(d**0.5)

    # st.write(check_rec)

    if check_rec:
        rec = reciprocal(int(-b+round(d**0.5,10)),int(2*a))
        rec2 = reciprocal(int(-b-round(d**0.5,10)),int(2*a))
        rec_a = reciprocal2(int(-b+round(d**0.5,10)),int(2*a))
        rec_b = reciprocal3(int(-b+round(d**0.5,10)),int(2*a))
        rec2_a = reciprocal2(int(-b-round(d**0.5,10)),int(2*a))
        rec2_b = reciprocal3(int(-b-round(d**0.5,10)),int(2*a))

    # st.write(rec_a)

    # Solusi
    if d < 0:
        st.write("x = Tidak ada")
    else:
        if fungsi(hasil_x1) == fungsi(hasil_x2):
            if check_rec:
                st.latex(fr"x = {rec_a[0]}\frac{{{rec_a[1]}}}{{{rec_a[2]}}} {apx(hasil_x1)} {fungsi(hasil_x1)}")
            else:
                st.latex(fr"x = {fungsi(hasil_x1)}")
        else:
            if check_rec:
                if rec_a[2] == 1:
                    st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                elif rec_b[0] == 0:
                    st.latex(fr"x_1 = {rec_a[0]}\frac{{{rec_a[1]}}}{{{rec_a[2]}}} {apx(hasil_x1)} {fungsi(hasil_x1)}")
                else:
                    st.latex(fr"x_1 = {rec_a[0]}\frac{{{rec_a[1]}}}{{{rec_a[2]}}} = {rec_b[0]}\frac{{{rec_b[1]}}}{{{rec_b[2]}}} {apx(hasil_x1)} {fungsi(hasil_x1)}")

                if rec2_a[2] == 1:
                    st.latex(fr"x_2 = {fungsi(hasil_x2)}")
                elif rec2_b[0] == 0:
                    st.latex(fr"x_2 = {rec2_a[0]}\frac{{{rec2_a[1]}}}{{{rec2_a[2]}}} {apx(hasil_x2)} {fungsi(hasil_x2)}")
                else:
                    st.latex(fr"x_2 = {rec2_a[0]}\frac{{{rec2_a[1]}}}{{{rec2_a[2]}}} = {rec2_b[0]}\frac{{{rec2_b[1]}}}{{{rec2_b[2]}}} {apx(hasil_x2)} {fungsi(hasil_x2)}")
            else:
                st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                st.latex(fr"x_2 = {fungsi(hasil_x2)}")
    
    st.write(f"Diskriminan = {fungsi(d)}")
    st.write(f"Jumlah Solusi = {fungsi(e)}")
    # st.write(f"Titik Puncak = $({fungsi(f1)}, {fungsi(f2)})$")
    rec_f1 = reciprocal2(int(-b),int(2*a))
    rec_f2 = reciprocal2(int(-b**2+4*a*c),int(4*a))
    st.write(fr"Titik Puncak = $({rec_f1[0]}\frac{{{rec_f1[1]}}}{{{rec_f1[2]}}}, {rec_f2[0]}\frac{{{rec_f2[1]}}}{{{rec_f2[2]}}})$ = $({fungsi(f1)}, {fungsi(f2)})$")
    st.write("")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
except:
    st.write("Ada yang bermasalah pada input persamaan")

    muncul_1 = False
    muncul_2 = False

if muncul_1:
    st.write('## Langkah Penyelesaian')

    jenis_list = ["Selesaikan persamaan kuadrat", "Hitung diskriminan", "Jumlah solusi", "Titik puncak"]
    jenis = st.selectbox("Pilih jenis langkah penyelesaian:", jenis_list)

    if jenis == jenis_list[0]:
        jenis_2_list = ["Rumus kuadrat", "Kuadrat sempurna", "Pemfaktoran"]
        jenis_2 = st.selectbox("Pilih cara langkah penyelesaian:", jenis_2_list)

        if jenis_2 == jenis_2_list[0]:
            g1 = fr"\sqrt{{{fungsi3(fungsi(b))}^2 - 4 \times {fungsi3(fungsi(a))} \times {fungsi3(fungsi(c))}}}"
            g2 = fr"\sqrt{{{fungsi(b ** 2)} {fungsi2(fungsi(-4 * a * c))}}}"
            g3 = fr"\sqrt{{{fungsi(d)}}}"

            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            # st.write(f"Gunakan rumus persamaan kuadrat<br><a href=""#mencari-variabel-x"">(Klik rumusnya)</a>", unsafe_allow_html=True)
            if step: st.write(f"Gunakan rumus persamaan kuadrat")
            st.latex(fr"x_{{1,2}} = \frac{{-{fungsi3(fungsi(b))}\pm{g1}}}{{2 \times {fungsi3(fungsi(a))}}}")
            nomor += 1
            st.write(f"### {nomor}")
            if step: st.write(f"Hitungkan")
            st.latex(fr"x_{{1,2}} = \frac{{{fungsi(-b)}\pm{g2}}}{{{fungsi(2 * a)}}}")
            nomor += 1
            st.write(f"### {nomor}")
            if step: st.write(f"Hitungkan")
            st.latex(fr"x_{{1,2}} = \frac{{{fungsi(-b)}\pm{g3}}}{{{fungsi(2 * a)}}}")
            if fungsi(d) >= 0:
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write(f"Hitung akar")
                st.latex(fr"x_{{1,2}} = \frac{{{fungsi(-b)}\pm{fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write(f"Variabel x diubah menjadi 2 solusi yang berbeda")
                st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write(f"Hitungkan")
                st.latex(fr"x_1 = \frac{{{fungsi(-b + d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b - d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write(f"Hasil")
                st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                st.latex(fr"x_2 = {fungsi(hasil_x2)}")
                if fungsi(hasil_x1) == fungsi(hasil_x2):
                    nomor += 1
                    st.write(f"### {nomor}")
                    if step: st.write(f"Hasil")
                    st.latex(fr"x = {fungsi(hasil_x1)}")
            else:
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write("Hasil")
                st.latex(r"x \notin \R")
                st.write("x = Tidak ada")

        if jenis_2 == jenis_2_list[1]:
            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))} {fungsi2(fungsi(-c))} = 0 {fungsi2(fungsi(-c))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x = {fungsi(-c)}")
            if a != 1:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}}x^2 {fungsi5(b)} \frac{{{fungsi(abs(b))}}}{{{fungsi(a)}}}x = \frac{{{fungsi(-c)}}}{{{fungsi(a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x^2 {fungsi4(fungsi2(fungsi(b / a)))}x = {fungsi(-c / a)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"x^2 {fungsi4(fungsi2(fungsi(b / a)))}x + {fungsi(b**2 / (4*a**2))} = {fungsi(-c / a)} + {fungsi(b**2 / (4*a**2))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"(x {fungsi2(fungsi(b / (2*a)))})^2 = {fungsi(-c / a + b**2 / (4*a**2))}")
            if fungsi(d) > 0:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x_1 {fungsi2(fungsi(b / (2*a)))} = {fungsi((-c / a + b**2 / (4*a**2))**0.5)}")
                st.latex(fr"x_2 {fungsi2(fungsi(b / (2*a)))} = {fungsi(-(-c / a + b**2 / (4*a**2))**0.5)}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x_1 {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = {fungsi((-c / a + b**2 / (4*a**2))**0.5)} {fungsi2(fungsi(-b / (2*a)))}")
                st.latex(fr"x_2 {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = {fungsi(-(-c / a + b**2 / (4*a**2))**0.5)} {fungsi2(fungsi(-b / (2*a)))}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                st.latex(fr"x_2 = {fungsi(hasil_x2)}")
            elif fungsi(d) == 0:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x {fungsi2(fungsi(b / (2*a)))} = 0")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x {fungsi2(fungsi(b / (2*a)))} {fungsi2(fungsi(-b / (2*a)))} = 0 {fungsi2(fungsi(-b / (2*a)))}")
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"x = {fungsi(hasil_x1)}")
            else:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(r"x \notin \R")
                st.write("x = Tidak ada")

        if jenis_2 == jenis_2_list[2]:
            nomor = 1
            st.write(f"### {nomor}")
            st.latex(fr"{hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}")
            if step: st.write("Ubah menjadi bentuk penjumlahan")
            st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(-rec[1]*rec2[0])))}x {fungsi4(fungsi2(fungsi(-rec[0]*rec2[1])))}x {fungsi2(fungsi(c))} = 0")
            nomor += 1
            st.write(f"### {nomor}")
            if step: st.write("Faktorkan dua-duanya")
            st.latex(fr"{fungsi4(fungsi(rec[1]))}x ({fungsi4(fungsi(rec2[1]))}x {fungsi2(fungsi(-rec2[0]))}) {fungsi2(fungsi(-rec[0]))} ({fungsi4(fungsi(rec2[1]))}x {fungsi2(fungsi(-rec2[0]))}) = 0")
            nomor += 1
            st.write(f"### {nomor}")
            if step: st.write("Faktorkan")
            st.latex(fr"({fungsi4(fungsi(rec[1]))}x {fungsi2(fungsi(-rec[0]))}) ({fungsi4(fungsi(rec2[1]))}x {fungsi2(fungsi(-rec2[0]))}) = 0")
            if fungsi(hasil_x1) == fungsi(hasil_x2):
                nomor += 1
                st.write(f"### {nomor}")
                if step: st.write("Ubah menjadi kuadrat")
                st.latex(fr"({fungsi4(fungsi(rec[1]))}x {fungsi2(fungsi(-rec[0]))})^2 = 0")

                # st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))} = 0")

    if jenis == jenis_list[1]:
        nomor = 1
        st.write(f"### {nomor}")
        if step: st.write("Siapkan inputnya")
        st.latex(fr"   {hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Gunakan rumus diskriminan")
        st.latex(fr"D = {fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Sederhanakan")
        st.latex(fr"D = {fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}")
        nomor += 1
        st.write(f"### {nomor}")
        if step: st.write("Kurangkan")
        st.latex(fr"D = {fungsi(d)}")

    if jenis == jenis_list[2]:
        nomor = 1
        st.write(f"### {nomor}. Siapkan inputnya")
        st.latex(fr"{hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}. Gunakan rumus diskriminan")
        st.latex(fr"D = {fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}")
        nomor += 1
        st.write(f"### {nomor}. Sederhanakan")
        st.latex(fr"D = {fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}")
        nomor += 1
        st.write(f"### {nomor}. Kurangkan")
        st.latex(fr"D = {fungsi(d)}")
        # st.write("Jika D > 0: Jumlah ")
        nomor += 1
        st.write(f"### {nomor}")
        if fungsi(d) > 0:
            st.write("Karena diskriminan lebih dari 0, maka jumlah solusinya 2.")
            st.write("Jumlah solusi = 2")
        elif fungsi(d) == 0:
            st.write("Karena diskriminan sama dengan 0, maka jumlah solusinya 1 dan kembar.")
            st.write("Jumlah solusi = 1")
        else:
            st.write("Karena diskriminan kurang dari 0, maka tidak ada solusi.")
            st.write("Jumlah solusi = 0")

    if jenis == jenis_list[3]:
        nomor = 1
        st.write(f"### {nomor}. Siapkan inputnya")
        st.latex(fr"{hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}. Gunakan rumus untuk mencari titik puncak untuk x")
        st.latex(fr"x = \frac{{{fungsi(-b)}}}{{2 \times {fungsi(a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Sederhanakan")
        st.latex(fr"x = \frac{{{fungsi(-b)}}}{{2 \times {fungsi(a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Bagikan")
        st.latex(fr"x = {fungsi(f1)}")
        nomor += 1
        st.write(f"### {nomor}. Gunakan rumus untuk mencari titik puncak untuk y")
        st.latex(fr"y = -\frac{{{fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}}}{{4 \times {fungsi(a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Sederhanakan")
        st.latex(fr"y = -\frac{{{fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}}}{{{fungsi(4 * a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Bagikan")
        st.latex(fr"y = -\frac{{{fungsi(d)}}}{{{fungsi(4 * a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Bagikan")
        st.latex(fr"y = {fungsi(f2)}")
        nomor += 1
        st.write(f"### {nomor}. Titik puncak")
        st.latex(fr"({fungsi(f1)}, {fungsi(f2)})")

        # st.latex(r"""\[ \int\limits_0^1 x^2 + y^2 \ dx \]""")

if muncul_2:
    st.write('## Grafik')

    jarak = f1 - 5
    batas = f1 + 5
    ukuran = 0.01

    plt.style.use('seaborn-whitegrid')

    x = np.arange(jarak, batas + 1e-14, ukuran)
    plt.figure(figsize=(10,10))

    y1 = a*x**2 + b*x + c
    plt.plot(x,y1,color='blue',lw=5)

    y2 = 0*x + 0
    plt.plot(x,y2,color='green',lw=5)

    plt.xlabel("x", size=20,)
    plt.ylabel("y",)
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