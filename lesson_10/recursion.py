

nested_list = [1, [2, 3], [4, [5, 6]], 7, "Text", {"key": "value"}, [8, [9, [10]]]]


def sort_list(list_with_lists: list):
    for l1 in list_with_lists:
        if isinstance(l1, list):
            sort_list(l1)
        else:
            print(l1)


sort_list(nested_list)
