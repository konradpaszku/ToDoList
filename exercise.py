class Exercise:
    def __init__(self, zadanie: str):
        self.zadanie = zadanie
        self.ismade = False

    def made_or_not(self):
        if self.ismade:
            return self.zadanie + '  V'
        else:
            return self.zadanie + '  X'

    def change_for_made(self):
        self.ismade = True

    def __str__(self):
        return self.made_or_not()
