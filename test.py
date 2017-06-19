with open('entrada.txt') as texto, open('saida.txt', 'w') as saida:
    # Crie um arquivo chamado 'entrada.txt' e cole o texto dentro
    # Não é necessário criar 'saida.txt' o programa já irá criá-lo automaticamente.
        for linha in texto.readlines():
            linha = linha.replace('\n', '')
            saida.write(linha)
texto.close()
saida.close()
