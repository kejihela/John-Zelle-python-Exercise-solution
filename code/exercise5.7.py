def ciphers():
    print("this program encode and decode a plaintext")
    key = int(input("please input the value of your key "))
    text = input("Please input your string of text ")
    message = ""
   
    for i in text:
        message = message + (chr(ord(i) + key)) 
    print(message)
    output = ""
    for ch in message:
        output = output + (chr(ord(ch) - key))
        output.join(output)
    print(output)
ciphers()
          
        
          
