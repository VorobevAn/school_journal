
import view
import model

def start():
    model.classes(view.journal())
    lesson = view.school_items(model.list_lesson())
    journal = model.open(lesson)
    while True:
        view.print_jornal(journal)
        stydent = view.ansfer_stydent()
        if stydent == 'Стоп':
            break
        model.student(stydent)
    model.save_file(view.save_jornal())


