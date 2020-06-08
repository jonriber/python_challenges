# O objetivo é criar uma função para salvar um dicionário em um arquivo externo
# Então criar outra função para recuperar esse dicionário através deste arquivo
# utilizar 'pickle' - object serialization
import pickle

def save_content(dictionary,file_path):
    with open(file_path,'wb') as file:
        pickle.dump(dictionary,file)

def retrieve_content(file_path):
    with open(file_path,'rb') as file:
        return pickle.load(file)



if __name__ == '__main__':
    dictionary = {'1':'first','2':'second','3':'third'}
    print("Welcome to the save a dictionary to a file script")
    file_name = input('first, choose a name to save the file:')
    save_content(dictionary,file_name)

    print('now, returning the content')
    print(retrieve_content(file_name))

