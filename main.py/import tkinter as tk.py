import tkinter as tk
import time
import threading

# Função para coordenar a mudança de cor de todos os semáforos
def coordenar_semaforos(canvas, semaforos):
    while True:
        # Fase 1: 1a e 3 vermelhos, 1a e 4 verdes
        canvas.itemconfig(semaforos[0]['verde'], fill="black")
        canvas.itemconfig(semaforos[0]['amarela'], fill="black")
        canvas.itemconfig(semaforos[0]['vermelha'], fill="red")
        canvas.itemconfig(semaforos[2]['verde'], fill="black")
        canvas.itemconfig(semaforos[2]['amarela'], fill="black")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="red")
        canvas.itemconfig(semaforos[3]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[3]['amarela'], fill="black")
        canvas.itemconfig(semaforos[3]['verde'], fill="green")
        canvas.update()
        time.sleep(12)  # Tempo da fase 1 (verde)

        # Fase 2: Amarelo nos semáforos 1a e 4
        canvas.itemconfig(semaforos[0]['verde'], fill="black")
        canvas.itemconfig(semaforos[0]['amarela'], fill="yellow")
        canvas.itemconfig(semaforos[0]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[3]['verde'], fill="black")
        canvas.itemconfig(semaforos[3]['amarela'], fill="yellow")
        canvas.itemconfig(semaforos[3]['vermelha'], fill="black")
        canvas.update()
        time.sleep(3)  # Tempo da fase 2 (amarelo antes do vermelho)

        # Fase 3: 1a e 4 vermelhos, 1a e 3 verdes
        canvas.itemconfig(semaforos[0]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[0]['amarela'], fill="black")
        canvas.itemconfig(semaforos[0]['verde'], fill="green")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[2]['amarela'], fill="black")
        canvas.itemconfig(semaforos[2]['verde'], fill="green")
        canvas.itemconfig(semaforos[3]['verde'], fill="black")
        canvas.itemconfig(semaforos[3]['amarela'], fill="black")
        canvas.itemconfig(semaforos[3]['vermelha'], fill="red")
        canvas.update()
        time.sleep(12)  # Tempo da fase 3 (verde)

        # Fase 4: Amarelo nos semáforos 1a e 3
        canvas.itemconfig(semaforos[0]['verde'], fill="black")
        canvas.itemconfig(semaforos[0]['amarela'], fill="yellow")
        canvas.itemconfig(semaforos[0]['vermelha'], fill="black")
        canvas.itemconfig(semaforos[2]['verde'], fill="black")
        canvas.itemconfig(semaforos[2]['amarela'], fill="yellow")
        canvas.itemconfig(semaforos[2]['vermelha'], fill="black")
        canvas.update()
        time.sleep(3)  # Tempo da fase 4 (amarelo antes do vermelho)

# Função para criar um semáforo deitado
def criar_semaforo_deitado(canvas, x, y):
    canvas.create_rectangle(x - 60, y - 20, x + 180, y + 20, fill="black")  # Corpo do semáforo deitado
    luz_verde = canvas.create_oval(x + 120, y - 20, x + 160, y + 20, fill="black")  # Luz verde à direita
    luz_amarela = canvas.create_oval(x + 60, y - 20, x + 100, y + 20, fill="black")  # Luz amarela no meio
    luz_vermelha = canvas.create_oval(x, y - 20, x + 40, y + 20, fill="black")  # Luz vermelha à esquerda
    return {'verde': luz_verde, 'amarela': luz_amarela, 'vermelha': luz_vermelha}

# Função para criar um semáforo em pé
def criar_semaforo_em_pe(canvas, x, y):
    canvas.create_rectangle(x - 20, y - 60, x + 20, y + 180, fill="black")  # Corpo do semáforo em pé
    luz_verde = canvas.create_oval(x - 20, y + 120, x + 20, y + 160, fill="black")  # Luz verde embaixo
    luz_amarela = canvas.create_oval(x - 20, y + 60, x + 20, y + 100, fill="black")  # Luz amarela no meio
    luz_vermelha = canvas.create_oval(x - 20, y, x + 20, y + 40, fill="black")  # Luz vermelha em cima
    return {'verde': luz_verde, 'amarela': luz_amarela, 'vermelha': luz_vermelha}

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação de Semáforos")

# Criando um canvas para desenhar os semáforos
canvas = tk.Canvas(janela, width=1000, height=800, bg="gray")
canvas.pack()

# Criando múltiplos semáforos, dois deitados e dois em pé
semaforos = []
posicoes_deitado = [(250, 100), (250, 300)]  # Posições dos semáforos deitados
posicoes_em_pe = [(500, 100), (500, 300)]  # Posições dos semáforos em pé

# Criando e adicionando semáforos deitados
for pos in posicoes_deitado:
    luzes = criar_semaforo_deitado(canvas, pos[0], pos[1])
    semaforos.append(luzes)

# Criando e adicionando semáforos em pé
for pos in posicoes_em_pe:
    luzes = criar_semaforo_em_pe(canvas, pos[0], pos[1])
    semaforos.append(luzes)

# Iniciando uma thread para coordenar os semáforos
threading.Thread(target=coordenar_semaforos, args=(canvas, semaforos)).start()

# Iniciando o loop da interface gráfica
janela.mainloop()
