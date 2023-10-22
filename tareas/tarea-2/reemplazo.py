import re

'''
Nos ayuda a reemplazar los caracteres descifrados en el proceso
Los caracteres cifrados con mayusculas y los descrifrafos con minúsculas 
para distinguir mejor las palabras
'''

cifrado = 'GK NKNIMUK F LKHPFO UH AUKHQJ UH AUKHQJ MUK LUNIKPK OIVFCIZFO AJH CJP MUK HJP TFRIFH IGLUCPFNJ F KPF QFOKF UH AUKHQJ MUK TFRCFOF NK CJP GIPQKOIJPJP QKOOJOKP NK HUKPQOF HFQUOFCKZF Y NKPLKOQFPK GIKNJP KPQOKGKAKNJOKP MUK NKBFPK FC CKAQJO AJH QKGJO NK GIOFO TFAIF PU FCOKNKNJO MUK LFOFCIZFPK CF PFHSOK Y FAKCKOFOF CJP CFQINJP NKC AJOFZJH PI HJ PK AJHPKSUIF KPJP OKPUCQFNJP GI AUKHQJ NK EFHQFPGFP PKOIF IHNISHJ NK PU HJGROK PKHQIF CF VFAIF IHAFLFAINFN NK IHVKHAIJH CF GFYJO NKPSOFAIF MUK LUKNK FEKAQFO F UH CKAQJO AUFHNJ F PUP FHPIJPFP IHVJFAIJHKP OKPLJHNK PJCJ CF HFNF GFOY W PTKCCKY'

#aqui iremos poniendo los caracteres descifrados
dic = {
    'K':'e',
    'F':'a',
    'P':'s',
    'U':'u',
    'C':'l',
    'J':'o',
    'I':'i',
    'H':'n',
    'A':'c',
}

print("Cifrado:",cifrado)

texto = cifrado

#reeamplazmos los caracteres
for char in dic.keys():
    texto=re.sub(char, dic[char], texto)

print("Normal:",texto)
