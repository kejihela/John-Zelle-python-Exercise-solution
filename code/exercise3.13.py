def sum_numbers():
    print("This will print the sum of series of numbers")
    n = int(input("How many numbers did you want to sum? "))
    accumulator = 0
    for i in range(n):
        x = int(input("please, input the number "))
        accumulator = accumulator + x
    print("The sum of the series of number is", accumulator)
sum_numbers()
