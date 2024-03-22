people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda x: print(f'Привет, {x}!'), people)
# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
say_to_all(lambda x: print(f'До завтра, {x}!'), people)