def count():
    print("this program is to count the number of characters in a sentence")
    text = input("please type in your sentence ").split()
    count = 0
    for character in text:
        count = count + 1
    print(count)
count()
    
