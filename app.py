from aplication import ToDoList
app = ToDoList()
flag = True
while flag:
    print('Witaj w to do liście')
    print(30 * '-')
    app.print()
    print(30 * '-')
    print('Wybierz opcję co byś chciał teraz zrobić?')
    print('Dodaj zadanie -> "a"')
    print('Oznacz zadanie jako zrobione -> "m"')
    print('Usuń zadanie -> "d"')
    print('Wyłącz program -> "q"')
    key = input('Twoja opcja -> ')
    if key == 'a':
        app.add()
    elif key == 'd':
        app.delete()
    elif key == 'm':
        app.change_for_made()
    elif key == 'q':
        print(30 * '-')
        print('Do zobaczenia!')
        flag = False
    else:
        print('Nie rozumiem')



