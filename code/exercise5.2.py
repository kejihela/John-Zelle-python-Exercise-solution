def grade():
    print("This program will print the grade of a corresponding score")
    score = int(input("please input your score "))
    grade_value = [ "A", "B", "C", "D", "E", "F"]
    grade = grade_value[score - 1]
    print("The corresponding grade of your score is",grade)
grade()
