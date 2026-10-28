# з.1. Вариант6
print("Вводите числа. Чтобы закончить, просто нажмите Enter.")

numbers = []

while True:
    s = input("Введите число: ")
    if s == "":  # если строка пустая - выходим
        break
    else:
        numbers.append(float(s))  # float, чтобы можно было вводить дроби

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
            
    print("\nЧисла НИЖЕ среднего:")
    for x in below:
        print(x)
        
    print("\nЧисла РАВНЫЕ среднему:")
    for x in equal:
        print(x)
        
    print("\nЧисла ВЫШЕ среднего:")
    for x in above:
        print(x)
