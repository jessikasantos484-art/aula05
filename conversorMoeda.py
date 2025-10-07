import tkinter as tk

# Fução que consome uma api publica
from moeda import apidolar


def dolar():
    cotacao = float(apidolar())
    reais = float(valor.get())
    conta = round(reais / cotacao,2)
    mensagem = f'Com R$ {reais} reais compra-se $ {conta} dólares'
    resposta.config(text=mensagem)
    return mensagem

janela = tk.Tk()

janela.geometry('2500x500')
janela.title('Aula05 - Tkinter com API')
janela.configure(bg='#0FC2C0')

titulo = tk.Label(janela, text ='Conversor de Reais para Dólar', font =('Verdana', 16), fg= '#023535', bg ='#015958')
titulo.pack(pady=10)

rotulo = tk.Label(janela, text='Digite valor em Reais para Converter:', font=('Verdana',12), fg='#0FC2C0', bg='#0FC2C0') 
rotulo.pack(pady=10)

valor = tk.Entry(janela, bg= '#0FC2C0', fg ='#023535')
valor.pack(pady=10)

botao = tk.Button(janela, text= 'CONVERTER', command=dolar, bg='#0FC2C0', fg= '#0FC2C0' )
botao.pack(pady=10)

resposta = tk.Label(janela, text='', font=('Verdana',12), fg='#0FC2C0', bg='#023535') 
resposta.pack(pady=10)


janela.mainloop()











janela.mainloop()