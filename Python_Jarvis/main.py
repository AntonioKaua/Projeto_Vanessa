from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
time.clock = time.time
num_audio = 1



def ouvir():
    global frase
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Ouvindo...")
        audio = mic.listen(source)
    try:
        frase = mic.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        print("Não entendi")
    return frase


def cria_audio(audio):
    global num_audio
    try:
        filename = f"bot{num_audio}.mp3"
        tts = gTTS(audio, lang='pt-BR')
        tts.save(filename)
        playsound(filename)
        num_audio += 1
        os.remove(filename)
    except PermissionError:
        print("Erro ao salvar mp3")


Bot = ChatBot("Vanessa")
conversa = ['Oi',
            'Olá, tudo bem?',
            'Tudo bem?',
            'Tudo ótimo, e você?',
            'Estou ótimo',
            'Quem bom',
            'Como você está?',
            'Estou bem, obrigado por perguntar.',
            'Qual é o seu nome?',
            'Meu nome é Vanessa, estou aqui para ajudar.',
            'O que você gosta de fazer?',
            'Gosto de conversar e ajudar as pessoas.',
            'Qual é a sua cor favorita?',
            'Não tenho uma cor favorita, mas gosto de todas.',
            'Você gosta de música?',
            'Sim, música é uma forma de expressão incrível.',
            'O que você faz?',
            'Sou um programa de computador projetado para conversar com pessoas.',
            'Você é humano?',
            'Não, sou uma inteligência artificial criada por Antônio Kauã, o cruel.',
            'Você tem irmãos ou irmãs?',
            'Não, sou filha única.',
            'Qual é o seu objetivo?',
            'Meu objetivo é ajudar pessoas com deficiência visual.',
            'Você pode me contar uma piada?',
            'Claro, aqui vai uma piada: Por que o programador colocou um interruptor debaixo da cama? Para desligar o sono profundo.',
            'Obrigado, isso me fez sorrir.',
            'Fico feliz em ouvir isso!',
            'Até mais tarde!',
            'Até logo, tenha um ótimo dia!']


trainer = ListTrainer(Bot)
trainer.train(conversa)

while True:
    quest = ouvir()
    resposta = Bot.get_response(quest)
    cria_audio(str(resposta.text))
    print("Bot: ", resposta)
