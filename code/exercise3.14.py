def average():
    print("This will print the average of series of numbers")
    n = int(input("How many numbers did you want to average? "))
    accumulator = 0
    for i in range(n):
        x = int(input("please, input the number "))
        accumulator = accumulator + x
    average = float(accumulator/n)
    print("The average of the series of number is", average)
average()
