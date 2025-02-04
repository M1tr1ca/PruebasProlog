import tkinter as tk
from tkinter import scrolledtext
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

# Configuración de la interfaz gráfica
BG_COLOR = "#F0F0F0"  # Gris claro de fondo
TEXT_COLOR = "#333333"  # Gris oscuro para el texto
BOT_COLOR = "#4B4B4B"  # Gris oscuro para el texto del bot
FONT = ("Helvetica", 12)
ENTRY_BG = "#FFFFFF"  # Blanco para el fondo de la entrada
BUTTON_BG = "#4CAF50"  # Verde para el botón
HEADER_COLOR = "#00796B"  # Verde oscuro para el encabezado

def mostrar_mensaje_inicial():
    mensaje_bienvenida = """💬 Bot: ¡Hola! Soy el Bot de Clasificación de Animales 🦁

Puedes preguntarme cosas como:
- "El perro es un mamífero"
- "El águila es un ave"
- "El pez es un reptil"
- "¿Es el gato un mamífero?"

Solo dime algo sobre un animal y su tipo. 😊\n"""
    chat.insert(tk.END, mensaje_bienvenida, "bot")

def procesar_input(event=None):
    mensaje_usuario = entrada_usuario.get().strip().lower()
    entrada_usuario.delete(0, tk.END)

    if not mensaje_usuario:
        return

    chat.insert(tk.END, f"\n🧑 Tú: {mensaje_usuario}\n", "user")
    
    # Saludo personalizado
    if "hola" in mensaje_usuario:
        chat.insert(tk.END, "🤖 Bot: ¡Hola! ¿En qué puedo ayudarte hoy? 😊\n", "bot")
        return
    
    # Verificar si la frase contiene "no"
    negacion = "no" in mensaje_usuario
    
    # Extraer animal y tipo de la frase
    animal, tipo = extraer_animal_tipo(mensaje_usuario)
    
    if animal and tipo:
        resultado = verificar_afirmacion(animal, tipo, negacion)
        chat.insert(tk.END, f"🤖 Bot: {resultado}\n", "bot")
    else:
        chat.insert(tk.END, "💬 Bot: No pude entender la afirmación. Asegúrate de mencionar un animal y un tipo.\n", "bot")

# Configuración de la interfaz
root = tk.Tk()
root.title("💬 Clasificador de Animales 🦁")
root.geometry("500x600")
root.configure(bg=BG_COLOR)

# Encabezado
header_frame = tk.Frame(root, bg=HEADER_COLOR)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Clasificación de Animales", font=("Helvetica", 14, "bold"), fg="white", bg=HEADER_COLOR)
header_label.pack(pady=10)

# Ventana de chat
chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="white", fg=TEXT_COLOR, font=FONT, bd=2, relief="solid")
chat.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat.tag_configure("user", foreground="#1E90FF")  # Color para el texto del usuario
chat.tag_configure("bot", foreground=BOT_COLOR)  # Color para el texto del bot

# Entrada del usuario
entrada_usuario = tk.Entry(root, font=FONT, bg=ENTRY_BG, fg=TEXT_COLOR, bd=2, relief="solid")
entrada_usuario.pack(pady=5, padx=10, fill=tk.X)
entrada_usuario.bind('<Return>', procesar_input)

# Botón de enviar
boton_enviar = tk.Button(root, text="Enviar", command=procesar_input, font=FONT, bg=BUTTON_BG, fg="white", bd=2, relief="solid")
boton_enviar.pack(pady=5)

mostrar_mensaje_inicial()

root.mainloop()
