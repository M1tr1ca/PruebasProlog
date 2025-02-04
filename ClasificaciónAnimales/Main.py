from pyswip import Prolog
import re

# Inicializar Prolog
prolog = Prolog()
prolog.consult("Clasificacion.pl")  # Asegúrate de que el archivo .pl esté en el mismo directorio

# Lista de animales disponibles y sus categorías definidas en Prolog
animales_disponibles = {sol["X"] for sol in prolog.query("mamifero(X); ave(X); reptil(X); pez(X)")}

categorias = {
    "mamífero": "es_mamifero",
    "ave": "es_ave",
    "reptil": "es_reptil",
    "pez": "es_pez",
}

def clasificar_animal(animal):
    """Consulta a Prolog para clasificar un animal."""
    for categoria, consulta in categorias.items():
        if list(prolog.query(f"{consulta}({animal})")):
            return categoria
    return None  # Si no se encuentra ninguna categoría

def extraer_animal_tipo(frase):
    """Extrae el animal y su tipo de la frase."""
    # Convierte la frase a minúsculas y busca un animal
    frase = frase.lower()
    
    animal = None
    tipo = None
    
    # Buscar el animal en la frase
    for palabra in frase.split():
        if palabra in animales_disponibles:
            animal = palabra
    
    # Buscar el tipo en la frase
    for categoria in categorias.keys():
        if categoria in frase:
            tipo = categoria
    
    return animal, tipo

def verificar_afirmacion(animal, tipo, negacion):
    """Verifica si la afirmación es correcta o falsa, considerando la negación."""
    categoria_real = clasificar_animal(animal)
    
    # Si hay negación, invertimos el resultado
    if negacion:
        if categoria_real != tipo:
            articulo = "El" if animal[-1] != 'a' else "La"
            return f"¡Correcto! {articulo} {animal.capitalize()} no es un {tipo}, como dijiste."
        else:
            articulo = "El" if animal[-1] != 'a' else "La"
            return f"Lo siento, eso no es correcto. {articulo} {animal.capitalize()} efectivamente es un {tipo}."
    else:
        if categoria_real == tipo:
            articulo = "El" if animal[-1] != 'a' else "La"
            return f"¡Correcto! {articulo} {animal.capitalize()} efectivamente es un {tipo}"
        else:
            articulo = "El" if animal[-1] != 'a' else "La"
            return f"Lo siento, eso no es correcto. {articulo} {animal.capitalize()} no es un {tipo}, es un {categoria_real}."

# Interfaz interactiva
while True:
    entrada = input("\nHazme una pregunta sobre clasificar animales: ").strip().lower()
    
    if entrada == "salir":
        print("Hasta luego, besitos :)")
        break

    # Verificar si la frase contiene "no"
    negacion = "no" in entrada
    
    # Extraer animal y tipo de la frase
    animal, tipo = extraer_animal_tipo(entrada)
    
    if animal and tipo:
        print(verificar_afirmacion(animal, tipo, negacion))
    else:
        print("No pude entender la afirmación. Asegúrate de mencionar un animal y un tipo.")
