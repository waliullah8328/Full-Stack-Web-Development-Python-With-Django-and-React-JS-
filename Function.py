# create a function
def func():
    print("Inner Area")

print("Out Area")

func()

def sum1():
    print(30+20)

sum1()

def sum2():
    return 40+10
v = sum2()
print(v)

def sum3(num1,num2):
    return num1 +num2
print(sum3(10,20))
print(sum3(10,21.8))
print(sum3("Wali","Ullah"))

def manyvalueprint(*num):
    sum=0
    for i in num:
        sum = sum+i
    print(sum)
manyvalueprint(10,20,30,40,50)
# nested function
def nested_function(a,b,c):
    a = a + 10
    b = b + 20
    def another_function(a,b):
        result = a+b
        def other_function(result,c):
            return result * c
        return other_function(result,c)
    return another_function(a,b)

print(nested_function(100,20,300))