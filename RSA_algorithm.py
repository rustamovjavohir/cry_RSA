import math
import random


class RSA:
    ma = 15

    def __init__(self, p, q, mine, protected) -> None:
        self.p = p
        self.q = q
        self.__mine = mine  # private
        self._protected = protected  # protected
        super().__init__()

    def get_mine(self):
        print(self.__mine)

    @staticmethod
    def gen_Prime_number(lower_value: 5, upper_value: 5000):
        prime_numbers = []

        for number in range(lower_value, upper_value + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    prime_numbers.append(number)
        return random.choice(prime_numbers)

    def find_N(self):
        return self.p * self.q

    def find_f(self, p: int, q: int):
        return (self.p - 1) * (self.q - 1)

    @staticmethod
    def check_prime_number(number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                return True

    @staticmethod
    def ekub(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        print(a)

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    @classmethod
    def clss(cls):
        print(f"class method {cls.ma}")

    def abb(self):
        print(f"object method {self.ma}")


def ekub(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)


def poland(n):
    x = y = 2
    i = 0
    while i <= n:
        i += 1
        x = (x ** 2 + 1) % n
        y = ((y ** 2 + 1) ** 2 + 1) % n
        e = math.gcd(int(math.fabs(y - x)), n)
        if e != 1 & e != n:
            return e, i


if __name__ == '__main__':
    rsa_object = RSA(7, 11, 5, 'Pro')
    # print(rsa_object.gen_Prime_number(lower_value=10, upper_value=100))
    print(poland(3901))
    # RSA.clss()
    # rsa_object.clss()
    # rsa_object.ma = 5
    # rsa_object.abb()
    # rsa_object.get_mine()
    # print(rsa_object._RSA__mine)  # private
    # print(rsa_object._protected)  # protected

