def pedir_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            calificaciones = list(map(float, input(f"Ingrese calificaciones separadas por coma para {nombre}: ").split(',')))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(cals)/len(cals) for nombre, cals in estudiantes.items()}
    return promedios

def encontrar_mejor(promedios):
    return max(promedios, key=promedios.get)

def guardar_resultados(estudiantes, promedios, mejor):
    with open("resultados.txt", "w") as f:
        for nombre, cals in estudiantes.items():
            f.write(f"{nombre}: {cals}, Promedio: {promedios[nombre]:.2f}\n")
        f.write(f"\nEstudiante con el mejor promedio: {mejor} ({promedios[mejor]:.2f})\n")

def main():
    estudiantes = pedir_datos()
    promedios = calcular_promedios(estudiantes)
    mejor = encontrar_mejor(promedios)
    guardar_resultados(estudiantes, promedios, mejor)
    print("¡Datos guardados en resultados.txt!")

if __name__ == "__main__":
    main()
