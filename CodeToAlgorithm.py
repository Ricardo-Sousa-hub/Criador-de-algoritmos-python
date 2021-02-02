from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Beta-CodeToAlgorithm")
root.geometry("500x450")


def abrir_txt():
    ficheiro = filedialog.askopenfilename(initialdir="C:/", title="Abrir ficheiro",
                                          filetypes=(("Text Files", "*.txt"),))
    aux = open(ficheiro, "r")
    codigo = aux.readlines()

    texto.insert(END, codigo)
    aux.close()

    ficheiro = open(ficheiro, "w")

    for line in codigo:
        line = line.replace('print', 'ver')
        line = line.replace('input', 'ler')
        line = line.replace('try', 'tenta')
        line = line.replace('if', 'se')
        line = line.replace('elif', 'se tambem')
        line = line.replace('else', 'entao')
        line = line.replace('except', 'excepto')
        line = line.replace('for', 'para')
        line = line.replace('append', 'adicionar')
        line = line.replace('while True', 'enquanto verdadeiro')
        line = line.replace('break', 'parar')
        line = line.replace('continue', 'continuar')
        line = line.replace('return', 'devolve')
        line = line.replace('range', 'alcance')
        line = line.replace('len', 'tamanho')
        line = line.replace('insert', 'inserir na posicao')
        line = line.replace('replace', 'subestituir')
        line = line.replace('remove', 'remover')
        line = line.replace('open', 'abrir')
        line = line.replace('close', 'fechar')
        line = line.replace('with', 'com')
        line = line.replace('pop', 'remover da posicao')
        line = line.replace('while', 'enquanto')
        line = line.replace('split', 'dividir')
        line = line.replace('write', 'escreve')
        ficheiro.write(line)
    ficheiro.close()
    messagebox.showinfo(title="Concluido", message="Tarefa concluida")
    exit()


texto = Text(root, width=40, height=10, font=("Helvetica", 16))
texto.pack(pady=20)

btn_abrir = Button(root, text="Abrir ficheiro", command=abrir_txt)
btn_abrir.pack(pady=20)

root.mainloop()
