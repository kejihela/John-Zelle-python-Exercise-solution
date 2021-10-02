
import math
def quadratic_equation():
    
    print("This program find the roots of a quadratic equation")
    a = float(input("please, input the value of your a "))
    b = float(input("please input the value of your b "))
    c = float(input("please input the value of c "))

    disc_root = math.sqrt(b*b - 4 * a * c)
    root1 = (-b + disc_root)/(2 * a)
    root2 = (-b - disc_root)/(2 * a)

    print("The root of the eqution is ", root1, root2)
quadratic_equation()
