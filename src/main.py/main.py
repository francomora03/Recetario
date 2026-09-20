import csv


def cargar_recetas():
    with open("data/recetas.csv", "r", encoding="utf-8") as archivo:
        recetas = list(csv.DictReader(archivo))

    return recetas


def mostrar_recetas(recetas):
    print("\n=== CATÁLOGO DE RECETAS ===")

    for receta in recetas:
        print(
            f"{receta['id']} - {receta['nombre']} "
            f"({receta['tiempo_min']} min) - "
            f"Dificultad: {receta['dificultad']} - "
            f"Categoría: {receta['categoria']}"
        )


recetas = cargar_recetas()
mostrar_recetas(recetas)