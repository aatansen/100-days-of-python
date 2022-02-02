alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_or="cay"
word=list(word_or)
# print(word)
# x=alphabet.index('c')
# print(x)
shift=5

encrypt_word=""
for i in range(len(word)):
    word_by_word=word[i]
    encrypt_letter=alphabet.index(word_by_word)+shift
    # print(encrypt_letter)
    if encrypt_letter>=26:
        # fixing index error
        index_sol=encrypt_letter-len(alphabet)
        encrypt_word+=alphabet[index_sol]
    else:
        encrypt_word+=alphabet[encrypt_letter]
print(f"original word is: {word_or}")
print(f"encrypted word is: {encrypt_word}")
