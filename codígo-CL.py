import tkinter as tk
from tkinter import messagebox
import math

class Calculadora(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calculadora")
        self.geometry("400x600")
        self.configure(bg="black")  # Define o fundo da janela como preto
        
        # Configurar o layout
        self.criar_widgets()

    def criar_widgets(self):
        # Área de entrada
        self.entrada = tk.Entry(self, font=("Arial", 28), borderwidth=2, relief="solid", bg="black", fg="white")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Menu de operações
        self.operacao_var = tk.StringVar(self)
        self.operacao_var.set("Escolha a operação")
        operacoes = ["+", "-", "*", "/", "Raiz Quadrada", "Raiz Cúbica", "Potência"]
        self.menu_operacoes = tk.OptionMenu(self, self.operacao_var, *operacoes)
        self.menu_operacoes.config(bg="black", fg="white", font=("Arial", 18))
        self.menu_operacoes.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Botões numéricos e de operações básicas
        botoes = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("C", 5, 2), ("+", 5, 3)
        ]

        for texto, linha, coluna in botoes:
            if texto == "C":
                botao = tk.Button(self, text=texto, font=("Arial", 24), command=self.limpar_entrada, bg="red", fg="white")
            else:
                botao = tk.Button(self, text=texto, font=("Arial", 24), command=lambda t=texto: self.adicionar_texto(t), bg="gray", fg="white")
            botao.grid(row=linha, column=coluna, sticky="nsew")

        # Botão de cálculo
        self.botao_calcular = tk.Button(self, text="Calcular", font=("Arial", 24), command=self.calcular, bg="blue", fg="white")
        self.botao_calcular.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Ajustar o tamanho das colunas e linhas
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def adicionar_texto(self, texto):
        # Adiciona o texto ao campo de entrada
        atual = self.entrada.get()
        if texto == "." and "." in atual:
            return
        self.entrada.insert(tk.END, texto)

    def limpar_entrada(self):
        # Limpa o campo de entrada
        self.entrada.delete(0, tk.END)

    def calcular(self):
        try:
            operacao = self.operacao_var.get()
            entrada = self.entrada.get()
            
            if operacao in ["+", "-", "*", "/"]:
                resultado = eval(entrada)
            elif operacao == "Raiz Quadrada":
                numero = float(entrada)
                if numero < 0:
                    raise ValueError("Número negativo para raiz quadrada.")
                resultado = math.sqrt(numero)
            elif operacao == "Raiz Cúbica":
                numero = float(entrada)
                resultado = numero ** (1/3)
            elif operacao == "Potência":
                base, expoente = map(float, entrada.split(","))
                resultado = base ** expoente
            else:
                raise ValueError("Operação inválida.")
            
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception as e:
            messagebox.showerror("Erro", f"Entrada inválida ou cálculo falhou: {e}")
            self.entrada.delete(0, tk.END)

class AplicacaoPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação Principal")
        self.geometry("300x200")
        self.criar_widgets()

    def criar_widgets(self):
        # Botão para abrir a calculadora
        self.botao_calculadora = tk.Button(self, text="Abrir Calculadora", font=("Arial", 16), command=self.abrir_calculadora, bg="blue", fg="white")
        self.botao_calculadora.pack(pady=20)

    def abrir_calculadora(self):
        Calculadora(self)

if __name__ == "__main__":
    app = AplicacaoPrincipal()
    app.mainloop()
