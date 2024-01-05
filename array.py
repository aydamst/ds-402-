class Array:
    def __init__(self):
        self.data = []

    def insert(self, obj, index):
        self.data.insert(index, obj)

    def delete(self, index):
        return self.data.pop(index)

    def find(self, obj):
        if obj in self.data:
            return self.data.index(obj)
        else:
             return -1

#my_array = Array()  # Create an object of the Array class
#for i in range(0,3):
#    my_array.insert(int(input('index morede nazar : ')), int(input("adad morede nazar : ")))  # Insert element 10 at position 0


#print(my_array.data)  

#index = my_array.find(20)  
#print("Index of 20:", index)  

#index = my_array.find(30)
#print("Index of 30:", index)

#deleted_element = my_array.delete(0) 
#print("Deleted element:", deleted_element)  

#print(my_array.data)  