def main():
    print("This program will print the grade of student")
    score = int(input("Please input your score "))
    if score >= 90:
        print("the grade is A")
    elif score >= 80 and score < 90:
        print("The grade is B")
    elif score >= 70 and score < 80:
        print("The grade is C")
    elif score >= 60 and score < 70:
        print("The grade is D")
    else:
        print("The grade is F")
main()
        
