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
            print(self.nombre, "ha sido alimentado 🍗😋")

    def jugar(self):
        if self.hambre > 70:
            print(self.imagen_triste)
            print(f"{self.nombre} tiene mucha hambre y no puede jugar")
            return
        
        # Aumentar felicidad
        self.felicidad += random.randint(10, 25)
        if self.felicidad > 100:
            self.felicidad = 100
        
        # Aumentar hambre
        self.hambre += random.randint(10, 15)
        if self.hambre > 100:
            self.hambre = 100
        
        print(self.imagen_feliz)
        print(f"{self.nombre} se divierte jugando contigo! ⚽😄")

    def estado_animo(self):
    # Función para crear barras visuales
        def crear_barra(valor, maximo=100, ancho=20):
            porcentaje = valor / maximo
            barra_llena = '█' * int(porcentaje * ancho)
            barra_vacia = '░' * (ancho - len(barra_llena))
            return f"{barra_llena}{barra_vacia} {valor}%"
        
        print("\n═"*30 + " ESTADO " + "═"*30)
        print(f"\n🐾 {self.nombre}")
        print(f"\n🍗 Hambre:    {crear_barra(self.hambre)}")
        print(f"😊 Felicidad: {crear_barra(self.felicidad)}")
        
        # Determinar estado de ánimo con emojis
        if self.hambre >= 70 and self.felicidad <= 50:
            estado = "😭 MUY HAMBRIENTA Y TRISTE"
            print(self.imagen_triste)
        elif self.hambre >= 70:
            estado = "😫 MUY HAMBRIENTA"
            print(self.imagen_disgustado)
        elif self.felicidad <= 50:
            estado = "😔 TRISTE"
            print(self.imagen_triste)
        else:
            estado = "😊 CONTENTA Y SATISFECHA"
            print(self.imagen_feliz)
        
        print(f"\nESTADO DE ÁNIMO: {estado}")
        print("═"*70 + "\n")

    def presentacion(self):  # opcional
        print(f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota!          ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}")

    def despedida(self):  # opcional
        print(
            f"\n╔════════════════════════════════════╗\n║ Nos vemos! juguemos otro dia :)║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n"
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

            