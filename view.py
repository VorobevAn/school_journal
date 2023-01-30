import controller

def journal():
    classes = input('Какой класс открыть?: ').lower()
    return classes

def school_items(classes:list) ->str:
    for i, items in enumerate(classes):
        print(i+1, items)
    return input('Выбирите предмет: ')

def print_jornal(journal):
    for key, value in journal.items():
        print(key, ':', value)

def ansfer_stydent():
    return input('для завершения набрать стоп, кто отвечает?: ').title()


def save_jornal():
    return input('Сохранить изменения? да/нет: ').lower()



