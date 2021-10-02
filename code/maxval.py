def main():
    print("This program will print the highest number")
    maxval = int(input("Please input your value"))
    n = int(input("Please input the number of values you have got "))
    for i in range(n-1):
        x = int(input("Please input your value"))
        if x > maxval:
            maxval = x
    print(maxval)

main()
                 
