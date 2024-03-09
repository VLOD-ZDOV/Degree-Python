while True:
    numbers = int(input("Введи число: "))
    stepen = int(input("Введи степерь: "))
    if numbers == 0 and stepen == 0:
        print("Бесконечность не передел (неопределенность) ")
        print("")

    elif numbers == 1:
        print ("Будет всегда 1!!! ")
        print("")

    elif stepen == 0:
        print ("Будет всегда 1!!! ")
        print("")

    elif stepen < 0:
        a = 1 / numbers
        result = a ** abs(stepen)
        print("Результат: ",result)
        print('или')
        b = numbers ** abs(stepen)
        print("Результат: 1/{:.0f}".format(b))



    else:
        for i in range(1, stepen + 1):
            result = numbers ** i
            print(result, 'это', i, 'степень')
            
  
