def list_of_words(words):
    new_list = []
    for word in words:
        if len(word)>4:
            new_list.append(word)
    return new_list



words= ['ace', 'mango', 'carrot', 'cheese', 'brandy']
list_of_words= list_of_words(words)
print(list_of_words)