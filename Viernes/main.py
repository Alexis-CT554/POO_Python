from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("--------------Herencia Alumno--------------")
    al1 = Alumno("Jose", 19, "1219747878", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("-------------Herencia Profesor")
    profe1 = Profesor("Jesus", 30 + 16 , 363565, "Ingenieria en software")
    print(profe1)
    profe1.dormir()

    print("-------------Herencia ayudante profesor----------------")
    ayudante = AyudanteProfesor("Adrian", 20, "232323", "ICO", 23223, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")
    ayudante.carrera = "ICO2"
    print(ayudante)

main()