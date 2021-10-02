def inner_prod(x,y):
    n = 0
    list1 = []
    for i in x:
        for a in y:
            value = i * y[n]
            list1.append(value)
            n+=1
            break
    return list1

def main():
    n = [1,2,3,4,5,6,7,8,9]
    b = [1,2,3,4,5,6,7,8,9]
    answer = inner_prod(n,b)
    print(answer)
main()
