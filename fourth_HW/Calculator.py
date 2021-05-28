class Cacultor:

    def __init__(self,name):
        self.name=name
        self.result=0
    def add(self,num1,num2):
        self.result=num1+num2
        return self.result

cacultor1 = Cacultor("박채원")
print(cacultor1.name)
print(cacultor1.add(3,5))

class Cacultor:

    def __init__(self,name,age):
        self.name=name
        self.result=0
        self.age=age
    
    def add(self,num1):
        self.result+=num1
        return self.result
    def minus(self,num1):
        self.result-=num1
        return self.result
    def multiple(self,num1):
        self.result*=num1
        return self.result
    def divide(self,num1):
        if num1 ==0:
            return self.result
            
        self.result/=num1
        return self.result
    
    
cacultor2=Cacultor("박채원","22")
print(cacultor2)
print(cacultor2.age)
print(cacultor2.add(7))
print(cacultor2.add(5))
print(cacultor2.divide(0))
