from groq import Groq

chat = Groq(api_key="")

def enviar_mensage(mensagem):
    resposta = chat.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a personalized AI suport assistant that brings clear and summarized answers to a customer service (give answers that are not very long, are summarized and are not organized into topics)"
            },
            {
                "role": "user",
                "content": mensagem
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return resposta.choices[0].message.content

# print(enviar_mensage("ola"))