from RotorClass import Rotor
from RotorClass import Reflector

Rotors = {}

names = ["I   ", "II   ", "III  ", "IV   ", "V    ", "VI   ", "VII  ", "VIII "]
notches = [
    ["Royal"[0]], ["Flags"[0]], ["Wave"[0]], ["Kings"[0]], ["Above"[0]], ["A", "N"], ["A", "N"], ["A", "N"]
]

cipher_grid = """
INPUT      	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Rotor I    	E	K	M	F	L	G	D	Q	V	Z	N	T	O	W	Y	H	X	U	S	P	A	I	B	R	C	J
Rotor II   	A	J	D	K	S	I	R	U	X	B	L	H	W	T	M	C	Q	G	Z	N	P	Y	F	V	O	E
Rotor III  	B	D	F	H	J	L	C	P	R	T	X	V	Z	N	Y	E	I	W	G	A	K	M	U	S	Q	O
Rotor IV   	E	S	O	V	P	Z	J	A	Y	Q	U	I	R	H	X	L	N	F	T	G	K	D	C	M	W	B
Rotor V    	V	Z	B	R	G	I	T	Y	U	P	S	D	N	H	L	X	A	W	M	J	Q	O	F	E	C	K
Rotor VI   	J	P	G	V	O	U	M	F	Y	Q	B	E	N	H	Z	R	D	K	A	S	X	L	I	C	T	W
Rotor VII  	N	Z	J	H	G	R	C	X	M	Y	S	W	B	O	U	F	A	I	V	L	P	E	K	Q	D	T
Rotor VIII 	F	K	Q	H	T	L	X	O	C	B	J	S	P	D	Z	R	A	M	E	W	N	I	U	Y	G	V
"""
# The following rotors were not available for 3-slot-machines.
# Beta rotor 	L	E	Y	J	V	C	N	I	X	W	P	B	Q	M	D	R	T	A	K	Z	G	F	U	H	O	S
# Gamma rotor	F	S	O	K	A	N	U	E	R	H	M	B	T	I	Y	C	W	L	Q	P	Z	X	V	G	J	D


for i in range(len(names)):
    buffer = 13 + ((i + 1) * 64)
    cipher = []
    for j in range(26):
        letter = cipher_grid[buffer + j*2]
        num = ord(letter) - 65
        cipher.append(num)
    # The cipher for Rotor I is:
    # [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    Rotors[names[i].replace(" ", "")] = Rotor(cipher, notches[i], names[i])


Reflectors = {}
names = ["B", "C", "B DUNN", "C DUNN"]
reflector_grid = """
reflector B     	(AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO) (TZ) (VW)
reflector C     	(AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW) (TQ) (SU)
reflector B Dünn	(AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP) (RX) (SZ) (TV)
reflector C Dünn	(AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW) (QZ) (SX) (UY)
"""
for i in range(len(names)):
    buffer = 19 + (i * 82)
    cipher = []
    for j in range(13):
        letter = reflector_grid[buffer + j*5]
        num = ord(letter) - 65
        cipher.append(num)
        letter = reflector_grid[buffer + j*5 + 1]
        num = ord(letter) - 65
        cipher.append(num)
    # The cipher for reflector B is:
    # [0, 24, 1, 17, 2, 20, 3, 7, 4, 16, 5, 18, 6, 11, 8, 15, 9, 23, 10, 13, 12, 14, 19, 25, 21, 22]
    Reflectors[names[i]] = Reflector(cipher, names[i])
