def main():
     print("This program will print a valid date or not")
     date_number = input("please input your date as mm/dd/year ")
     month, day, year = date_number.split("/")
     month = int(month)    

     if month == 2:
         if int(day) >=0 and int(day) <=29:
             print("the date is valid", month, day, year)
         else:
             print("the date is not valid", month, day, year)
        
     
     elif month==9 or month==4 or month==6 or month == 11:
         if int(day) >0 and int(day) <=30:
             print("the date is valid", month, day, year)
         else:
             print("the date is not valid", month, day, year)
       
         
     if month==1 or month==3 or month== 5 or month== 7 or month==8 or month==10:
         if int(day) >0 and int(day) <=31:
             print("the date is valid,", month, day, year)
         else:
             print("the date is not valid", month, day, year)
     else:
         print("the date is not valid", month, day, year )
         
main()
