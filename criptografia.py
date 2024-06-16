from cryptography.fernet import Fernet

def criptografa_msg(mensagem, chave):
    fernet = Fernet(chave)
    return fernet.encrypt(mensagem.encode())

def descriptografa_msg(mensagem_criptografada, chave):
    fernet = Fernet(chave)
    return fernet.decrypt(mensagem_criptografada).decode()
