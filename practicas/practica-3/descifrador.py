import re
from textwrap import wrap

'''Lee el archivo en bytes y nos regresa la lista en numeros base 10'''
def leer_archivo():
    archivo_lol = input("Dime le nombre del archivo: ")
    archivo_lol="archivos-cifrados/"+archivo_lol
    #pasamos el archivo en modo lectura por byte
    archivo = open(archivo_lol, 'rb').read()
    #lo pasamos a lista de numeros para que sea mas facil manipular
    #si, con i xd para que no lo tome como palabra reservada
    bites = []
    for b in archivo:
        bites.append(b)
    #ya lo pasa de manera automatica a base 10
    return bites


'''Escribe el archivo, recibe una lista de numero en base 10 
y lo transforma a base 16 para poder escribir los bytes'''
def escribir_archivo(des, nombre):
    #bts es de bytes, no del grupo de k-pop xd
    bts = []
    for b in des:
        bts.append(hex(b))
        #print(hex(b))
    file = open('archivos-descifrados/'+nombre, 'wb')
    file.write(des)
    file.close()


'''descifrado cesar, reciba la lista de numeros en base 10
y los descrifa en esa misma base'''
def cesar(lista):
    des = bytes(list(map((lambda x:(x+187)%256),lista)))
    return des


'''descifrado afin'''    
def afin(lista):
    des = bytes(list(map((lambda x:((x-182)*211)%256),lista)))
    return des


'''descrifrado base 64'''
def base_64(lista_cif):
    binarios = []
    #lista_cif = lista_cif[:-1]
    for n in lista_cif:
        binarios.append(bin(n)[2:])
        
    ceros_unos = ''
    for b in binarios:
        ceros_unos+=str(b)

    ceros_unos_8=wrap(ceros_unos,8)

    hexa = []
    for n in ceros_unos_8:
        hexa.append(int(n,2))
    
    g = bytes(list(hexa))
    #print(g)

    return g
    #file = open('archivos-descifrados/file2', 'wb')
    #file.write(g)
    #file.close()


# leemos y desciframos el archivo 1 con cesar
#lista_cif_cesar = leer_archivo()
#lista_des_cesar = cesar(lista_cif_cesar)
#escribir_archivo(lista_des_cesar, 'file1.mp4')


# leemos y desciframos el archivo 2 con base 64
#lista_cif_base = leer_archivo()
#lista_des_base = base_64(lista_cif_base)
#escribir_archivo(lista_des_base, 'file2.jpg')

lista_cif_afin = leer_archivo()
lista_des_afin = afin(lista_cif_afin)
escribir_archivo(lista_des_afin, 'file3.mp3')

#lista_cif_base = leer_archivo()
#lista_des_base = base_64(lista_cif_base)
#print(lista_des_base)


#lista_cif=lista_cif[:-1]
#binarios = []
#for n in lista_cif:
#    binarios.append(bin(n))
#print(binarios)

#ceros_unos = ''
#for b in binarios:
#    ceros_unos+=str(b)
#print(ceros_unos)

#ceros_unos_8=re.finditer('.{1,2,3,4,5,6,7,8}',ceros_unos)
#ceros_unos_8=wrap(ceros_unos,8)
#print(ceros_unos_8)

##hexa = []
#for n in ceros_unos_8:
#    hexa.append(hex(int(n,2)))

#print(hexa)
#print(lista_cif[:-1])

#print(lista_cif)
#lista_des = cesar(lista_cif)
#hexa = bytes(lista_des)
#print(lista_cif)


#f = open('test.xd', 'wb')
#f.write(hexa)
