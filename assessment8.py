class MyList:
    def __init__(self, data):
        self.data = data

    def get_item(self, index):
        return self.data[index]
    def get_slice(self, start, end):
        
        return self.data[start:end]
    
my_list = MyList([1,2,3,4,5])
print(my_list.get_slice(1,2))

