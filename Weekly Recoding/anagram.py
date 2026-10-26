def anagram(str1: str, str2: str):
    if len(str1) != len(str2):
        return "Not an anagram"
    
    store1 = {}
    store2 = {}
    for i in str1.lower():
        if i not in store1:
            store1[i] = 1
        else:
            store1[i] += 1
    for j in str2.lower():
        if j not in store2:
            store2[j] = 1
        else:
            store2[j] += 1

    if store1 == store2:
        return "Anagram"
    else:
        return "Not an anagram"

print(anagram("hello", "world"))