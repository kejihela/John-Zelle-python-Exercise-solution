def Bsearch(x, lst):
    low = 0
    high = len(lst)-1
    
    while low <= high:
        mid = (high + low)//2
        item = lst[mid]
        if x == item:
            return mid
        elif x > item:
            low = mid + 1

        else:
            high = mid-1

    return -1



def main():
    lst = [1,2,3,4,5,6,7,8,9]
    answer = Bsearch(7,lst)
    print(answer)

main()
