def date():
    print("This program is going to print the date")
    input_date = input("please type in your date with format DD/MM/YYY")
    month = ["January", "february", "March", "April", "May", "June","July",
             "August", "September", "October", "November", "December"]
    daystr, monthstr, yearstr= input_date.split("/")
    monthstr = month[int(monthstr)-1]
    print("the date is,",daystr,"/",monthstr,"/",yearstr)
    
date()
