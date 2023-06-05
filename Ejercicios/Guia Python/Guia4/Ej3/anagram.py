def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    return sorted_list1 == sorted_list2