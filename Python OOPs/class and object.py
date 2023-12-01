class car:
    speed=0     #class global variable, if it will change it does affect all the objects  
    def __init__(self,brand,model,colour,price):
        self.brand=brand
        self.model=model
        self.colour=colour
        self.price=price

    def topspeed(self):
        if(self.model=="R8"):
            print("Top speed of R8 is {} kms/h".format(280))
        elif(self.model=="veyron"):
            print("Top speed of veyron is {} kms/h".format(400))

    def accelerate(self):
        self.speed+=20
        print("speed :",self.speed)

    def curr_speed(self):
        print("current speed :",self.speed)
        
    def stop(self):
        self.speed=0

import sys
car1=car("Bucatti","veyron","blue",2000000)
print(car1.model)
car2=car("Audi","R8","black",1000000)
print(car1.price)
car1.topspeed()

count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")


def doge_count(str):
    count = 0
    i=0
    while i<(len(str)-3):
        if (str[i:(i+4)])=="doge":
            count+=1
            i+=3
        if (str[i]=='g'):
            if (str[i+1:i+4])=="oge":
                count+=1
                i+=3
            elif(str[1,i+4])=="dgge":
                count+=1
                i+=2
            elif(str[i-3:i])=="dog":
                count+=1
                i+=1
        i+=1
        
    return count
print(doge_count("dogegogenhjdoge"))
