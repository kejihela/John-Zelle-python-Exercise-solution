def main():
    print("This program will print investment doubling")
    investment = eval(input("please input the investment value "))
    interest_rate = eval(input("please input your interest rate "))
    interest = investment * 2
    count = 0
    while(investment < interest):
        investment = investment * (1 + interest_rate)
        count = count+1
    print(count)
main()
                      
