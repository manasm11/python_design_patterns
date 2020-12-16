class DSA:
    '''Data Structures & Algorithm Info'''

    def price(self):
        return 11000

    def __str__(self):
        return 'DSA'


class STL:
    '''Standard Template Library Info'''

    def price(self):
        return 8000

    def __str__(self):
        return "STL"


class SDE:
    '''Software Development Engineer'''

    def price(self):
        return 15000

    def __str__(self):
        return 'SDE'


if __name__ == "__main__":
    sde = SDE()    # object for SDE class
    dsa = DSA()    # object for DSA class
    stl = STL()    # object for STL class

    print(f'Name of the course is {sde} and its price is {sde.price()}')
    print(f'Name of the course is {dsa} and its price is {dsa.price()}')
    print(f'Name of the course is {stl} and its price is {stl.price()}')
