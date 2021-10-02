def BMI(weight, height):
    bmi = (weight * 720)/height**2
    return bmi
def main():
    print("This program is to calculate the BMI of persons")
    w = int(input("Please input your weight "))
    h = int(input("please input your height "))
    result = BMI(w, h)
    if result < 19:
        print("you are below the healthy range")
    elif result >=19 and result <=25:
        print("you are within the healthy range")
    else:
        print("you are far from it")
main()
    
