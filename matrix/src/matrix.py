class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        returnRow = []
        listOfString = self.matrix_string.split()
        listInt = []
        for string in listOfString:
            listInt.append(int(string))
        returnRow.append(listInt[0])
        return returnRow

    def column(self, index):
        pass
