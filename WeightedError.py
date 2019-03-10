

class WeightedError:

    class DimensionException(Exception):
        pass

    def __init__(self):
        self.__holidays = set()
        self.__dateString = "/02/2010"
        date = 12
        for i in range(0, 6, 1):
            if i == 0 or i == 1 or i == 2:
                self.__holidays.add(str(date - i) + self.__dateString)
            else:
                self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/09/2010"
        date = 10
        for i in range(0, 6, 1):
            if i == 0:
                self.__holidays.add(str(date - i) + self.__dateString)
            else:
                self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/11/2010"
        date = 26
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)
        self.__dateString = "/02/2011"
        date = 11
        for i in range(0, 6, 1):
            if i == 0 or i == 1:
                self.__holidays.add(str(date - i) + self.__dateString)
            else:
                self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/09/2011"
        date = 9
        for i in range(0, 6, 1):
            self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/12/2011"
        date = 30
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)
        self.__dateString = "/02/2012"
        date = 10
        for i in range(0, 6, 1):
            if i == 0:
                self.__holidays.add(str(date - i) + self.__dateString)
            else:
                self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/09/2012"
        date = 7
        for i in range(0, 6, 1):
            self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/11/2012"
        date = 23
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)
        self.__dateString = "/12/2012"
        date = 28
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)
        self.__dateString = "/02/2013"
        date = 8
        for i in range(0, 6, 1):
            self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/09/2013"
        date = 6
        for i in range(0, 6, 1):
            self.__holidays.add("0" + str(date - i) + self.__dateString)
        self.__dateString = "/11/2013"
        date = 29
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)
        self.__dateString = "/12/2013"
        date = 27
        for i in range(0, 6, 1):
            self.__holidays.add(str(date - i) + self.__dateString)

    def calculateError(self, date, y1, y2):
        length = len(y1)
        length2 = len(y2)
        length3 = len(date)

        if length == 0 or length2 == 0 or length3 == 0:
            raise SyntaxError("Can not be 0")

        if length != length2 or length != length3:
            raise self.DimensionException

        totalW = 0
        totalE = 0
        for i in range(0, length):
            if date[i] in self.__holidays:
                totalW += 5
                totalE += 5 * abs(y1[i] - y2[i])
            else:
                totalW += 1
                totalE += 5 * abs(y1[i] - y2[i])
        return totalE/totalW
