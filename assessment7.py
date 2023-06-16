def count_positive_negative(numbers):
     positive= 0
     negative= 0
     for num in numbers:
          if num> 0:
               pos_count += 1
          elif num<0:
               neg_count += 1
     return(pos_count, neg_count)

count_positive_negative =(1,2,3,4,5,6,7,8,9,10)
