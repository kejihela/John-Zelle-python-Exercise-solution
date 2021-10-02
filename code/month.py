def Month():
    months = "JanFebMarAprMayJunJulAugSepNovDec"
    n = int(input("Please, input the month between 1-12" ))
    pos = (n-1)*3
    month = months[pos:pos+3]
    print("The month is", month)

            
Month()
