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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

st.markdown("# <font color='#80ffb0'>Informasi</font>", unsafe_allow_html=True)
st.write('')

st.write('Di program ini')
st.write('Sumber link')
st.markdown('''
<font size=4><b>Link:</b></font><br>
Link yang mungkin kamu sukai:<br>
1. https://byjus.com/global/<br>
2. https://www.cuemath.com/worksheets/
''', unsafe_allow_html=True)