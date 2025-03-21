import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

executando = False  # Variável para controlar a execução

def iniciar_script():
    global executando
    if executando:
        messagebox.showinfo("Informação", "O script já está em execução.")
        return

    inicial = entrada_inicial.get()
    quantidade = entrada_quantidade.get()

    if not inicial:
        messagebox.showerror("Erro", "Por favor, insira um valor inicial.")
        return

    if not quantidade:
        messagebox.showerror("Erro", "Por favor, insira a quantidade de iterações.")
        return

    try:
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
        return

    executando = True

    def executar_automacao():
        global executando
        time.sleep(5)  # Adiciona um atraso de 5 segundos antes de começar
        i = 0
        while i < quantidade and executando:
            pyautogui.press('end')
            pyautogui.press('backspace')
            pyautogui.write(inicial)
            pyautogui.press('tab')
            i += 1
        executando = False
        messagebox.showinfo("Informação", "Script concluído ou interrompido.")

    threading.Thread(target=executar_automacao).start()
    messagebox.showinfo("Informação", "Script iniciado, será executado em 5 segundos.!")

def parar_script():
    global executando
    if executando:
        executando = False
        messagebox.showinfo("Informação", "Solicitação de parada enviada.")
    else:
        messagebox.showinfo("Informação", "O script não está em execução.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Automação")
janela.geometry("250x150") # Aumenta a altura da janela

# Label e entrada para o valor inicial
label_inicial = tk.Label(janela, text="Valor Inicial:")
label_inicial.pack()
entrada_inicial = tk.Entry(janela)
entrada_inicial.pack()

# Label e entrada para a quantidade de iterações
label_quantidade = tk.Label(janela, text="Quantidade:")
label_quantidade.pack()
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack()

# Botão para iniciar o script
botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_script)
botao_iniciar.pack()

# Botão para parar o script
botao_parar = tk.Button(janela, text="Parar", command=parar_script)
botao_parar.pack()

janela.mainloop()