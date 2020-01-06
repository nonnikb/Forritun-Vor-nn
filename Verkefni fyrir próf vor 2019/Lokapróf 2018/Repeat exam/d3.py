import math


class VectorTest:
    ''' This is a class for testing the Vector class '''

    def __init__(self, list1, list2):
        self.__v1 = Vector(list1)
        self.__v2 = Vector(list2)

    def test_print(self):
        print("v1 and v2: {} {}".format(self.__v1, self.__v2))

    def test_length(self):
        print("Length of v1 and v2: {:.2f} {:.2f}".format(self.__v1.length(), self.__v2.length()))

    def test_addition(self):
        print("v1 + v2: {}".format(self.__v1 + self.__v2))

    def test_scaling(self, scalar):
        self.__v1.scaling(scalar)
        self.__v2.scaling(scalar)
        print("Scaling v1 and v2 by {}: {} {}".format(scalar, self.__v1, self.__v2))


class Vector:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return "{}".format(self.list)

    def length(self):
        ans = 0
        for x in self.list:
            ans += (x**2)
        return math.sqrt(ans)

    def __add__(self, other):
        my_list = []
        for x in range(len(self.list)):
            my_list.append(self.list[x] + other.list[x])
        return my_list

    def scaling(self, scalar):
        s_list = []
        for x in self.list:
            s_list.append(x*scalar)
        self.list = s_list

    





# Your implementation


# Main program starts here
vtest = VectorTest([2, 4], [3, -4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(2)

vtest = VectorTest([3, 5, -2], [2, -3, 4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(3)