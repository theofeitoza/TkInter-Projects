from tkinter import *
from tkinter import ttk

def get_avista():
    global avista_entry
    avista=avista_entry.get()
    try:
        return float(avista)
    except ValueError:
        return None

def get_aprazo():
    global aprazo_entry
    aprazo=aprazo_entry.get()
    try:
        return float(aprazo)
    except ValueError:
        return None

def get_taxa():
    global taxa_entry
    taxa=taxa_entry.get()
    try:
        return float(taxa)
    except ValueError:
        return None
    
def get_parcelas():
    global parcelas_entry
    parcelas=parcelas_entry.get()
    try:
        return int(parcelas)
    except ValueError:
        return None

def calculo():
    aprazo=get_aprazo()
    avista=get_avista()
    parcelas=get_parcelas()
    taxa=get_taxa()
    parcela = aprazo/parcelas
    porcentagem=taxa/100
    montante=avista
    for t in range(parcelas):
        montante = montante + montante * porcentagem
        montante -= parcela
    if montante<0:
        aviso.configure(text=f"É preferivel comprar o produto a vista \n nesta modalidade voce teria uma economia de R${-montante}")
    else:
        aviso.configure(text=f"É preferivel comprar o produto a prazo \n nesta modalidade voce teria uma economia de R${montante}")

janela = Tk()
janela.title("Valor futuro a valor presente")
janela.geometry("480x200")

aviso=Label(janela, text="")
aviso.grid(column=5, row=11)

texto_avista= ttk.Label(janela, text="Digite o valor do produto a vista: R$")
texto_avista.grid(column=5, row=1)

avista_entry=ttk.Entry(janela,width=10)
avista_entry.grid(column=6,row=1)


texto_aprazo= ttk.Label(janela, text="Digite o valor do produto a prazo: R$")
texto_aprazo.grid(column=5, row=3)

aprazo_entry=ttk.Entry(janela,width=10)
aprazo_entry.grid(column=6,row=3)


texto_aprazo= ttk.Label(janela, text="Digite a quantidade de parcelas: ")
texto_aprazo.grid(column=5, row=5)

parcelas_entry=ttk.Entry(janela,width=10)
parcelas_entry.grid(column=6,row=5)


texto_aprazo= ttk.Label(janela, text="Digite a taxa de rendimentos: ")
texto_aprazo.grid(column=5, row=7)

taxa_entry=ttk.Entry(janela,width=10)
taxa_entry.grid(column=6,row=7)


botao=ttk.Button(janela,text="Fazer comparação", command=calculo)
botao.grid(column=6,row=9)

janela.mainloop()