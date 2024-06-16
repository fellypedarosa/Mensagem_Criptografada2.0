# Sistema de Mensagens Criptografadas

Este é um sistema de mensagens criptografadas desenvolvido em Python, que permite aos usuários enviar mensagens de forma segura.

## Funcionalidades

- Autenticação de usuário com tela de login.
- Envio de mensagens criptografadas de forma segura.
- Leitura de mensagens recebidas.
- Interface gráfica simples e intuitiva.

## Como usar

1. **Instalação:**

   Certifique-se de ter o Python instalado. Você também precisa instalar as dependências do projeto.
   
3. **Execução:**

Execute o arquivo `inicio.py` para iniciar o aplicativo:


3. **Autenticação:**

- Na tela de login, digite seu nome de usuário e senha para acessar o sistema.
- Após o login, você poderá enviar mensagens criptografadas e ler mensagens recebidas.

4. **Enviar mensagem:**

- Digite sua mensagem no campo de texto.
- Clique no botão "Enviar" para enviar a mensagem criptografada.

5. **Ler mensagens:**

- Clique no botão "Ler" para visualizar as mensagens recebidas.

6. **Limpar mensagens:**

- Clique em "Limpar Mensagens" para limpar todas as mensagens do arquivo de texto.

## Detalhes técnicos

- **Autenticação:** O sistema utiliza autenticação de usuário para garantir o acesso seguro às mensagens.
- **Criptografia:** As mensagens são criptografadas utilizando a biblioteca `cryptography` para garantir a segurança durante a transmissão.
- **Interface gráfica:** A interface é construída com Tkinter para proporcionar uma experiência de usuário simples e amigável.
-  **Armazenamento de usuários:** Os usuários registrados são armazenados no arquivo `usuarios.json`.


## Estrutura do projeto

- **autenticacao.py:** Contém a lógica de autenticação de usuário.
- **criptografia.py:** Contém funções para criptografar e descriptografar mensagens.
- **mensagem.py:** Possui funções para enviar e ler mensagens.
- **inicio.py:** Arquivo principal que inicia a interface do aplicativo.
- **cria_chave:** Cria um novo arquivo de chave.key ou atualiza a axistente.
- **chave.key:** Arquivo contendo a chave de criptografia.
- **mensagem.txt:** Arquivo onde as mensagens são armazenadas.

## Dependências

- cryptography
- bcrypt
- tkinter

### Login

![Captura de tela 2024-06-16 014017](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/46409a28-8572-4c84-b1cf-7283173f9cab)

### Leitura de Mensagem

![Captura de tela 2024-06-16 014553](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/b76e0ace-c3f0-4bdf-9402-7e4f71864fad)


### Leitura sem haver mensagens no arquivo de texto

![Captura de tela 2024-06-16 014422](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/df0c2c0f-1be7-444c-b22c-f3b7ce35e2e2)

### Envio de Mensagem
![Captura de tela 2024-06-16 014513](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/0f02dbc3-e5f2-42a8-afe5-50887939ed31)

### Limpeza de mensagens

![Captura de tela 2024-06-16 021138](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/aedc6a11-089e-436c-8421-a6d54afb9239) ![Captura de tela 2024-06-16 021148](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/7b1c4ccc-ff21-491c-9892-ffe1e3201f1b)

### Segurança
#### Arquivo de `mensagem.txt` totalmente criptografado

![Captura de tela 2024-06-16 021440](https://github.com/fellypedarosa/Mensagem_Criptografada2.0/assets/171340743/52472692-96b0-4b21-b3a1-c84e3f26a3ef)






