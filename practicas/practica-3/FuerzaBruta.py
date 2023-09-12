import os
"""
Instrucciones de ejecucion:

Simplemente en la terminal usar el comando
python3 FuerzaBruta.py

Nota: El archivo .lol debe de estar en la
misma carpeta

Nota2: Solo funciona para el cifrado cesar
"""

def derecha(num,i):
    """
    Metodo que realiza que recorre un numero
    a la derecha tantas veces como lo indique
    la clave.

    Usado para hacer cifrado cesar
    """
    return (num + i)%256

def izquierda(num,i):
    """
    Metodo que realiza que recorre un numero
    a la izquierda tantas veces como lo indique
    la clave.

    Usado para hacer cifrado cesar
    """
    if (num - i) < 0:
        return 256 + (num -i)
    else:
        return num -i



def crearArchivo(numero, bytes):
    """
    Metodo que crea los archivos prueba, con el numero en el nombre
    """
    try:
        f = open(os.path.join('intentos', "prueba"+str(numero)), "wb")
    except Exception as e:
        os.mkdir("intentos")
        f = open(os.path.join('intentos', "prueba"+str(numero)), "wb")
    f.write(bytes)
    f.close()

# Se leen los 3 archivos
hex1 = open('file1.lol', 'rb').read()
hex2 = open('file2.lol', 'rb').read()
hex3 = open('file3.lol', 'rb').read()

# Crea las 255 posibles rotaciones del cifrado cesar en una carpeta llamada inentos.
for i in range(255):
    aux = [izquierda(x,i) for x in hex2]
    aux2 = bytes(aux)
    crearArchivo(i, aux2)
