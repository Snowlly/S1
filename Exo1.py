def test_distinct(list):
    return len(list) == len(set(list))
        


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))


