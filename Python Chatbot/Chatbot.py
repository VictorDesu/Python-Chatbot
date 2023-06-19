import nltk
from nltk.chat.util import Chat, reflections
import webbrowser
from unidecode import unidecode
import unicodedata

def formatarEntrada(texto):
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.strip("?!@#$%¨&*(){[]}^~´`,.|\/'")
    texto = unidecode(texto)
    texto = ''.join(
        char for char in unicodedata.normalize('NFD', texto)
        if unicodedata.category(char) != 'Mn'
    )
    return texto

# Definindo os padrões de entrada e saída para o chatbot
pares = [
    [
        r"Oi|Ola|e ai|eai|Opa",
        ["Olá!", "Oi!"]
    ],
    [
        r"Oi, tudo bem|tudo bem|Oi, como vai|como vai",
        ["Olá! Tudo bem com você?", "Oi! Como posso ajudar?"]
    ],
    [
        r"bao",
        ["Bão.", "Bão fi."]
    ],
    [
        r"Qual é o seu nome|Qual o seu nome|qual seu nome|Como se chama",
        ["Pode me chamar de Chatbot Test. Estou a seu dispor."]
    ],
    [
        r"Qual é a sua idade|qual sua idade|quantos anos voce tem",
        ["Eu sou um programa de computador, então não tenho uma idade real."]
    ],
    [
        r"Quem criou você|quem é seu criador|por quem voce foi criada|por quem voce foi criado",
        ["Fui criado por Victor, um programador bem bacana!"]
    ],
    [
        r"Abrir (.+)|Abra (.+)",
        ["Abrindo o link"]
    ]
]

# Criando o chatbot
chatbot = Chat(pares, reflections)

# Função para iniciar a conversa
def iniciar_conversa():
    print("Chatbot: Olá! Eu sou o Chatbot Test. Você pode começar a conversa digitando mensagens.")

    # Loop para manter a conversa acontecendo até que o usuário queira sair
    while True:
        entrada = input("Você: ")
        entrada = formatarEntrada(entrada)
        resposta = chatbot.respond(entrada)

        if entrada == "sair" or entrada == "adeus" or entrada == "tchau" or entrada == "até logo":
            resposta = "Até logo!"
            break

        elif entrada.endswith("kk"):
            resposta = "kkkkkkkkkkkkkkkkkkk"

        # Verifica se a resposta do chatbot contém um link
        elif resposta.startswith("Abrindo o link"):
            link = entrada.split(" ")[1]
            opera_gx = webbrowser.get("C:/Users/Windows 10 PRO/AppData/Local/Programs/Opera GX/launcher.exe %s")  # Caminho para o executável do Opera GX
            opera_gx.open(link)  # Abre o link no Opera GX
            print("Chatbot: Abrindo o link ", link)
        
        elif resposta == None:
            resposta = "Não tenho uma resposta para isso."

        print("ChatBot:", resposta)

# Iniciar a conversa
iniciar_conversa()
