from aplication import ToDoList

app = ToDoList()
flag = True
app.print()
while flag:
    print('Witaj w to do liście')
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
        f = open("todolist.txt", "w")
        f.write(app.print_for_file())
        f.close()
    else:
        print('Nie rozumiem')
