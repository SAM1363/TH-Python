def word_count(string):
    counts = dict()
    words = string.lower().split()

    for each in words:
        item = words.count(each)
        counts[each] = item
    
    return counts



# def word_count(string):
#     dictionary = {}
#     list_with_string = string.lower().split() 
#     for item in list_with_string:
#         value = list_with_string.count(item)
#         dictionary[item] = value
#     return dictionary

# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts


print(word_count('samson is a samson or is man or boy'))
