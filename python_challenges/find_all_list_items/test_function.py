# Utilizando pytest para realizar TDD e tentar quebrar o código

from find_all_list_items import find_list_items,index_func


def test_func_returning_parameters():
    example = [1,2,3]
    assert find_list_items(example) == [1,2,3]

def test_index_func_simple_1():
    search_list = [[[1,2,3],2,[1,3]],[1,2,3]]
    item = 2

    assert index_func(search_list,item) == [[0,0,1],[0,1],[1,1]]

def test_index_func_simple_2():
    search_list = [1,2,3,2,4,2]
    item = 2
    assert index_func(search_list,item) == [[1],[3],[5]]

def test_index_func_simple_3():
    search_list = [2]
    item = 2
    assert index_func(search_list,item)==[[0]]
