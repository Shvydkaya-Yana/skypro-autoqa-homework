weekDays=["Понедельник",
          "Вторник",
          "Среда",
          "Четверг",
          "Пятница",
          "Суббота",
          "Воскресенье"]

length=len(weekDays) # длина строки
print(length)

monday = weekDays[0]
print(monday)

thursday = weekDays[3]
print(thursday)
print(weekDays[-1])

def greet(name):
    print("Привет, " +name)
greet("Alex")

def sumNumbers(a,b):
    print(a)
    print(b)
    sum=a+b
    return sum

x = sumNumbers(5,6)
print(x)

print(x+5)

def multiply(x,y):
    return x*y
print(multiply(3,5))

def sub(x,y):
    return x-y
print(sub(30,5))

def div(x,y):
    return x/y
print(div(10,5))

globalVar = 1

def printGlobal():
    print(globalVar)

def printLocal():
    localVar = 2
    print(localVar)
printLocal()
printGlobal()
