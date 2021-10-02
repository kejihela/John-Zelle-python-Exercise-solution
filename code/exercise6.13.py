def toNumbers(strList):
    numberList = []
    for i in strList:
        i = int(i)
        numberList.append(i)
    return numberList

def main():
    print("this program is to print the square of each entry")
    value_list = input("please type your numbers ")
    string = value_list.split()
    answer = toNumbers(string)
    print(answer)
main()
