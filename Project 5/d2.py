class Time:
    # DO NOT CHANGE THIS METHOD
    def normalize(self):

        s = self.__seconds
        m = self.__minutes
        h = self.__hours

        while (s < 0):
            s += 60
            m -= 1

        while (m < 0):
            m += 60
            h -= 1

        while (h < 0):
            h = h + 24

        self.__seconds = s % 60
        self.__minutes = (m + s // 60) % 60
        self.__hours = (h + m // 60 + s // 3600) % 24

class math(Time):
    def __add__(self, other):

    def __sub__(self, other):

    def __gt__(self, other):

    def __lt__(self, other):

# DO NOT CHANGE THIS FUNCTION
def create_time():
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))
    time = Time(hours, minutes, seconds)

    return time


# DO NOT CHANGE THIS FUNCTION
def main():
    t1 = Time()
    t1 = create_time()
    t2 = create_time()
    t3 = create_time()

    print("Time1:", t1)
    print("Time2:", t2)
    print("Time3:", t3)

    t4 = t1 + t2
    print("Time4:", t4)

    t1 = t3 - t4
    print("Time1:", t1)

    if t1 < t3:
        print("Time1 < Time3")
    else:
        print("Time3 >= Time1")

    t5 = t2 + Time(0, 0, 1)
    if (t5 < t2):
        print("Time5 < Time2")
    else:
        print("Time5 >= Time2")

    print("Almost midnight: ", Time(0, 0, 0) - Time(0, 0, 1))


main()