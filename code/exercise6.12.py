def sumEach(nums):
    acc= 0
    for i in nums:
        i = int(i)
        acc = acc + i
    return acc

def main():
    print("this program is to print the square of each entry")
    value_list = input("please type your numbers ")
    value = value_list.split()
    answer = sumEach(value)
    print(answer)
main()
