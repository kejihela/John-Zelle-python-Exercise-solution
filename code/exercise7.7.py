import math
def start_time(start_hour, start_minutes):
    if start_minutes >= 60:
        start_hour = start_hour + (start_minutes//60)
        minute = (minutes%60)
        start = start_hour + (start_minutes/100)              
        return start      
    else:
        start = start_hour + (start_minutes/100)
        return start
def end_time(end_hour, end_minutes):
    if end_minutes >= 60:
        end_hour = end_hour + (end_minutes//60)
        end_minutes = (end_minutes%60)
        end= end_hour + (end_minutes/100)
        return end     
    else:
        end = end_hour + (end_minutes/100)
        return end
    
def charges(start, end):
    if start >=7 and start <=20.59:
        if end>=7 and end <=20.59:
            work_time = abs(end-start)
            charges = work_time * 2.5
            return charges
        else:
            work_end_time = (21 - end)*1.5
            charges = (start- end-work_end_time)*2.5
            result = work_end_time + charges
            return result        
    else:
         work_start_time = abs(start - 7)*1.5
         charges = (end - start- work_start_time)*2.5
         result= work_start_time +  charges
         return result
        #else:
            #work_time = abs(end_time-start_time)
            #charges = work_time * 1.5
            #return charges           

def main():
    print("This program willl print the amount charge for baby sitting")
    start_hour =float(input("please input your time in hours "))
    start_minutes = float(input("please input your time in minutes "))
    end_hour =float(input("please input your time in hours "))
    end_minutes = float(input("please input your time in minutes "))
    start_time(start_hour, start_minutes)
    end_time(end_hour, end_minutes)
    charges(start, end)
main()
    
    
    
        
    
    
                  
              
