import tkinter as tk
from tkinter import messagebox
from autenticacao import UserManager
from criptografia import criptografa_msg, descriptografa_msg
from mensagem import enviar_mensagem, ler_mensagem
import cryptography.fernet

class SecureChatApp:
    def __init__(self, root):
        self.user_manager = UserManager()
        self.current_user = None

        self.root = root
        self.root.title("Secure Chat")

        self.login_frame = tk.Frame(self.root)
        self.chat_frame = tk.Frame(self.root)

        self.setup_login_frame()
        self.setup_chat_frame()

    def setup_login_frame(self):
        tk.Label(self.login_frame, text="Usuário").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Senha").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(self.login_frame, text="Registrar", command=self.register).grid(row=2, column=1)

        self.login_frame.pack()

    def setup_chat_frame(self):
        self.text_chat = tk.Text(self.chat_frame, wrap=tk.WORD)
        self.text_chat.pack()

        self.entry_message = tk.Entry(self.chat_frame, width=50)
        self.entry_message.pack(padx=10, pady=5)

        button_frame = tk.Frame(self.chat_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Enviar", command=self.send_message).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Ler", command=self.read_message).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Limpar Mensagens", command=self.clear_messages).pack(side=tk.LEFT, padx=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.authenticate_user(username, password):
            self.current_user = username
            self.login_frame.pack_forget()
            self.chat_frame.pack()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.user_manager.create_user(username, password)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def send_message(self):
        mensagem = self.entry_message.get()
        enviar_mensagem(mensagem, self.get_chave())
        self.text_chat.insert(tk.END, "Mensagem enviada!\n")
        self.entry_message.delete(0, tk.END)

    def read_message(self):
        chave = self.get_chave()
        if chave is None:
            return

        try:
            mensagens = ler_mensagem(chave)
            self.text_chat.delete(1.0, tk.END)  # Limpa a área de texto
            for mensagem in mensagens:
                self.text_chat.insert(tk.END, mensagem + "\n")
        except cryptography.fernet.InvalidToken:
            messagebox.showerror("Erro", "Não foi possível descriptografar as mensagens. A chave pode estar incorreta.")

    def clear_messages(self):
        confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar todas as mensagens?")
        if confirmacao:
            with open("mensagem.txt", "wb") as file:
                file.truncate(0)
            self.text_chat.delete(1.0, tk.END)
            messagebox.showinfo("Sucesso", "Todas as mensagens foram limpas.")

    def get_chave(self):
        try:
            with open('chave.key', 'rb') as filekey:
                chave = filekey.read()
            return chave
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de chave não encontrado")
            return None

# Iniciar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SecureChatApp(root)
    root.mainloop()
