def main():
    print("This program is about to decode messages")
    message = input("please type in your input ")
    output = ""
    for intstring in message.split():
        st = int(intstring)
        output = output + chr(st)
    print(output)

       
        
        
main()
