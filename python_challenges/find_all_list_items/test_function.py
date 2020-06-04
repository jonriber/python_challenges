from find_all_list_items import find_list_items


def test_func_returning_parameters():
    example = [1,2,3]
    assert find_list_items(example) == [1,2,3]
