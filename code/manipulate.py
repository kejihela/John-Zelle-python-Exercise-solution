def main():
    print("This will compute the easter date")
    
    for year in range(1900, 2100):
        a = year%19
        b = year%4
        c = year%7
        d = (19*a + 24)%30
        e = (2*b+4*c+6*d)%7
        day = (22 + d + e)%31
        if day == 0:
            day = day+1
            month = "April"
            print("The day of easter is ",month,"/",day,"/",year)
            print(d,e)
        else:
            month = "April"
            print("The day of easter is ",month,"/",day,"/",year)
            print(a,b,c,d,e)
       
    
main()
        

