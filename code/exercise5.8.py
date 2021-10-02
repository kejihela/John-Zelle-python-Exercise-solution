def ciphers():
    print("this program encode and decode a plaintext")
    key = int(input("please input the value of your key "))
    text = input("Please input your string of text ")
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                 "n","o","p","q","r","s","t","u","v","w","x","y","z"]
                 
    message = ""
   
    for i in text:
       text_value = ord(i) - 96 + key
       answer = text_value%26
       output = alphabets[answer - 1]
       message = message + output
    print(message)
    decode_output = ""

    for ch in message:
        decode_value = ord(ch)-96-key
        decode = decode_value%26
        decode_result = alphabets[decode-1]
        decode_output = decode_output + decode_result  
    print(decode_output)
        
ciphers()
          
