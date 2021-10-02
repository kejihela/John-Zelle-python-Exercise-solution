def sumN(n):
    sum_n = (n * (n+1))/2
    return sum_n
def sumCube(n):
    sum_cube = ((n * (n+1))/2)**2
    return sum_cube
def main():
    print("this program will print sum of n nstursl number and sum of cube")
    n = int(input("please input the number"))
    sum_number = sumN(n)
    print(sum_number)
    cube_number = sumCube(n)
    print(cube_number)
main()
