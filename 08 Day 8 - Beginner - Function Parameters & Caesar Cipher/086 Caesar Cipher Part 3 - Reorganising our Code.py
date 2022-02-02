direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift_num=int(input("Type your shift number:\n"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = "decode"
# text = "mjqqt"
# shift_num = 5
def caesar(direct, message, sft_amount):
    end_text=""
    if direct=="decode":
        sft_amount*=-1
    for letter in message:
        position=alphabet.index(letter)
        new_position=position+sft_amount
        end_text+=alphabet[new_position]
    print(f"Your {direction}d result : {end_text}")
caesar(direct=direction, message=text, sft_amount=shift_num)

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
