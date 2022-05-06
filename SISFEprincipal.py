import sys
from SISFEfunciones import *

def main(): 
    validarArchivo() 
    driver = generarDriver()
    informacion = leerArchivos()
    loguearProfesional(driver)
    navegar(driver)
    totalApremios = calcularRepeticiones(informacion,driver)
    posicion = 0
    while (True):
        cargarDatosProfesional(informacion,driver)
        posicion = posicion + cargarDatosDemandados(informacion,driver,totalApremios,posicion)
        if (posicion>=totalApremios[2]):
            break
    input("Presione una tecla para salir del navegador automatizado")
if __name__ == "__main__":
    sys.exit(main())

