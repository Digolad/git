
#! Программа - да пошел ты нахер
 
print("Команды которые я знаю: \n 1. pidor - вывод трех последних команд \n 2. exit - выход")
last_words=["-","-","-"]
while True:
    data = input("Введите что нибудь: ")
    if data.lower() == "exit":
        break  # выход из цикла
    if data.lower()=="pidor":
        for i in last_words:
            print(i)
    else:
        print(data)
        last_words.append(data)
        last_words.pop(0)
   
print("Работа завершена")

