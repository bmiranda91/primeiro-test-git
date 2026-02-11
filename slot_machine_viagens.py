import tkinter as tk
import random
import time
import threading

# LISTA MASSIVA DE DESTINOS
destinos = [
    "Paris", "Roma", "Londres", "Nova Iorque", "Tóquio", "Barcelona", "Dubai", "Bangkok",
    "Rio de Janeiro", "Amesterdão", "Veneza", "Santorini", "Maldivas", "Costa Rica",
    "Islândia", "Sydney", "Melbourne", "Atenas", "Berlim", "Praga", "Viena", "Budapeste",
    "Varsóvia", "Cracóvia", "Copenhaga", "Estocolmo", "Oslo", "Helsínquia", "Zurique",
    "Genebra", "Nice", "Marselha", "Porto", "Lisboa", "Madeira", "Açores", "Sevilha",
    "Madrid", "Valência", "Marrakech", "Casablanca", "Cidade do Cabo", "Joanesburgo",
    "Nairobi", "Zanzibar", "Ilhas Maurícias", "Seychelles", "Bali", "Phuket", "Hanoi",
    "Ho Chi Minh", "Seul", "Hong Kong", "Taipei", "Singapura", "Kuala Lumpur",
    "Doha", "Abu Dhabi", "Istambul", "Cairo", "Petra", "Jerusalém", "Toronto",
    "Vancouver", "Montreal", "Los Angeles", "São Francisco", "Las Vegas", "Miami",
    "Cancún", "Cidade do México", "Buenos Aires", "Santiago do Chile", "Lima",
    "Bogotá", "Quito", "Panamá", "San José", "Auckland", "Fiji", "Taiti", "Havai"
]

# DESAFIOS DIVERTIDOS
desafios = [
    "Tira uma selfie com a polícia local e identifica a Partimos Amanhã Viagens!",
    "Experimenta o prato mais estranho que encontrares e publica nas redes!",
    "Faz uma dança típica local em público e grava um vídeo!",
    "Pede a um desconhecido para tirar uma foto tua com a pose mais ridícula possível!",
    "Compra algo num mercado local gastando menos de 2€ e mostra o resultado!",
    "Encontra um animal local e tira uma selfie com ele!",
    "Faz um vídeo a tentar falar 3 frases na língua local!",
    "Encontra o melhor miradouro e tira uma foto a saltar!",
    "Pede a alguém para te recomendar um lugar secreto e vai lá!",
    "Faz um TikTok no destino e identifica a Partimos Amanhã!",
    "Encontra um monumento famoso e recria uma pose histórica!",
    "Compra um íman feio de propósito e mostra ao mundo!",
    "Faz uma foto criativa com um polícia, bombeiro ou guia turístico!",
    "Encontra um artista de rua e tira uma foto com ele!",
    "Faz um vídeo a elogiar o destino com sotaque local!"
]

# ANIMAÇÃO DO SLOT
def animar_slot(callback):
    velocidades = [0.02, 0.03, 0.04, 0.05, 0.07, 0.1, 0.13, 0.16]
    for v in velocidades:
        for _ in range(8):
            resultado_label.config(
                text=random.choice(destinos),
                fg="#ffffff"
            )
            janela.update()
            time.sleep(v)
    callback()

# EFEITO FADE-IN
def fade_in(texto):
    for i in range(0, 11):
        cor = f"#{i*15:02x}{i*15:02x}{i*15:02x}"
        resultado_label.config(text=texto, fg=cor)
        janela.update()
        time.sleep(0.03)

# FUNÇÃO PRINCIPAL
def jogar(numero):
    def revelar():
        destino = random.choice(destinos)
        desafio = random.choice(desafios)

        texto = f"🌍 PRÓXIMO DESTINO:\n\n⭐ {destino.upper()} ⭐\n\n🔥 DESAFIO:\n{desafio}"

        fade_in(texto)

    threading.Thread(target=lambda: animar_slot(revelar)).start()

# INTERFACE
janela = tk.Tk()
janela.title("Slot Machine de Viagens – Partimos Amanhã")
janela.geometry("650x550")
janela.configure(bg="#1e1e2f")  # fundo escuro moderno

titulo = tk.Label(
    janela,
    text="Escolhe um número de 1 a 6 e tenta a sorte!",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#ffdd57"
)
titulo.pack(pady=20)

frame_botoes = tk.Frame(janela, bg="#1e1e2f")
frame_botoes.pack(pady=10)

cores = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93", "#ff924c"]

for i in range(1, 7):
    tk.Button(
        frame_botoes,
        text=str(i),
        width=5,
        height=2,
        font=("Arial", 16, "bold"),
        bg=cores[i-1],
        fg="white",
        activebackground="#ffffff",
        activeforeground="#000000",
        command=lambda n=i: jogar(n)
    ).grid(row=0, column=i-1, padx=10)

resultado_label = tk.Label(
    janela,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white",
    justify="center",
    wraplength=500
)
resultado_label.pack(pady=40)

janela.mainloop()