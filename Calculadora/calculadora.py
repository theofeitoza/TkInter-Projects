from tkinter import *
from tkinter import ttk

cor1="#3b3b3b"
cor2="#feffff"
cor3="#38576b"
cor4="#ECEFF1"
cor5="#FFAB40"


janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)

def entrar_valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")

todos_valores = "" 
valor_texto = StringVar()

frame_tela= Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=235, height=260, bg=cor3)
frame_corpo.grid(row=1, column=0)

calc_label= Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3)
calc_label.place(x=0, y=0)

botao1=Button(frame_corpo,text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: limpar_tela())
botao1.place(x=0, y=0)

botao2=Button(frame_corpo,text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valor('%'))
botao2.place(x=118, y=0)

botao3=Button(frame_corpo,text="/", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('/'))
botao3.place(x=177, y=0)

botao4=Button(frame_corpo,text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('7'))
botao4.place(x=0, y=52)

botao5=Button(frame_corpo,text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('8'))
botao5.place(x=59, y=52)

botao6=Button(frame_corpo,text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('9'))
botao6.place(x=118, y=52)

botao7=Button(frame_corpo,text="*", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('*'))
botao7.place(x=177, y=52)

botao8=Button(frame_corpo,text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('4'))
botao8.place(x=0, y=104)

botao9=Button(frame_corpo,text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('5'))
botao9.place(x=59, y=104)

botao10=Button(frame_corpo,text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('6'))
botao10.place(x=118, y=104)

botao11=Button(frame_corpo,text="-", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('-'))
botao11.place(x=177, y=104)

botao4=Button(frame_corpo,text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('1'))
botao4.place(x=0, y=156)

botao5=Button(frame_corpo,text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('2'))
botao5.place(x=59, y=156)

botao6=Button(frame_corpo,text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('3'))
botao6.place(x=118, y=156)

botao7=Button(frame_corpo,text="+", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('+'))
botao7.place(x=177, y=156)

botao1=Button(frame_corpo,text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor('0'))
botao1.place(x=0, y=208)

botao2=Button(frame_corpo,text=",", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valor(','))
botao2.place(x=118, y=208)

botao3=Button(frame_corpo,text="=", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: calcular())
botao3.place(x=177, y=208)

janela.mainloop()