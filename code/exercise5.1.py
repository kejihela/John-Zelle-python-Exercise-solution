def dateformat():
    print("This  program will print the date you type in")
    date = input("please input the date format mm/dd/yyyy")
    month, day, year = date.split("/")
    month_value = int(month)
    month_list  = ["january", "february", "march","april","may","june",
                   "july","august","september", "November", "december"]
    date_month = month_list[month_value - 1]
    print("the date is {0}/{1}/{2}".format(date_month, day, year))
dateformat()
    
                
