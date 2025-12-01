def test_distinct(list):
    r = []
    n = len(list)
    for i in range(n):
        for j in range(n):
            if (list[i] == list[j]):
                r.append(list[i] == list[j])
    return r

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))


