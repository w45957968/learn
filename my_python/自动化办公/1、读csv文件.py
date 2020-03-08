import csv


def readCsv(path):
    infoList = []
    with open(path,"r") as f:
        fileINfo = csv.reader(f)
        print(fileINfo)
        for row in fileINfo:
            infoList.append(row)
    return infoList

path = r"C:\Users\Administrator\Desktop\洛阳户籍.csv"
if __name__ == '__main__':
    read = readCsv(path)