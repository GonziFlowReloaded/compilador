import os
import subprocess

# Nombre del archivo a compilar


# Comando para compilar el archivo utilizando PyInstaller


def generate_exe(python_code):
    archivo_a_compilar = 'archivo_a_compilar.py'
    comando = f'pyinstaller --onefile {archivo_a_compilar}'
    # Agregar este comando a python_code input("Presiona cualquier tecla para cerrar...")

    python_code += f'\ninput("Presiona cualquier tecla para cerrar...")'


    # Guardar el código fuente en un archivo
    with open(archivo_a_compilar, 'w') as file:
        file.write(python_code)

    
    # Compilar el archivo a un ejecutable .exe
    subprocess.run(comando, shell=True)
    
    # Eliminar el archivo de código fuente
    os.remove(archivo_a_compilar)
    
    # Eliminar la carpeta /build
    os.system('rmdir /s /q build')



    print(f'El código ha sido compilado a un archivo ejecutable {archivo_a_compilar[:-3]}.exe con éxito.')