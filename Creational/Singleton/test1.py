class Singleton:
    __instance = None
    def __init__(self):
        assert 

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance