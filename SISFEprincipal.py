import sys
from SISFEfunciones import *
from easygui import *

def main(): 
    cantidadApremios = validarArchivo() 
    driver = generarDriver()
    informacion = leerArchivos()
    loguearProfesional(driver)
    navegar(driver)
    totalApremios = calcularRepeticiones(informacion,driver)
    posicion = 0
    while (True):
        # cargarDatosProfesional(informacion,driver)
        posicion = posicion + cargarDatosDemandados(informacion,driver,totalApremios,posicion)
        print("La posición es: ", posicion)
        print("La cantidad de apremios es", cantidadApremios) 
        if (posicion>cantidadApremios):
            msgbox("CREE EL LOTE Y PRESIONE ACEPTAR PARA TERMINAR.")
            break

if __name__ == "__main__":
    sys.exit(main())

