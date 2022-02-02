# direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text=input("Type your message:\n").lower()
# shift_num=int(input("Type your shift number:\n"))

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text="helloworld"
shift_num=5
def encrypt(message,sft_amount):
    # message=list(message)
    cipher_text=""
    for letter in message:
        position=alphabet.index(letter)
        new_position=position+sft_amount
        # print(new_position)
        #note if i add alphabet 2 times in list alphabet I won't need this condition
        if new_position>25:
            fix_position=new_position-len(alphabet)
            cipher_text+=alphabet[fix_position]
        else:    
            cipher_text+=alphabet[new_position]
    print(f"The encoded text is: {cipher_text}")
    print(f"The original text is: {message}")

    
encrypt(message=text,sft_amount=shift_num)



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
  