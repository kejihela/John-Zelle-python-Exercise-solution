def main():
    a, b, c = eval( input('Enter three numbers: ' ))
    if a > b:
        if b>c:
            print("spam" )
        else:
            print("its a late parrot")
    elif b>c:
        print("Cheese Shoppe" )
        if a >= c :
            print("Cheddar" )
        elif a < b :
            print ("G ouda" )
        elif c == b :
            print("Swiss" )
    else:
        print("Trees" )
        if a == b:
            print("Chestnut" )
        else :
            print("Larch" )
        print ("Done")
main()
