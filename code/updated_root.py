import math
def main():
    print("This program will print the root of quadratic equation")
    a = int(input("please, enter the value of a "))
    b = int(input("please, enter the value of b "))
    c = int(input("please, enter the value of c "))

    determinant = b*b - 4*a*c

    if determinant > 0:
        root = math.sqrt(b*b - 4*a*c)
        root1 = (-b+root)/(2*a)
        root2 = (-b-root)/(2*a)
        print(root1, root2)
    elif determinant == 0:
        root3 = -b/2*a
        print("the solution has one root at ",root3)
    else:
        print("The equation has no real root")

main()    
            
