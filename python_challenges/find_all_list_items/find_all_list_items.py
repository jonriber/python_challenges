# Função de pesquisa de um elemento em uma lista dada.
# O resultado é uma lista com o índice do elemento pesquisado dentro da lista de pesquisa;

def find_list_items(a_list):
    return a_list

def index_func(search_list,item):
    result = []
    for i in range(len(search_list)):
        if search_list[i] == item:
            result.append([i])
        elif isinstance(search_list[i],list):
            for index in index_func(search_list[i],item):
                result.append([i]+index)
        
    return result