class Course:
    def __init__(self):
        # Steps to build object
        self.fee_()
        self.available_batches()

    def fee_(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError


class DSA(Course):
    def fee_(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"

class STL(Course):
    def fee_(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"

class SDE(Course):
    def fee_(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"
