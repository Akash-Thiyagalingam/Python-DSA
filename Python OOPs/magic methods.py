class Magic_methods:
    def __init__(self, value):
        self.value = value
        # This function called when the object is created 
    def __add__(self,other):               
        return other.value * self.value
        #This function is called using the + with two objectsn as oparents
        #Similarly can use __sub__,__mul__ etc
    def __del__(self):
        print("__del__ method is called")
        #We can call this function using 'del' keyword and also delete the object
    def __repr__(self):
        return f"value : {self.value}"
        #It is used for representing the object when the object is only called 
        #Ex: val1 = Magic_methods(2)
        #print(val)  __repr__ method is called. Instead of this we can use __str__
    def __len__(self):
        return 1
        #This method is called when the len(obj) is called.
    def __call__(self):
        return f"Object as a function"
        #This method is called when object is called as a function Ex: val1()
val1 = Magic_methods(2)
val2 = Magic_methods(10)
print(val1+val2)
print(val1)

