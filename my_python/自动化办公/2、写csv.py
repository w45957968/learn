import csv


def writeCsv(path,data):
    with open(path,"w",newline='') as f:   #newline = ""   用来解决写文件出现空格的情况
        writer = csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)

path = r"C:\Users\Administrator\Desktop\测试.csv"
data = [[1,2,3,4],[5,6,7,8,9],["a","v","as"],["s","sv","f"]]
write = writeCsv(path,data)
if __name__ == '__main__':
    write()