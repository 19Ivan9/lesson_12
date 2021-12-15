class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, arr):
        return [i ** 2 for i in arr]

    def remove_positives(self, arr):
        return [i for i in arr if i < 0]

    def filter_leaps(self, arr):
        return [i for i in arr if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]
