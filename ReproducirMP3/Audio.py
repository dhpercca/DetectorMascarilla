from gtts import gTTS
from playsound import playsound

'''with open("contenido.txt", "w") as file:
    file.write("Hola, soy tu asistente por voz.")
    file.write("\n")
    file.write("¿Qué necesitas?")
    file.close()

def voz(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.read()
    file = gTTS(text=text,lang=lang)
    filename = name_file
    file.save(filename)

voz("contenido.txt","es","voz.mp3")'''
#Para reproducir un mp3, solo se necesita ejecutar las siguientes dos lineas
audio = "voz.mp3"
playsound(audio)

