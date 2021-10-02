def student_standing(credit):
    if credit < 7:
        print("The student is a fresh man")
    elif credit >=7 and credit < 16:
        print("The student is a sophomore")
    elif credit >= 16 and credit < 26:
        print("The student is junior")
    else:
        print("The student is junior")
    

def main():
    print("This program will print the student standings ")
    score = int(input("please input your credit score "))
    result = student_standing(score)
    print(result)
main()
    
