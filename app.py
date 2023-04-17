# Title

# List import
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import math
# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 15}

plt.rc('font', **font)


# Menjalankan program
# streamlit run 'Equation Solver 4 - 1.py'

# @import fonts/Roboto-Regular.ttf;

aaa = """
	<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}
	</style>
"""

streamlit_style = """
	<style>
	@import fonts;

	[class*="css"]  {
	font-family: 'FreeSans';
	}
	</style>
"""

def color(text, c):
    return f"<font color={c}>{text}</font>"

st.markdown(streamlit_style, unsafe_allow_html=True)
# st.write(f"The next word is {color('red','yellow')}", unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# Streamlit
# st.title('Equation Solver')
st.markdown("# <font color='#80ffb0'>Equation Solver</font>", unsafe_allow_html=True)
# st.write('#### **Made by Devan Daniel - Kelas 8 Betania**')
st.write('**Made by Devan Daniel - Kelas 9**')
st.write('')
stw(f"**{color('Equation Solver','#a0ff60')}** adalah bangun yang punya sisi, luas, dan volume. Ada banyak jenis geometri dan bisa melihat gambarnya.")
st.markdown('''
- Program ini dapat menyelesaikan persamaan **Linear**, **2 Variabel**, dan **Kuadrat**
- Program ini juga dapat menampilkan langkah penyelesaian dan grafik solusi dari soal
- Silahkan masukkan jenis persamaan dan variabelnya di menu bawah
- Agar bisa melihat informasi, klik tombol informasi program ini

Version: 1.3<br>
Last updated: ?????

<font size=4><b>Link:</b></font><br>
Link website saya:<br>
https://devandaniel9.github.io/index.html<br>
Link program geometri:<br>
https://devandaniel9-geometry-3.streamlit.app/
''', unsafe_allow_html=True)

# st.info('This is a purely informational message', )

# st.download

# import streamlit as st

st.write('')

# st.divider()

st.write('## **Pengaturan**')

with st.expander("Tampilkan"):
    st.write('### **Digit Precision**')
    digit = int(st.number_input("Digit (2-10)", value=3, min_value=2, max_value=10))

st.write('## **Persamaan**')
persamaan_list = ["Persamaan Linear", "Persamaan 2 Variabel", "Persamaan Kuadrat", "Persamaan Eksponensial", "Buat Soal Cerita", "Informasi"]
persamaan = st.selectbox("Pilih persamaan:", persamaan_list)

# Konversi float ke int, contoh: 3.0 menjadi 3, 3.2 menjadi 3.2
def fungsi(angka):
    a = round(angka, digit)
    if round(angka, digit) == round(angka, 0):
        angka = int(a)
    else:
        angka = a
   
    return angka

# Plus minus
def fungsi2(angka):
    if angka < 0:
        angka = f"- {-angka}"
    else:
        angka = f"+ {angka}"

    return angka

# Kurung
def fungsi3(angka):
    if angka < 0:
        angka = f"({angka})"

    return angka

# Angka 1 dengan variabel
def fungsi4(angka):
    if angka == "+ 1" or angka == 1:
        if angka == 1: angka = ""
        else: angka = "+ "
    elif angka == "- 1" or angka == -1:
        if angka == -1: angka = "-"
        else: angka = "- "

    return angka

# Plus minus 2
def fungsi5(angka):
    if angka < 0:
        angka = "-"
    else:
        angka = "+"

    return angka

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

# Pecahan
def reciprocal(a, b):
    # a/b
    gcd = math.gcd(a,b)
    a1 = a//gcd
    b1 = b//gcd
    # print(f"{a}/{b} = {a1}/{b1}")
    return a1, b1

def reciprocal2(a, b):
    return a//b, a%b, b

# reciprocal(12,18)

# st.time_input()
# st.map()
# st.camera_input("Take a picture")
# st.file_uploader("Choose a file")
# st.snow()

