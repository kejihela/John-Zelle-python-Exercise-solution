def molecular_formular():
    print("This program will computes the molecular weight of carbs")
    h = int(input("How many hydrogen do we have "))
    o = int(input("How many oxygen do we have "))
    c = int(input("How many carbon do we have "))
    H = 1.00794
    C = 12.0107
    O = 15.9994

    ans = h*H + o*O + c*C
    print("molecular weight of the above carbohydrate is ", ans)
molecular_formular()

    
