def first_unique(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for index, char in enumerate(s):
        if count[char] == 1:
            return index
    return -1
s = "leetcode"
result = first_unique(s)
print(result)
