def main():
    print("This program is about to calculate greatest common divisor")
    n = int(input("please input your divisor "))
    m = int(input("please input your divisee "))
    k = 1
    gcd = []
    while(k>0):
        k = n%m
        n = m+0
        m = k+0
        gcd.append(m)
    print(gcd[-2])
main()
