class Counter:
    """ This is a Counter that can help you to increment 1 or decrement 1 ,etc!"""
    instance = 0

    def __init__(self):
        self._result = 0
        Counter.instance += 1
        self.rest()

    def rest(self):
        self._result = 0

    def increment(self, step=1):
        self._result += step

    def decrement(self, step=1):
        self._result -= step

    def get_result(self):
        return self._result

    def __str__(self):
        return str(self._result)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._result == other._result


if __name__ == '__main__':
    c1 = Counter()
    print(c1.instance)
    print(c1.get_result())
    c1.increment()
    print(c1.instance)
    print(c1.get_result())
    c1.increment()
    print(c1.instance)
    print(c1.get_result())
    # c2 = Counter : means is give Counter class to variable c2
    c2 = Counter()
    print(c2.instance)
    print(c2.get_result())
    print(c1 == 2)
    print(c1 == c2)
    c2.increment()
    c2.increment()
    print(c1 == c2)
    c2 = c1
    c2.increment()
    print(c1.get_result())
    print(c2.get_result())
    print(c1 == c2)
