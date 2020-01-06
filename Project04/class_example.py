class Vector:
    def __init__(self, vec=[]):
        self.vec = vec

    def __add__(self, other):
        result = Vector()
        for index, _ in enumerate(self.vec):
            result.add(self.vec[index] + other.vec[index])
        return result

    def __sub__(self, other):
        result = []
        for index, _ in enumerate(self.vec):
            result.append(self.vec[index] - other.vec[index])
        return Vector(result)

    def __str__(self):
        result = ""
        for x in self.vec:
            result += str(x) + " "
        return result

    def add(self, new_value):
        self.vec.append(new_value)

    def __eq__(self, other):
        for index, value in enumerate(self.vec):
            if self.vec[index] != other.vec[index]:
                return False
        return True

    def __len__(self):
        return len(self.vec)


    def __gt__(self, other):
        return sum(self.vec) > sum(other.vec)


def main():
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([1, 2, 3])
    if vec1 == vec2:
        print("Everything is awesome!")
    print(vec1)
    print(len(vec1))
    vec3 = vec1 + vec2
    #vec4 = vec2 - vec1
    print(vec3)
    #print(vec4)





main()
