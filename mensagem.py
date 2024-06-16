from criptografia import criptografa_msg, descriptografa_msg
import cryptography.fernet    # Importa a exceção InvalidToken


# Função para enviar mensagem
def enviar_mensagem(mensagem, chave):
    mensagem_criptografada = criptografa_msg(mensagem, chave)
    with open("mensagem.txt", "ab") as file:
        file.write(mensagem_criptografada + b"\n")
    print("Mensagem enviada!")

# Função para ler mensagem
def ler_mensagem(chave):
    mensagens = []
    try:
        with open("mensagem.txt", "rb") as file:
            conteudo = file.readlines()
            if conteudo:
                for mensagem_criptografada in conteudo:
                    try:
                        mensagem = descriptografa_msg(mensagem_criptografada.strip(), chave)
                        mensagens.append(mensagem)
                    except cryptography.fernet.InvalidToken:
                        mensagens.append("Erro: Não foi possível descriptografar a mensagem. Chave incorreta ou mensagem corrompida.")
            else:
                mensagens.append("Não ha mensagens ainda.")
    except FileNotFoundError:
        mensagens.append("O arquivo mensagem.txt não foi encontrado. Envie uma mensagem primeiro.")
    return mensagens

