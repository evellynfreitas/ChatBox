import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def responder(pergunta, mensagens_anteriores=[]):
    mensagens_anteriores.append({"role": "user", "content": pergunta})

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensagens_anteriores
    )

    return resposta["choices"][0]["message"]


mensagens_anteriores = []
while (True):
    entrada = input("Digite sua mensagem: ")
    resposta = responder(entrada, mensagens_anteriores)
    mensagens_anteriores.append(resposta)

    print("ChatGPT:", resposta["content"])
