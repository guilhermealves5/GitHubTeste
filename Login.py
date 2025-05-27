import tkinter as tk  #bibliotecas
from tkinter import messagebox
from PIL import Image, ImageTk

# login do usuario
def verificar_login():  
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "usuario" and senha == "senha":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        janela.destroy()
    else: 
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

janela = tk.Tk()   # Tela
janela.title("Sistema de Login")
janela.geometry("1280x720")  # Tamanho fixo opcional

# fundo
imagem_fundo = Image.open("fundo.webp")
imagem_fundo = imagem_fundo.resize((1280, 720))  # Ajusta ao tamanho da janela
fundo = ImageTk.PhotoImage(imagem_fundo)

label_fundo = tk.Label(janela, image=fundo)
label_fundo.place(relwidth=1, relheight=1)

# frame para os widgets
frame = tk.Frame(janela, bg="#000000", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

# formatação dos textos
fonte = ("Arial", 12, "bold")
cor_texto = "white"

# texto do usuario
rotulo_usuario = tk.Label(frame, text="Usuário:", font=fonte, fg=cor_texto, bg="#000000")
rotulo_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#entrada de informação
entrada_usuario = tk.Entry(frame)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

#texto da senha
rotulo_senha = tk.Label(frame, text="Senha:", font=fonte, fg=cor_texto, bg="#000000")
rotulo_senha.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#entrada de informação
entrada_senha = tk.Entry(frame, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=10)
#botão de login
botao_login = tk.Button(frame, text="Login", font=fonte, bg="#1e90ff", fg="white", command=verificar_login)
botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

frame.grid_columnconfigure(1, weight=1)

janela.mainloop()
