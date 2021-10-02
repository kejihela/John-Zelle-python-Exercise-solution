def removeDuplicate(somelist):
    new_list = []
    for i in somelist:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

def main():
    list1 = [1,2,3,4,5,5,10,5,3,7,8,3,4,6,6,9,10]
    answer = removeDuplicate(list1)
    print(answer)
main()
