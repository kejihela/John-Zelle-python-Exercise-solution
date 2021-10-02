def average_count():
    print("this program is to count the number of characters in a sentence")
    text = input("please type in your sentence ").split()
    count = 0
    acc = 0
    
        
    for word in text:
        acc = acc + 1
        for i in word:
            count = count +1
    answer = count/acc   
        
    print(answer)
average_count()
