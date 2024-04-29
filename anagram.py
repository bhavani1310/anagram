
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    count1 = {}
    count2 = {}
    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    for char in str2:
        count2[char] = count2.get(char, 0) + 1
    if count1 == count2:
        return True
    else:
        return False
str1 = input()
str2 = input()
print(are_anagrams(str1,str2))






