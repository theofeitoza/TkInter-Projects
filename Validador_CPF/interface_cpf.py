import re
import sys
from tkinter import *
from tkinter import ttk

cor1="#3d3d3d" #preto
cor2="#fafcff" #branco
cor3="#21c25c" #verde
cor4="#eb463b" #vermelho
cor5="#dedcdc" #cinza
cor6="#3080f0" #azul

def get_cpf():
    global cpf_entry
    cpf_enviado=cpf_entry.get()
    try:
        return str(cpf_enviado)
    except ValueError:
        return None

def get_nome():
    global nome_entry
    nome=nome_entry.get()
    try:
        return str(nome)
    except ValueError:
        return None
    
def validar_cpf():
    cpf_enviado=get_cpf()
    nome_enviado=get_nome()
    cpf_enviado=re.sub(r'[^0-9]','',cpf_enviado)

    entrada_sequencial=cpf_enviado==cpf_enviado[0]*len(cpf_enviado)

    if entrada_sequencial:
        sys.exit()

    nove_digitos=cpf_enviado[:9]
    contador_regressivo_1=10
    resultado_digito_1=0

    for digito in nove_digitos:
        resultado_digito_1+=int(digito)*contador_regressivo_1
        contador_regressivo_1-=1
    digito_1=((resultado_digito_1*10)%11)
    digito_1=digito_1 if digito_1<=9 else 0

    dez_digitos=nove_digitos+str(digito_1)
    contador_regressivo_2=11
    resultado_digito_2=0

    for digito in dez_digitos:
        resultado_digito_2+=int(digito)*contador_regressivo_1
        contador_regressivo_2-=1
    digito_2=((resultado_digito_2*10)%11)
    digito_2=digito_2 if digito_1<=9 else 0

    novo_cpf=f'{nove_digitos}{digito_1}{digito_2}'
    if novo_cpf==cpf_enviado:
        retorno.config(text=f'Ola, {nome_enviado}\nO CPF de numero {cpf_enviado} é válido\nCadastro realizado com sucesso')
    else:
        retorno.config(text=f'Ola, {nome_enviado}\nO CPF de numero {cpf_enviado} é inválido\n Tente realizar o cadastro novamente')

janela = Tk()
janela.title('Validador de CPF')
janela.geometry('360x150')
janela.resizable(width=FALSE, height=FALSE)

frame_cima= Frame(janela, width=360, height=75, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo= Frame(janela, width=360, height=75, bg=cor2)
frame_baixo.grid(row=2, column=0)

nome=Label(frame_cima,text='Digite seu nome completo:', bg=cor2,fg=cor1)
nome.place(x=10, y=5)

nome_entry=ttk.Entry(frame_cima, width=30, background=cor1)
nome_entry.place(x=160, y=5)

cpf=Label(frame_cima,text='Digite seu numero de CPF:', bg=cor2,fg=cor1)
cpf.place(x=10, y=30)

cpf_entry=ttk.Entry(frame_cima, width=30, background=cor1)
cpf_entry.place(x=160, y=30)

botao=ttk.Button(frame_cima,text="Validar CPF", command=validar_cpf)
botao.place(x=10, y=50)

retorno=Label(frame_baixo, text="", bg=cor2, fg=cor1)
retorno.place(x=80, y=0)

janela.mainloop()