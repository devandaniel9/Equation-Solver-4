# All functions

import numpy as np
import math
from PIL import Image, ImageDraw, ImageFont

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

# Pecahan
def reciprocal(a, b):
    # a/b
    gcd = math.gcd(abs(a),abs(b))
    a1 = a//gcd
    b1 = b//gcd
    if a/b > 0:
        return a1, b1
        # print(f"{a}/{b} = {a1}/{b1}")
    else:
        return a1, b1

def reciprocal2(a, b):
    # a/b
    gcd = math.gcd(abs(a),abs(b))
    a1 = abs(a)//gcd
    b1 = abs(b)//gcd
    if a/b > 0:
        return '', a1, b1
        # print(f"{a}/{b} = {a1}/{b1}")
    else:
        return '-', a1, b1

def reciprocal3(a, b):
    gcd = math.gcd(abs(a),abs(b))
    a1 = abs(a)//gcd
    b1 = abs(b)//gcd
    if a/b > 0:
        a2 = a1//b1
    else:
        if a//b == 0:
            a2 = '-'
        else:
            a2 = -(abs(a)//abs(b))
    return a2, abs(a1)%abs(b1), abs(b1)

# reciprocal2(12,18)