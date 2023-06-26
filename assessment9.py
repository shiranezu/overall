# create a class that takes a dictionary that has three functions to get the suum of
#  people tht submitted. grade everyone, 70 and above = A


class Grade:
    def __init__(self, dict):
        self.dict = dict
    def counter(self):
        count= 0
        for i in self.dict:
            count+= 1
            return count

    def assign_scores(self):
        new_dict= {}
        for i in new_dict:
            if new_dict[i]>= 70:
                print('A')
            elif new_dict[i]<= 69:
                print('B')
            elif new_dict[i]<= 59:
                print('C')
            elif new_dict[i]<= 49:
                print('f')
        return new_dict
assign= Grade({'john':67, 'mark':76, 'will':88})
print(assign.assign_scores())

            
