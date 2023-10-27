# используется для сортировки
from operator import itemgetter


class Library:
    """Библиотека"""
    def __init__(self, id, title, rows_count, pr_id):
        self.id = id
        self.title = title
        self.rows_count = rows_count
        self.pr_id = pr_id


class ProgrammingLanguage:
    """Язык программирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibProg:
    """
    'Библиотеки языка программирования' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, pr_id, lib_id):
        self.pr_id = pr_id
        self.lib_id = lib_id


# Языки программирования
progs = [
    ProgrammingLanguage(1, 'Python'),
    ProgrammingLanguage(2, 'C++'),
    ProgrammingLanguage(3, 'C#'),
    ProgrammingLanguage(4, 'Java'),
]


# Библиотеки
libs = [
    Library(1, 'CV2', 4500, 1),
    Library(2, 'Numpy', 2000, 1),
    Library(3, 'Math', 1500, 2),
    Library(4, 'Libpq', 6000, 2),
    Library(5, 'NUnit', 4000, 3),
    Library(6, 'Moq', 3000, 3),
    Library(7, 'JHipster', 7000, 4),
    Library(8, 'Maven', 4500, 4),
]


libs_progs = [
    LibProg(1,1),
    LibProg(1,2),
    LibProg(2,3),
    LibProg(2,4),
    LibProg(3,5),
    LibProg(3,6),
    LibProg(4,7),
    LibProg(4,8),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(l.title, l.rows_count, p.name) 
                   for p in progs 
                   for l in libs 
                   if l.pr_id == p.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(p.name, lp.pr_id, lp.lib_id) 
                         for p in progs 
                         for lp in libs_progs 
                         if p.id == lp.pr_id]
    
    many_to_many = [(l.title, l.rows_count, prog_name) 
                    for prog_name, pr_id, lib_id in many_to_many_temp 
                    for l in libs 
                    if l.id == lib_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key = itemgetter(0))
    print(res_11)
    
    print('\nЗадание Б2')
    res_12_unsorted = []
    # Перебираем все языки программирования
    for p in progs:
        # Список библиотек языка программирования
        p_libs = list(filter(lambda i: i[2] == p.name, one_to_many))
        # Если в языке есть библиотеки        
        if len(p_libs) > 0:
            # Строки библиотек данного языка
            p_rows = [rows_count for _,rows_count,_ in p_libs]
            # Суммарное количество строк всех библиотек данного языка
            p_rows_sum = sum(p_rows)
            res_12_unsorted.append((p.name, p_rows_sum))


    # Сортировка по суммарном количестве строк
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse = True)
    print(res_12)


    print('\nЗадание Б3')
    res_13 = {}
    # Перебираем все библиотеки
    for l in libs:
        if ('m' in l.title) or ('M' in l.title):
            # Список библиотек языка программирования
            l_progs = list(filter(lambda i: i[0] == l.title, many_to_many))
            # Только название языка
            l_progs_titles = [x for _,_,x in l_progs]
            # Добавляем результат в словарь
            # ключ - библиотека, значение - язык программирования
            res_13[l.title] = l_progs_titles

    print(res_13)


if __name__ == '__main__':
    main()

