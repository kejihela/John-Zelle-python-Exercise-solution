import math
def main():
    print("This program will print the root of quadratic equation")
    a = int(input("please, enter the value of a "))
    b = int(input("please, enter the value of b "))
    c = int(input("please, enter the value of c "))
    try:
        determinant = b*b - 4*a*c
        root = math.sqrt(b*b - 4*a*c)
        root1 = (-b+root)/(2*a)
        root2 = (-b-root)/(2*a)
        print(root1, root2)
    except ValueError as excObj:
        if str(excObj)=="math domain error":
            print("no real root")
        else:
            print("invalid coefficient given")
    except:
        print("something went wrong")
       
main()    
            

