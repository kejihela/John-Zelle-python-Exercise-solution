def main():
    print("This will compute the easter date")
    year = int(input("Please input the year "))
    if year >= 1900 and year <=2099:
        a = year%19
        b = year%4
        c = year%7
        d = (19*a + 24)%30
        e = (2*b+4*c+6*d)%7
        day = (22 + d + e)%31
        if year == 1954 or year==1981 or year == 2049 or year==2076:
            day = day+7
            month = "April"
            print("The day of easter is ",month,"/",day,"/",year)
            print(d,e)
        else:
            month = "April"
            print("The day of easter is ",month,"/",day,"/",year)
            print(a,b,c,d,e)
       
    else:
        print("you enter the wrong year")
main()
        
