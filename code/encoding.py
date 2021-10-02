def main():
    print("This program is about to print encoded characters")
    message = input("please enter your message")
    for ch in message:
        result = ord(ch)
        print(result)

main()
