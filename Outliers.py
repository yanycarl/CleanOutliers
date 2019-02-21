
import csv
import numpy as np
import pandas as pd


class ReadFile:
    matrix = []

    @classmethod
    def openFile(cls):
        with open('train WITH OUTLIERS.csv', newline='\n') as csvFile:
            read = csv.reader(csvFile, delimiter=',', quotechar='|')
            i = 0
            for row in read:
                i += 1
                if i > 1:
                    temp = []
                    for item in row:
                        if item != 'NA':
                            temp.append(item)
                        else:
                            temp.append('-99999')
                    cls.matrix.append(temp)
        cls.matrix = np.transpose(cls.matrix)

    @classmethod
    def getData(cls):
        cls.openFile()
        cls.matrix = cls.matrix[[3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]]
        cls.matrix = cls.matrix.reshape(11, 421570)
        cls.matrix = cls.matrix.astype(float)


class CalculateThreshold:
    __Q1Array = []
    __Q3Array = []
    floorArray = []
    ceilArray = []

    @classmethod
    def calculateThreshold(cls, m):
        for row in m:
            temp_row = []
            for item in row:
                if item > -10000:
                    temp_row.append(item)
            cls.__Q1Array.append(np.percentile(temp_row, 25))
            cls.__Q3Array.append(np.percentile(temp_row, 75))

        for i in range(0, len(cls.__Q1Array)):
            cls.floorArray.append(cls.__Q1Array[i] - 1.5 * (cls.__Q3Array[i] - cls.__Q1Array[i]))
            cls.ceilArray.append(cls.__Q3Array[i] + 1.5 * (cls.__Q3Array[i] - cls.__Q1Array[i]))


class CleanData:
    dirtyIndex = set()
    cleanIndex = [0]

    @classmethod
    def findIndex(cls, c, f, m):
        for i in range(0, len(m)):
            for j in range(0, len(m[0])):
                if j not in cls.dirtyIndex and (c[i] < m[i, j] or f[i] > m[i, j] > -10000):
                    cls.dirtyIndex.add(j)
        print("The problem rows: ")
        print(str(cls.dirtyIndex))
        print("Deleted: "+str(cls.dirtyIndex.__len__()))

        for i in range(0, len(m[0])-1):
            if i not in cls.dirtyIndex:
                cls.cleanIndex.append(i+1)
        print("Remaining: "+str(len(cls.cleanIndex)))


class RecreateFile:
    @staticmethod
    def writeFile():
        df = pd.read_csv("train WITH OUTLIERS.csv")
        df = pd.DataFrame(df.iloc[list(CleanData.cleanIndex), :])
        df.to_csv("train WITHOUT outliers.csv")


if __name__ == "__main__":
    ReadFile.getData()
    CalculateThreshold.calculateThreshold(ReadFile.matrix)
    CleanData.findIndex(CalculateThreshold.ceilArray, CalculateThreshold.floorArray, ReadFile.matrix)
    RecreateFile.writeFile()
