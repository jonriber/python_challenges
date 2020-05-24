def check_palindrome(word):
    palindrome = word[::-1]
    if word == palindrome:
        return True
    return False
        

if __name__ == '__main__':
    print('Iniciando programa.')
    while True:
        word = str(input('Digite uma palavra para verificar se possui palindromo:'))
        print(f'a palavra {word} possui palindromo?')
        result = check_palindrome(word)
        if result == True:
            print('sim')
        else:
            print('não')
        print('Deseja continuar?')
        continuar = input('Sim ou não?')
        if continuar == 'não' or continuar == 'nao' or continuar == 'Não':
            break
    print('Programa Finalizado!')