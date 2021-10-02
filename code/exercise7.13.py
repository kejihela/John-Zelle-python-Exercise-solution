def leap_year(month, day):
    if month==2 and day ==29:
        year_number = 31*(month - 1)+day + 1
        print("the corresponding day is", year_number, "and its a leap ") 
    elif month > 2:
        num_year = (31*(month - 1)+day) - ((4*(month)+23)//10)
        print("the corresponding day is",num_year)
    else:
        year_number = 31*(month - 1)+day
        print(year_number)

    

def main():
     print("This program will print a valid date or not")
     date_number = input("please input your date as mm/dd/year ")
     month, day, year = date_number.split("/")
     month = int(month)
     day = int(day)

     if month == 2:
         if int(day) >=0 and int(day) <=28:
             print("the date is valid", month, day, year)
         else:
             print("the date is not valid", month, day, year)
        
     
     elif month==9 or month==4 or month==6 or month == 11:
         if int(day) >0 and int(day) <=30:
             print("the date is valid", month, day, year)
         else:
             print("the date is not valid", month, day, year)
       
         
     elif month==1 or month==3 or month== 5 or month== 7 or month==8 or month==10:
         if int(day) >0 and int(day) <=31:
             print("the date is valid", month, day, year)
         else:
             print("the date is not valid", month, day, year)
     else:
         print("the date is not valid", month, day, year )

         
     leap = leap_year(month, day)
     print(leap)

         
         
main()
