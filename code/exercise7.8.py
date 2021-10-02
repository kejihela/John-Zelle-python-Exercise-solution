def election(age, duration):
    if age >= 30 and duration >=9:
        print ("you are eligible to be a senator and a representative")
    
    elif age >= 25 and duration >=7:
        print ("you are eligible to be a representative")
    else:
        print("you can vote but cant be voted for")
    return None

def main():
    print("This program will print out your eligibility")
    a = int(input("How old are you "))
    d = int(input("how many years have you spend in the U.S "))
    result = election(a,d)
    print(result)
main()
                   
              
    
    
