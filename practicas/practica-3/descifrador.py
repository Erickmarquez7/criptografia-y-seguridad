'''Lee el archivo en bytes y nos regresa la lista en numeros base 10'''
def leer_archivo():
    archivo_lol = input("Dime le nombre del archivo: ")
    archivo_lol="archivos-cifrados/"+archivo_lol
    #pasamos el archivo en modo lectura por byte
    archivo = open(archivo_lol, 'rb').read()
    #lo pasamos a lista de numeros para que sea mas facil maniuplar
    #si, con i xd para que no lo tome como palabra reservada
    bites = []
    for b in archivo:
        bites.append(b)
    #ya lo pasa de manera automatica a base 10        
    return bites


'''Escribe el archivo, recibe una lista de numero en base 10 
y lo transforma a base 16 para poder escribir los bytes'''
#def escribir_archivo(lista):

    

'''descifrado cesar, reciba la lista de numeros en base 10
y los descrifa en esa misma base'''
def cesar(lista):
    #no c si la llave sea 63 xd solo lo supuse xd
    des = list(map((lambda x:(x+63)%256),lista))
    return des

    
'''descifrado afin'''    
#def afin()
    
'''descrifrado base 64'''
#def base_64()


lista_cif = leer_archivo()
lista_des = cesar(lista_cif)
hexa = bytes(lista_des)
print(hexa)
