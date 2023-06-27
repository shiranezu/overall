def largest_divisible(n, lst):
    my_list=[]
    for i in lst:
        if i % n == 0:
            my_list.append(i)
    if len(my_list) == 0:
        print(None)  

    print(max(my_list))               
   

largest_divisible(3,[20,22,6,8,10])