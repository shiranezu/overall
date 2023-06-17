def count_positive_negative(numbers):
     positive= 0
     negative= 0
     for num in numbers:
          if num> 0:
               positive += 1
          else:
               negative += 1
     return (positive, negative) 

count_positive_negative = (-1,-2,-3,-4,1,2,3,4,5,6,7)
                         