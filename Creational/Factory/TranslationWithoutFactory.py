class FrenchLocalizer:
    '''It simply returns french version'''
    def __init__(self):
        self.translations = {
            'car':'voiture',
            "cycle":"cyclette"
        }

    def localize(self, msg):
        '''changes the msg using translations'''
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    '''It simply returns spanish version'''
    def __init__(self):
        self.translations = {
            'car':'coche',
            "cycle":"ciclo"
        }

    def localize(self, msg):
        '''changes the msg using translations'''
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    '''Simply returns same message'''
    def localize(self, msg):
        return msg

if __name__ == "__main__":
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()

    message = ['car', 'bike', 'cycle']
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))