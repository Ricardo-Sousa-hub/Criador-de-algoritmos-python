f = open('teste.txt', 'r')
linelist = f.readlines()
f.close



f2 = open('teste.txt', 'w')
for line in linelist:
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
    line = line.replace('w', 'abrir como escrita')
    line = line.replace('r', 'abrir como leitura')
    f2.write(line)


f2.close()
