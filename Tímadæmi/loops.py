class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return str(self.vec)

    def __len__(self):
        return len(self.vec)

    def scale(self, number):
        """for index in range(len(self.vec)):
            self.vec[index] = self.vec[index] * number"""
        for index, value in enumerate(self.vec):
            self.vec[index] = value * number

    def add(self, vec_b):
        for index, value in enumerate(vec_b):
            self.vec[index] += value



def main():
    vec1 = Vector([1, 2, 3])
    print(vec1)
    vec1.scale(3) #[3, 6, 9]
    print(vec1)

    vec1.add([1,2,3])
    print(vec1)

    print(len(vec1))

main()