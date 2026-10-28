# з.1. Вариант6
print("Вводите числа. Чтобы закончить, просто нажмите Enter.")

numbers = []

while True:
    s = input("Введите число: ")
    if s == "":  
        break
    else:
        numbers.append(float(s))  

if len(numbers) == 0:
    print("Вы не ввели ни одного числа.")
else:
    average = sum(numbers) / len(numbers)
    print("\nСреднее значение:", average)
    
    below = []
    equal = []
    above = []
    
    for x in numbers:
        if x < average:
            below.append(x)
        elif x == average:
            equal.append(x)
        else:
            above.append(x)
            
    print("\nЧисла ниже среднего:")
    for x in below:
        print(x)
        
    print("\nЧисла равные среднему:")
    for x in equal:
        print(x)
        
    print("\nЧисла выше среднего:")
    for x in above:
        print(x)
