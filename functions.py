def name_of_individual(age):
    if age>= 10:
        print(' hey, you are already old enough. ganbare desu')
        return ' hey, you are already old enough. ganbare desu'
    else:
        print('i ie, dame desu yo')
        return 'i ie, dame desu yo'
    
name_of_individual(20)


def sum(a, b):
    print(a, b)
    a -= 1 
    if a> 0:
        sum(a, b)

sum= (3,4)
# recursions may not be useful unlessyou wanna become a scientist






