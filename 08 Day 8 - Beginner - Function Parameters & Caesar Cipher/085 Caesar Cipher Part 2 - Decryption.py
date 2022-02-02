direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift_num=int(input("Type your shift number:\n"))

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# text="zzzbc"
# shift_num=5
def encrypt(message,sft_amount):
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
    print(f"The original text is: {message}")
    print(f"The encoded text is: {cipher_text}")
    

def decrypt(cipher_text,sft_amount):
    original_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-sft_amount
        original_text+=alphabet[new_position]
    print(f"The original text is: {cipher_text}")
    print(f"The decoded text is: {original_text}")
    

if direction=="encode":
    encrypt(message=text,sft_amount=shift_num)
elif direction=="decode":
    decrypt(cipher_text=text,sft_amount=shift_num)
else:
    print("Please type 'encode' or 'decode'")



#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message. encrypt(plain_text=text, shift_amount=shift)