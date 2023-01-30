import io

journal = {}
path = ''
subject = ''

def classes(classes: str):
    global path
    path = 'classes/' + 'class' + classes + '.txt'


def list_lesson() -> list:
    with io.open(path, 'r', encoding='UTF-8') as fail:
        data = fail.readlines()
    lst = []
    for lain in data:
        lst.append(lain.split(': ')[0])
    return lst


def open(lesson: str):
    global subject
    with io.open(path, 'r', encoding='UTF-8') as fail:
        data = fail.readlines()
    while True:
        for lain in data:
            if lain.split(': ')[0].startswith(lesson[:2]):
                subject = lain.split(': ')[0]
                for lst in lain.split(': ')[1].strip().split('; '):
                    journal[lst.split(':')[0]] = ','.join(lst.split(':')[1].split(','))
                return journal
        else:
            lesson = input('Уточните предмет: ').lower()



def student(student: str):
    global journal
    ansfer = ''
    for key, value in journal.items():
        if key.startswith(student[:2]):
            if 'да' in input(f'{key} Этот ученик да\нет: '):
                ansfer += journal[key]
                ansfer += f',{input("Оценка: ")}'
                journal[key] = ansfer
                break
    else:
        print('Ученик не найден повторите\n')


def save_file(save):
    if save == 'да':
        new_file = []
        with io.open(path, 'r', encoding='UTF-8')as fail:
            data = fail.readlines()
        for lain in data:
            if lain.split(': ')[0] != subject:
                new_file.append(lain.strip())
        item = []
        for key, value in journal.items():
            item.append(key + ':' + value)
        item = subject + ': ' + '; '.join(item)
        new_file.append(item)
        with io.open(path, 'w', encoding='UTF-8')as data:
            data.write('\n'.join(new_file))
        print('Изминения сохранены')
    else:
        print("в журнал изменения не внесены")



