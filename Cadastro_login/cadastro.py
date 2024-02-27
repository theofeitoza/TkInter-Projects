from tkinter import *
from tkinter import ttk

def get_login():
    global login_entry
    login=login_entry.get()
    try:
        return str(login)
    except ValueError:
        return None

def get_senha():
    global senha_entry
    senha=senha_entry.get()
    try:
        return str(senha)
    except ValueError:
        return None

def verificacao():
    login=get_login()
    senha=get_senha()
    if login or senha == None:
        retorno.configure(text='Um erro ocorreu')
    else:
        if login == '202200343' and senha == '12345678':
                retorno.configure(text='Usuario logado')
        else:
                retorno.configure(text='Usuario nao reconhecido')


cadastro = Tk()

cadastro.title("Cadastro")
cadastro.geometry("480x200")

texto1=ttk.Label(cadastro,text='Login:')
texto1.grid(column=1, row=1)

login_entry=ttk.Entry(cadastro,width=10)
login_entry.grid(column=2,row=1)

texto2=ttk.Label(cadastro,text='Senha:')
texto2.grid(column=1, row=2)

senha_entry=ttk.Entry(cadastro,width=10)
senha_entry.grid(column=2,row=2)

botao=ttk.Button(cadastro,text="Logar", command=verificacao)
botao.grid(column=2,row=3)

retorno=Label(cadastro, text="")
retorno.grid(column=1, row=4)

cadastro.mainloop()