if persamaan == persamaan_list[0]:
    col = st.columns(2)
    with col[0]: open_image("Linear Equation.png")
    with col[1]: st.write('**Persamaan Linear** adalah persamaan dengan garis yang lurus dalam grafik. Rumusnya adalah ax+b=c.')
    st.write('Ada 3 variabel di persamaan linear, yaitu a, b, c. Variabel a disebut juga gradien, sedangkan b dan c adalah konstanta.')
    st.write('### **Rumus**')
    # st.latex(r"ax + b = c")
    st.latex(r"ax + b = c\text{, dengan } a \neq 0")
    # st.latex(r"a \neq 0")
    st.write('### **Masukkan angka**')
    col = st.columns(3)
    with col[0]: a = float(st.text_input("a (Default: 2)", value=2))
    with col[1]: b = float(st.text_input("b (Default: 1)", value=1))
    with col[2]: c = float(st.text_input("c (Default: 5)", value=5))

    st.write('## **Hasil Persamaan**')

    ruas_kiri = fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b))}"
    ruas_kanan = fungsi(c)

    hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

    st.latex(hasil_persamaan)

    st.write('## **Hasil Penyelesaian**')

    try:
        hasil = (c - b) / a
        rec1, rec2 = reciprocal(int(c-b),int(a))
        rec21, rec22, rec23 = reciprocal2(int(c-b),int(a))
        # print(rec2)
        if rec2 == 1:
            st.latex(f"x = {fungsi(hasil)}")
        else:
            if rec21 == 0:
                st.latex(fr"x = \frac{{{rec1}}}{{{rec2}}} \approx {fungsi(hasil)}")
            else:
                st.latex(fr"x = \frac{{{rec1}}}{{{rec2}}} = {rec21}\frac{{{rec22}}}{{{rec23}}} \approx {fungsi(hasil)}")

        muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
        muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
    except:
        st.write("Ada yang bermasalah pada input persamaan")
        if a == 0:
            st.write("Variabel a tidak sama dengan 0")

        muncul_1 = False
        muncul_2 = False

    if muncul_1:
        st.write('## **Langkah Penyelesaian**')

        nomor = 1
        st.write(f"### {nomor}. Siapkan inputnya")
        st.latex(fr"{hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}. Buatlah pengurangan ruas kiri dan kanan")
        st.latex(fr"{ruas_kiri} - {fungsi(b)} = {ruas_kanan} - {fungsi(b)}")
        nomor += 1
        st.write(f"### {nomor}. Kurangkan kedua ruas")
        st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b)}")
        if fungsi(a) != 1:
            nomor += 1
            st.write(f"### {nomor}. Buatlah pembagian ruas kiri dan kanan")
            st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}}x = \frac{{{fungsi(c - b)}}}{{{fungsi(a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan kedua ruas")
            st.latex(fr"x = {fungsi(hasil)}")

    if muncul_2:
        st.write('## **Grafik**')

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

if persamaan == persamaan_list[1]:
    col = st.columns(2)
    with col[0]: open_image("simultaneous-linear-equations.png")
    with col[1]: st.write('**Persamaan 2 Variabel** adalah persamaan kompleks yang terdiri dari 2 variabel dan 2 baris. Tujuannya untuk mencari solusi x dan y.')
    st.write('''Ada 6 variabel di persamaan 2 variabel, yaitu a, b, c, d, e, f.
        Variabel a dan d adalah gradien x, b dan e adalah gradien y, dan c dan f adalah konstanta.
        Barisan pertama terdiri dari variabel a, b, c; dan barisan kedua terdiri dari variabel d, e, f.
    ''')
    st.write('### **Rumus**')
    st.latex(r"ax + by = c\\dx + ey = f")

    # st.latex(r"a \neq 0, a \neq 0, a \neq 0, d \neq 0")
    st.write('### **Masukkan angka**')
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

    st.write('## **Hasil Persamaan**')

    ruas_kiri_1 = fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(b)))}y"
    ruas_kanan_1 = fungsi(c)
    ruas_kiri_2 = fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}y"
    ruas_kanan_2 = fungsi(f)
    persamaan_1 = fr"{ruas_kiri_1} = {ruas_kanan_1}"
    persamaan_2 = fr"{ruas_kiri_2} = {ruas_kanan_2}"
    persamaan = fr"{persamaan_1}\\{persamaan_2}"
    st.latex(persamaan)

    st.write('## **Hasil Penyelesaian**')

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
            st.write(f"Di Persamaan 1, kalikan kedua ruas dengan {fungsi(d)}")
            st.write(f"Di Persamaan 2, kalikan kedua ruas dengan {fungsi(a)}")
            st.latex(fr"{fungsi4(fungsi(d * a))}x {fungsi4(fungsi2(fungsi(d * b)))}y = {fungsi(d * c)}\\{fungsi4(fungsi(a * d))}x {fungsi4(fungsi2(fungsi(a * e)))}y = {fungsi(a * f)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write("Kurangkan persamaan atas dengan bawah")
            st.latex(fr"{fungsi4(fungsi(d * b))}y - {fungsi4(fungsi3(fungsi(a * e)))}y = {fungsi(d * c)} - {fungsi3(fungsi(a * f))}")
            st.latex(fr"{fungsi4(fungsi(d * b - a * e))}y = {fungsi(d * c - a * f)}")
            if fungsi(d * b - a * e) != 1:
                st.latex(fr"""\frac{{{fungsi(d * b - a * e)}}}{{{fungsi(d * b - a * e)}}} y = \frac{{{fungsi(d * c - a * f)}}}{{{fungsi(d * b - a * e)}}}""")
                st.latex(fr"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Subsitusikan y = {fungsi(hasil_y)} ke Persamaan 1")
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
            st.write(f"Subsitusikan y ke Persamaan 2")
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
            st.write(f"Subsitusikan x = {fungsi(hasil_x)} ke Persamaan 1")
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
            st.write(f"Ubah bentuk persamaan menjadi determinan")
            # st.latex(r"D = \begin{bmatrix}a & b\\c & d\end{bmatrix}")
            st.latex(fr"D = \begin{{bmatrix}}{fungsi(a)} & {fungsi(b)}\\{fungsi(d)} & {fungsi(e)}\end{{bmatrix}}")
            st.latex(fr"D_1 = \begin{{bmatrix}}{fungsi(c)} & {fungsi(b)}\\{fungsi(f)} & {fungsi(e)}\end{{bmatrix}}")
            st.latex(fr"D_2 = \begin{{bmatrix}}{fungsi(a)} & {fungsi(c)}\\{fungsi(d)} & {fungsi(f)}\end{{bmatrix}}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Gunakan rumus determinan")
            # st.latex(rf"D = ad - bc")
            st.latex(rf"D = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(d))}")
            st.latex(rf"D_1 = {fungsi3(fungsi(c))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(f))}")
            st.latex(rf"D_2 = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(f))} - {fungsi3(fungsi(c))} \times {fungsi3(fungsi(d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"D = {fungsi(a * e)} {fungsi2(fungsi(-b * d))}")
            st.latex(rf"D_1 = {fungsi(c * e)} {fungsi2(fungsi(-b * f))}")
            st.latex(rf"D_2 = {fungsi(a * f)} {fungsi2(fungsi(-c * d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"D = {fungsi(a*e-b*d)}")
            st.latex(rf"D_1 = {fungsi(c*e-b*f)}")
            st.latex(rf"D_2 = {fungsi(a*f-c*d)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Gunakan rumus persamaan dan determinan")
            st.latex(rf"x = \frac{{D_1}}{{D}} = \frac{{{fungsi(c*e-b*f)}}}{{{fungsi(a*e-b*d)}}}")
            st.latex(rf"y = \frac{{D_2}}{{D}} = \frac{{{fungsi(a*f-c*d)}}}{{{fungsi(a*e-b*d)}}}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Hitungkan")
            st.latex(rf"x = {fungsi(hasil_x)}")
            st.latex(rf"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"Penyelesaian x dan y")
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

if persamaan == persamaan_list[2]:
    col = st.columns(2)
    with col[0]: open_image("quadratic-formula.png")
    with col[1]: st.write('**Persamaan 2 Variabel** adalah persamaan kompleks yang terdiri dari 2 variabel dan 2 baris. Tujuannya untuk mencari solusi x dan y.')
    st.write('''Ada 6 variabel di persamaan 2 variabel, yaitu a, b, c, d, e, f.
        Variabel a dan d adalah gradien x, b dan e adalah gradien y, dan c dan f adalah konstanta.
        Barisan pertama terdiri dari variabel a, b, c; dan barisan kedua terdiri dari variabel d, e, f.
    ''')
    st.write('### **Rumus**')
    st.latex(r"ax^2 + bx + c = 0\text{, dengan } a \neq 0")
    # st.latex(r"a \neq 0")

    with st.expander("Tampilkan rumus lebih banyak"):
        st.write('### **Mencari Variabel x**')
        # g1 = fr"\sqrt{{{fungsi3(fungsi(b))}^2 - 4 \times {fungsi3(fungsi(a))} \times {fungsi3(fungsi(c))}}}"
        st.latex(r"x_{1,2} = \frac{-b\pm\sqrt{b^2-4ac}}{2a}")
        st.write('### **Diskriminan**')
        st.latex(r"D = b^2-4ac")
        st.write('### **Jumlah Solusi**')
        st.write('Jumlah solusi 2, jika D > 0')
        st.write('Jumlah solusi 1, jika D = 0')
        st.write('Jumlah solusi 0, jika D < 0')
        st.write('### **Titik Puncak**')
        st.latex(r"x = -\frac{b}{2a}")
        st.latex(r"y = -\frac{b^2-4ac}{4a}")
        # st.latex(fr"y = -\frac{{{fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}}}{{4 \times {fungsi(a)}}}")
    
    st.write('### **Masukkan angka**')
    col = st.columns(3)
    with col[0]: a = float(st.text_input("a (Default: 1)", value=1))
    with col[1]: b = float(st.text_input("b (Default: 3)", value=3))
    with col[2]: c = float(st.text_input("c (Default: 2)", value=2))

    st.write('## **Hasil Persamaan**')

    ruas_kiri = fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))}"
    ruas_kanan = "0"

    hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

    st.latex(hasil_persamaan)

    st.write('## **Hasil Penyelesaian**')

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

        '''rec1, rec2 = reciprocal(int(c-b),int(a))
        rec21, rec22, rec23 = reciprocal2(int(c-b),int(a))
        # print(rec2)
        if rec2 == 1:
            st.latex(f"x = {fungsi(hasil)}")
        else:
            if rec21 == 0:
                st.latex(fr"x = \frac{{{rec1}}}{{{rec2}}} \approx {fungsi(hasil)}")
            else:
                st.latex(fr"x = \frac{{{rec1}}}{{{rec2}}} = {rec21}\frac{{{rec22}}}{{{rec23}}} \approx {fungsi(hasil)}")'''
        
        # st.write(d)
        
        check_rec = int(d**0.5+1e-10) == fungsi(d**0.5)

        # st.write(check_rec)

        if check_rec:
            rec1, rec2 = reciprocal(int(-b+round(d**0.5,10)),int(2*a))
            rec21, rec22, rec23 = reciprocal2(int(-b+round(d**0.5,10)),int(2*a))

        st.write(check_rec)

        # Solusi
        if d < 0:
            st.write("x = Tidak ada")
        else:
            if fungsi(hasil_x1) == fungsi(hasil_x2):
                if check_rec:
                    st.latex(fr"x = {fungsi(hasil_x1)}")
                else:
                    st.latex(fr"x = {fungsi(hasil_x1)}")
            else:
                if check_rec:
                    if rec2 == 1:
                        st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                    else:
                        if rec21 == 0:
                            st.latex(fr"x_1 = \frac{{{rec1}}}{{{rec2}}} \approx {fungsi(hasil_x1)}")
                        else:
                            st.latex(fr"x_1 = \frac{{{rec1}}}{{{rec2}}} = {rec21}\frac{{{rec22}}}{{{rec23}}} \approx {fungsi(hasil)}")
                else:
                    st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                st.latex(fr"x_2 = {fungsi(hasil_x2)}")
        
        st.write(f"Diskriminan = {fungsi(d)}")
        st.write(f"Jumlah Solusi = {fungsi(e)}")
        st.write(f"Titik Puncak = ({fungsi(f1)}, {fungsi(f2)})")
        st.write("")

        muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)
        muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)
    except:
        st.write("Ada yang bermasalah pada input persamaan")

        muncul_1 = False
        muncul_2 = False

    if muncul_1:
        st.write('## **Langkah Penyelesaian**')

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
                st.write(f"Gunakan rumus persamaan kuadrat")
                st.latex(fr"x_1 = \frac{{-{fungsi3(fungsi(b))} + {g1}}}{{2 \times {fungsi3(fungsi(a))}}}")
                st.latex(fr"x_2 = \frac{{-{fungsi3(fungsi(b))} - {g1}}}{{2 \times {fungsi3(fungsi(a))}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"Hitungkan")
                st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {g2}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {g2}}}{{{fungsi(2 * a)}}}")
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"Hitungkan")
                st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {g3}}}{{{fungsi(2 * a)}}}")
                st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {g3}}}{{{fungsi(2 * a)}}}")
                if fungsi(d) >= 0:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hitung akar")
                    st.latex(fr"x_1 = \frac{{{fungsi(-b)} + {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    st.latex(fr"x_2 = \frac{{{fungsi(-b)} - {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hitungkan")
                    st.latex(fr"x_1 = \frac{{{fungsi(-b + d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    st.latex(fr"x_2 = \frac{{{fungsi(-b - d ** 0.5)}}}{{{fungsi(2 * a)}}}")
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hasil")
                    st.latex(fr"x_1 = {fungsi(hasil_x1)}")
                    st.latex(fr"x_2 = {fungsi(hasil_x2)}")
                    if fungsi(hasil_x1) == fungsi(hasil_x2):
                        nomor += 1
                        st.write(f"### {nomor}")
                        st.write(f"Hasil")
                        st.latex(fr"x = {fungsi(hasil_x1)}")
                else:
                    nomor += 1
                    st.write(f"### {nomor}")
                    st.write(f"Hasil")
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

                # st.latex(fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))} = 0")

        if jenis == jenis_list[1]:
            nomor = 1
            st.write(f"### {nomor}. Siapkan inputnya")
            st.latex(fr"   {hasil_persamaan}")
            nomor += 1
            st.write(f"### {nomor}. Gunakan rumus diskriminan")
            st.latex(fr"D = {fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"D = {fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}")
            nomor += 1
            st.write(f"### {nomor}. Kurangkan")
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
        st.write('## **Grafik**')

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

if persamaan == persamaan_list[3]:
    st.write('[Coming Soon]')

if persamaan == persamaan_list[4]:
    st.write('[Coming Soon]')

if persamaan == persamaan_list[5]:
    st.write('Di program ini')
    st.write('Sumber link')
    st.markdown('''
    <font size=4><b>Link:</b></font><br>
    Link yang mungkin kamu sukai:<br>
    1. https://byjus.com/global/<br>
    2. https://www.cuemath.com/worksheets/
    ''', unsafe_allow_html=True)
