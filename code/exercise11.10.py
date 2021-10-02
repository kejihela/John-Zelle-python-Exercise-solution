def prime_numbers(list1):
    list2 = []
    while len(list1) != 0: 
        for i in list1:
            list2.append(i)
            list1.remove(i)
            break
        for b in list1:
            if b%i == 0:
                list1.remove(b)
            else:
                continue
    return list2

def main():
    n = int(input("whats is the range of your numbers "))
    list1 = []
    for i in range(n):
        list1.append(i+1)
    ans = prime_numbers(list1)
    print(ans)
    
main()
