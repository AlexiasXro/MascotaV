import random
from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        #validando rangos 
        self.hambre = 0
        self.felicidad = 0

        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_feliz = imagen.feliz
        self.imagen_disgustado = imagen.disgustado
        self.imagen_muerto = imagen.muerto

    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0

        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(self.nombre,"Esta lleno, ya no puede comer mas")
        
        else:
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(self.nombre, "ha sido alimentado 👌")


    def jugar(self):
        pass

    def estado_animo(self):
        pass

    def presentacion(self):  # opcional
        print(f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota!          ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}")

    def despedida(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Nos vemos! ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n"
        )


# Crear una instancia de MascotaVirtual

# Interactuar con la mascota virtual
# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉
interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"


print(interfaz_inicio)

nombre = input("Elige el nombre de tu mascota: ")
mascota = MascotaVirtual(nombre)
mascota.presentacion()

while True:
    print(interfaz_juego)
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        mascota.alimentar()
    elif opcion == 2:
        mascota.jugar()
    elif opcion == 3:
        mascota.estado_animo()
    elif opcion == 4:
        mascota.despedida()
        break

            