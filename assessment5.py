def multiply_even_number(numbers):
    num=1
    for no in numbers:
        if no%2 == 0:
            num= no

    return num


numbers=[2,3,4,5,6,7,8,9]
print(multiply_even_number(numbers))