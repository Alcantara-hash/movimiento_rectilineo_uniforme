def calcular_velocidad_promedio():
    delta_x = float(input("Ingrese el cambio en la posición (Δx): "))
    delta_t = float(input("Ingrese el cambio en el tiempo (Δt): "))
    velocidad_promedio = delta_x / delta_t
    print("La velocidad promedio es:", velocidad_promedio)

def calcular_desplazamiento():
    velocidad = float(input("Ingrese la velocidad constante (v): "))
    tiempo = float(input("Ingrese el tiempo transcurrido (t): "))
    desplazamiento = velocidad * tiempo
    print("El desplazamiento es:", desplazamiento)

def calcular_tiempo():
    desplazamiento = float(input("Ingrese el desplazamiento (x): "))
    velocidad = float(input("Ingrese la velocidad constante (v): "))
    tiempo = desplazamiento / velocidad
    print("El tiempo transcurrido es:", tiempo)

def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Calcular velocidad promedio")
    print("2. Calcular desplazamiento")
    print("3. Calcular tiempo")
    print("4. Conversión de unidades")
    print("5. Salir")

def realizar_conversion():
    opcion_conversion = int(input("Seleccione una opción de conversión: \n"
                                 "1. Metros a kilómetros\n"
                                 "2. Kilómetros a metros\n"
                                 "3. Segundos a horas\n"
                                 "4. Horas a segundos\n"
                                 "Ingrese el número de opción: "))

    if opcion_conversion == 1:
        metros = float(input("Ingrese la cantidad en metros: "))
        kilometros = metros / 1000
        print("El equivalente en kilómetros es:", kilometros)
    elif opcion_conversion == 2:
        kilometros = float(input("Ingrese la cantidad en kilómetros: "))
        metros = kilometros * 1000
        print("El equivalente en metros es:", metros)
    elif opcion_conversion == 3:
        segundos = float(input("Ingrese la cantidad en segundos: "))
        horas = segundos / 3600
        print("El equivalente en horas es:", horas)
    elif opcion_conversion == 4:
        horas = float(input("Ingrese la cantidad en horas: "))
        segundos = horas * 3600
        print("El equivalente en segundos es:", segundos)
    else:
        print("Opción no válida.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de opción deseada: "))

        if opcion == 1:
            calcular_velocidad_promedio()
        elif opcion == 2:
            calcular_desplazamiento()
        elif opcion == 3:
            calcular_tiempo()
        elif opcion == 4:
            realizar_conversion()
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
main()
