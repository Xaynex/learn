# Задача 1. Словарь квадратов чисел

# s = {}
# num = 5
# for i in range(1, 5 + 1):
#     s[i] = i ** 2
# print(s)

# Задача 2. Студент
#
# Результат:
# Имя - Илья
# Фамилия - Иванов
# Город - Москва
# Место учёбы - МГУ
# Оценки - [5, 4, 4, 4, 5]
#
# student_str=input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')

# rates=[]
# student_str = 'Илья Иванов Москва МГУ 5 4 4 4 5'
# student_info = student_str.split()
# student_info2=student_info[:]
# for i in student_info:
#     if i.isdigit():
#         rates.append(i)
#         student_info2.remove(i)
# rates=' '.join(rates)
# info = ['имя', 'фамилия', 'город', 'место учёбы', 'оценки']
# count = 0
# student_dict = {}
# for i in student_info2:
#     student_dict[info[count]] = i
#     count += 1
# student_dict[info[count]]=rates
# print(student_dict)
#
# for i in student_dict:
#     print(i, '-',student_dict[i], '\n',end='')

# Задача 3. Контакты
# Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему.
# И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
# Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов.
# Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
# Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.
#
# Пример:
# Текущие контакты на телефоне:
# <Пусто>
# Введите имя: Иван
# Введите номер телефона: 100200300
#
# Текущие контакты на телефоне:
# Иван  100200300
#
# Введите имя: Лена
# Введите номер телефона: 8005555522
#
# Текущие контакты на телефоне:
# Иван  100200300
# Лена  8005555522
#
# Введите имя: Иван
# Ошибка: такое имя уже существует.
# phones = {}
# while True:
#     print('Текущие контакты на телефоне: ')
#     for i in phones:
#         print(i, phones[i])
#     name = input('Введите имя: ')
#     if name in phones:
#         print('Ошибка: такое имя уже существует')
#         quit()
#     number = input('Введите номер телефона: ')
#     phones[name] = number