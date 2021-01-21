from exercise import Exercise


class ToDoList:
    def __init__(self):
        self.zadania = []

    def print(self):
        print(30 * '-')
        if len(self.zadania) > 0:
            for index, exercise in enumerate(self.zadania):
                print(f'[{index}] --> {exercise}')
        else:
            print('Twoja lista jest pusta.')

    def print_for_file(self):
        if len(self.zadania) > 0:
            for index, exercise in enumerate(self.zadania):
                return f'[{index}] --> {exercise}'
        else:
            return f'Twoja lista jest pusta.'

    def add(self):
        quest = input('Podaj swoje zadanie do zrobienia ')
        zadanie = Exercise(quest)
        self.zadania.append(zadanie)
        self.print()

    def get_index(self):
        flag = True
        while flag:
            index = int(input('Podaj indeks zadania '))
            if len(self.zadania) > index >= 0:
                flag = False
                return index
            else:
                print('Coś poszło nie tak spróbuj ponownie')

    def delete(self):
        index = self.get_index()
        del self.zadania[index]
        self.print()

    def change_for_made(self):
        index = self.get_index()
        self.zadania[index].change_for_made()
        self.print()
