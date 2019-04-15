class Node:
    # определяем список
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next     
        
class LinkedList:
    # конструктор , указывыаем явным образом
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    # вывод списка
    def __str__(self):
        if self.first == None:
            # сообщение если список пуст
            all_list ="This is list empty!"
            return all_list
        if self.first != None:
            # если ссылка на первую ноду не пустая
            curr = self.first
            # то запоминаем в переменую ссылку на первую ноду
            #(переменная стала первой нодой)
            all_list = 'LinkedList ['+" " +str(curr.value) +" "
            # эта переменная для красивого вывода
            while curr.next != None:
                # цыкл работает пока указатель на след. ноду не будет пустой
                curr = curr.next
                # переменная становится следующей нодой +1
                all_list += str(curr.value)+ " "
                # добавлем в общую переменную значение текущей ноды
                # переводим в строку и добавляем в конце пробел
            return all_list + ']'
            # возвращаем методу общую переменную с всеми данными списка и закрываем скобку
    

    def clear(self):
        # метод для очистки списка
        self.__init__()

    def SortedInsert(self,x):
        if self.first == None:
          self.first = Node(x,self.last)
          return
        # если первой ноды нет, то определяем список со значением Х
        # и линкой на последную запсь пусто ;]
        if self.first.value > x:
          self.first = Node(x,self.first)
          return
          # если значение первой ноды больше введенного , то
          # ссылка на первую ноду падает на Х и нода Х будет иметь ссылку "next" на бывшую первую ноду
        curr = self.first
        # переменная currva становится следующей нодой +1
        while curr != None:
            # цыкл работает пока указатель на след. ноду не будет пустой
            if curr.value > x:
                # если значение курва значение болье введенного Х
                old.next = Node(x,curr)
                return
              # определяем переменную (похожа на странную переменную)
              # значение введенное и ссылка на наноду курва, (то есть становится перед курвой) как я нагло становлюсь в очередь
              # вернули ифу нихуя ибо смысл?))
            old = curr
            curr = curr.next
            # сложная итерация с двумя переменными типа:
            # old становится на место курвы,
            # курва стала перед old
        self.last = old.next = Node(x,None)
        # ссылка на последнуюю ноду сохранилось в old.next и нода определилась
    
    def Delele(self,i):
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        
            
    
L = LinkedList()
while True:
    print("Select: \n a - add \n d - delete \n v - vivod \n e - exit \n cl - clear")
    sl=input()
    if sl == "e":
        break #exit
    if sl == "a":
        print("enter date only int")
        sl1=input()
        L.SortedInsert(int(sl1))
    if sl == "v":
        print(L)
    if sl == "cl":
        L.clear()
    # и тут я со всей силы поплыл 
    if sl == "d":
        print("Enter number node for delete it")
        el = int(input())
        print (type(el))
        L.Delete(self,el)
    
    
    


       
