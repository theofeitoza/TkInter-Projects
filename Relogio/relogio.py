from tkinter import *
from datetime import datetime

from pyglet import *
options['win32_gdi_font'] = True
font.add_file("digital-7.ttf")

cor1="#3d3d3d" #preto
cor2="#fafcff" #branco
cor3="#21c25c" #verde
cor4="#eb463b" #vermelho
cor5="#dedcdc" #cinza
cor6="#3080f0" #azul

fundo=cor1
cor=cor2

janela= Tk()
janela.title('')
janela.geometry('470x180')
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor1)

def relogio():
    tempo=datetime.now()
    hora=tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")

    label1.config(text=hora)
    label1.after(1000,relogio)
    label2.config(text=dia_semana + " " + str(dia) + " " + str(mes) + " " + str(ano))

label1=Label(janela, text= "", font=('digital-7 110'), bg=fundo, fg=cor)
label1.grid(row=0, column=0, sticky=NW, padx=5)

label2=Label(janela, text= "", font=("digital-7 17"), bg=fundo, fg=cor)
label2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()