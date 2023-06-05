def find_common_elements( list1, list2):
    common_elements = []
    for element in list1:
         if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

list1= [2,3,4,5,6,7]
list2= [1,3,4,5,6]
common_elements = find_common_elements(list1, list2)
print(common_elements)