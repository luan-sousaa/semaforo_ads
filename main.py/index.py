import tkinter as tk
import time
import threading

# Função para coordenar a mudança de cor de todos os semáforos
def coordenar_semaforos(canvas, semaforos):
    while True:
        # Fase 1: 1a e 3 vermelhos, 1a e 4 verdes
        canvas.itemconfig(semaforos[0]['verde'], fill="black")
        canvas.itemconfig(semaforos[0]['vermelha'], fill="red")

        canvas.itemconfig(semaforos[1]['verde'], fill="green")

        canvas.itemconfig(semaforos[2]['verde'], fill="black")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="red")

        canvas.itemconfig(semaforos[3]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[3]['verde'], fill="green")
        canvas.update()
        time.sleep(15)  

        # Fase 2: 1a e 4 vermelhos, 1a e 3 verdes
        canvas.itemconfig(semaforos[0]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[0]['verde'], fill="green")

        canvas.itemconfig(semaforos[1]['verde'], fill="green")

        canvas.itemconfig(semaforos[2]['vermelha'], fill="red")
        canvas.itemconfig(semaforos[2]['verde'], fill="black")

        canvas.itemconfig(semaforos[3]['verde'], fill="black")
        canvas.itemconfig(semaforos[3]['vermelha'], fill="red")
        canvas.update()
        time.sleep(15) 

        #fase 3: 3 , 4 vermelho e principal do meio verde
        canvas.itemconfig(semaforos[1]['verde'], fill="green")
        canvas.itemconfig(semaforos[1]['verde'], fill="green")

        canvas.itemconfig(semaforos[2]['vermelha'], fill="red")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="red")


        canvas.itemconfig(semaforos[3]['vermelha'], fill="red")
        canvas.update()
        time.sleep(30)
        #fase 4: 
        canvas.itemconfig(semaforos[0]['verde'], fill="black")
        canvas.itemconfig(semaforos[0]['vermelha'], fill="red")

        canvas.itemconfig(semaforos[2]['verde'], fill="green")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="black")

        canvas.itemconfig(semaforos[3]['vermelha'], fill="red")
        canvas.update()
        time.sleep(45)

        

# Função para criar um semáforo
def criar_semaforo(canvas, x, y):
    canvas.create_rectangle(x - 20, y - 60, x + 20, y + 180, fill="black")
    luz_verde = canvas.create_oval(x - 20, y + 120, x + 20, y + 160, fill="black")
    luz_amarela = canvas.create_oval(x - 20, y + 60, x + 20, y + 100, fill="black")
    luz_vermelha = canvas.create_oval(x - 20, y, x + 20, y + 40, fill="black")
    return {'verde': luz_verde, 'amarela': luz_amarela, 'vermelha': luz_vermelha}

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação de Semáforos")

# Criando um canvas para desenhar os semáforos
canvas = tk.Canvas(janela, width=1000, height=800, bg="white")
canvas.pack()

# Criando múltiplos semáforos em posições diferentes
semaforos = []
posicoes = [(500, 50), (500, 550), (250, 300), (750, 300)]  # Posições dos semáforos
for pos in posicoes:
    luzes = criar_semaforo(canvas, pos[0], pos[1])
    semaforos.append(luzes)

# Iniciando uma thread para coordenar os semáforos
threading.Thread(target=coordenar_semaforos, args=(canvas, semaforos)).start()

# Iniciando o loop da interface gráfica
janela.mainloop()
