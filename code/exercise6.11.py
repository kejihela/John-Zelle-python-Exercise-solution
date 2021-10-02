def squareEach(nums):
    acc= []
    for i in nums:
        i = int(i)
        square = i**2
        acc.append(square)
    return acc

def main():
    print("this program is to print the square of each entry")
    value_list = input("please type your numbers ")
    value = value_list.split()
    answer = squareEach(value)
    print(answer)
main()
