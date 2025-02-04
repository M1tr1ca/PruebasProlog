import tkinter as tk
from tkinter import scrolledtext
from pyswip import Prolog

prolog = Prolog()
prolog.consult("Clasificacion.pl")

BG_COLOR = "#FFC0CB"
TEXT_COLOR = "#000000"
BOT_COLOR = "#FF69B4"
FONT = ("Arial", 12)

def mostrar_mensaje_inicial():
   mensaje_bienvenida = """❤️ Bot: ¡Hola! ¡Feliz San Valentín!
   
💌 Puedes preguntarme sobre el amor usando palabras como:
- "love/amor" (ej: "I love Adela")
- "happiness/felicidad" (ej: "Adela es mi felicidad")
- "heart/corazón" (ej: "Adela es mi corazón") 
- "message" para un mensaje aleatorio de amor

¿Qué quieres decirme sobre Adela? 💕\n"""
   chat.insert(tk.END, mensaje_bienvenida, "bot")

def procesar_input(event=None):  # Added event parameter
   mensaje_usuario = entrada_usuario.get().strip().lower()
   entrada_usuario.delete(0, tk.END)

   if not mensaje_usuario:
       return
   
   chat.insert(tk.END, f"\n🧑 Tú: {mensaje_usuario}\n", "user")
   
   if "hola"  in mensaje_usuario:
       chat.insert(tk.END, "❤️ Bot: ¡Hola! ¿Qué quieres decirme sobre Adela hoy? 💕\n", "bot")
       return

   consultas = {
       ("love", "quiero", "amo", "amor"): "i_love_you(adela, Message)",
       ("felicidad", "happiness"): "you_are_my_happiness(adela, Message)",
       ("todo", "everything","vida"): "you_are_my_everything(adela, Message)",
       ("corazón", "heart"): "you_are_my_heart(adela, Message)",
       ("reina", "queen"): "you_are_my_queen(adela, Message)",
       ("alma", "soul"): "you_are_my_soulmate(adela, Message)",
       ("mensaje", "message"): "love_message(Message)",
       ("valentine", "san valentin"): "valentine_message(Message)",
       ("gabacho", "francés"): "french_message(adela,Message)",

   }
   
   for palabras, consulta in consultas.items():
       if any(palabra in mensaje_usuario for palabra in palabras):
           try:
               result = list(prolog.query(consulta))
               if result:
                   mensaje = result[0]["Message"]
                   chat.insert(tk.END, f"❤️ Bot: {mensaje}\n", "bot")
                   return
           except Exception as e:
               chat.insert(tk.END, f"🤖 Bot: Error: {str(e)}\n", "bot")
               return
   
   chat.insert(tk.END, "💌 Bot: Prueba con palabras como 'love', 'heart', 'soul' o pide un 'message'\n", "bot")

root = tk.Tk()
root.title("💬 Chat Romántico con Adela 💖")
root.geometry("500x600")
root.configure(bg=BG_COLOR)

chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="white", fg=TEXT_COLOR, font=FONT)
chat.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat.tag_configure("user", foreground="#0000CD")
chat.tag_configure("bot", foreground=BOT_COLOR)

entrada_usuario = tk.Entry(root, font=FONT)
entrada_usuario.pack(pady=5, padx=10, fill=tk.X)
entrada_usuario.bind('<Return>', procesar_input)  # Bind Enter key to procesar_input

boton_enviar = tk.Button(root, text="Enviar", command=procesar_input, font=FONT, bg="#FF1493", fg="white")
boton_enviar.pack(pady=5)

mostrar_mensaje_inicial()
root.mainloop()