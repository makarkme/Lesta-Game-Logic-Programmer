class Queue1:  # Реализация №1 - очередь (fifo) на массиве
    def __init__(self):
        self.array = list()

    def add_element(self, element):  # добавление нового элемента в очередь
        self.array.append(element)

    def is_empty(self):  # проверка очереди на пустоту
        if not self.array:
            return True
        else:
            return False

    def get_element(self):  # получение элемента
        if not self.is_empty():
            return self.array[0]

    def dequeue(self):  # получение элемента с последующим удалением из очереди
        if not self.is_empty():
            return self.array.pop(0)

    def get_size(self):  # получение длины очереди
        return len(self.array)


# queue = Queue1()
# queue.add_element(12)
# queue.add_element(-4)
# queue.add_element(356)
# print(queue.dequeue())

class Node:  # одна ячейка списка, хранящая значение и указатель на следующую ячейку
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue2:
    def __init__(self):
        self.head = None  # указатель на первый элемент очереди
        self.tail = None  # указатель на последний элемент очереди
        self.size = 0

    def add_element(self, element):  # добавление нового элемента в очередь
        new_node = Node(element)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def is_empty(self):  # проверка очереди на пустоту
        if not self.head:
            return True
        else:
            return False

    def get_element(self):  # получение элемента
        if not self.is_empty():
            return self.head.value

    def dequeue(self):  # получение элемента с последующим удалением из очереди
        if not self.is_empty():
            data = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return data

    def get_size(self):  # получение длины очереди
        return self.size


# queue = Queue2()
# queue.add_element(12)
# queue.add_element(-4)
# queue.add_element(356)
# print(queue.dequeue())

# Сравнение подходов (по асимптотике):
# ДОБАВЛЕНИЕ:
# На массиве: за O(1), если есть свободное место, но всё зависит от того, что мы делаем при переполнении.
# При переполнении можно создать новый массив в 2 раза больше предыдущего и перенести все элементы из старого в новый + добавить элемент - это за O(n).
# Ещё можно перезаписывать новым элементом самый старый элемент - это за O(1). Ну и ещё можно просто ограничить запись при переполнении.
# На списке: за O(n) - просто добавить новый указатель на элемент.
# УДАЛЕНИЕ:
# На массиве: за O(n) - придется создавать новый массив, копировать всё из старого, но без удаляемого элемента.
# На списке: за O(n) - просто перепривязываем указатели на нужные Node, так, чтоб никто не ссылался на удаляемый элемент.
# ИТОГ: реализация на списке выигрывает в скорости и притом сильно, но и требует она в 2 раза больше памяти
# (т.к. на каждый элемент ещё приходится указатель, который тоже хранится в памяти).
# В свою очередь, реализация на массиве выигрывает в кол-ве занимаемой памяти, но соответственно проигрывает в скорости.
