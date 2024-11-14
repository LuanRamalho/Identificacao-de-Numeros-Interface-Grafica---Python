import tkinter as tk
from tkinter import messagebox

def verificar_divisibilidade():
    try:
        num = int(entry.get())
        divisores = []

        for i in range(2, 11):
            if num % i == 0:
                divisores.append(i)

        if divisores:
            messagebox.showinfo("Resultado", f"Número: {num}\nDivisível por: {', '.join(map(str, divisores))}")
        else:
            messagebox.showinfo("Resultado", f"Número: {num}\nNão é divisível por nenhum número de 2 a 10.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número inteiro válido.")

# Configurações da janela principal
root = tk.Tk()
root.title("Verificador de Divisibilidade")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Título
titulo = tk.Label(root, text="Verificador de Divisibilidade", font=("Arial", 16), bg="#f0f8ff", fg="#2e8b57")
titulo.pack(pady=20)

# Entrada de número
entry_label = tk.Label(root, text="Digite um número inteiro:", font=("Arial", 12), bg="#f0f8ff", fg="#000000")
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=10)
entry.pack(pady=5)

# Botão para verificar divisibilidade
verificar_button = tk.Button(root, text="Verificar", font=("Arial", 12), bg="#2e8b57", fg="#ffffff", command=verificar_divisibilidade)
verificar_button.pack(pady=20)

# Loop principal
root.mainloop()
