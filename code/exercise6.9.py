def grade(score_value, grade_value):
    grade = grade_value[score_value - 1]
    return grade
def main():
    print("print the corresponding grade of the score")
    score_value = int(input("please input your score "))
    grade_value =["F","F","F","F","F","F","F","F","F","F","F","F","F","F",
                  "F","F","F","F","F","F","F","F","F","F","F","F","F","F",
                  "F","F","F","F","F","F","F","F","F","F","F","F","F","F",
                  "F","F","F","F","F","F","F","F","F","F","F","F","F","F",
                  "D","D","D","D","D","D","D","D","D","D","C","C","C","C",
                  "C","C","C","C","C","C","C","B","B","B","B","B","B","B",
                  "B","B","B","A","A","A","A","A","A","A","A","A","A","A"]
    student_grade = grade(score_value, grade_value)
    print(student_grade)
main()
    
