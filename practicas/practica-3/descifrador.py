from textwrap import wrap

'''Lee el archivo en bytes y nos regresa la lista en numeros base 10'''
def leer_archivo(archivo):
    #archivo_lol = input("Dime le nombre del archivo: ")
    archivo_lol="archivos-cifrados/"+archivo
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
    #es el inverso de alfa = 91 y beta = 182
    des = bytes(list(map((lambda x:((x-182)*211)%256),lista)))
    return des


'''descrifrado base 64'''
def base_64(lista_cif):
    #obtenemos los numero binarios
    binarios = []
    for n in lista_cif:
        binarios.append(bin(n)[2:])
    #rellenamos con 0 a la izquierda para tener 6 bits
    binarios_p=[]
    for b in binarios:
        b = b.zfill(6)
        binarios_p.append(b)
    # lo transformamos a una cadenota
    ceros_unos = ''
    for b in binarios_p:
        ceros_unos+=str(b)
    #los agrupamos de 8 en 8
    ceros_unos_8=wrap(ceros_unos,8)
    #una vez agrupados los pasamos a su valor decimal
    hexa = []
    for n in ceros_unos_8:
        hexa.append(int(n,2))
    #quitamos el penultimo para que funciones
    hexa.pop(-2)
    g = bytes(list(hexa))
    return g

# leemos y desciframos el archivo 1 con cesar
lista_cif_cesar = leer_archivo('file1.lol')
lista_des_cesar = cesar(lista_cif_cesar)
escribir_archivo(lista_des_cesar, 'file1.mp4')


# leemos y desciframos el archivo 2 con base 64
lista_cif_base = leer_archivo('file2.lol')
lista_des_base = base_64(lista_cif_base)
escribir_archivo(lista_des_base, 'file2.jpg')

# leemos y desciframos el archivo 3 con afin
lista_cif_afin = leer_archivo('file3.lol')
lista_des_afin = afin(lista_cif_afin)
escribir_archivo(lista_des_afin, 'file3.mp3')