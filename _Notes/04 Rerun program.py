# rerun the program using function:
def main():
    num=int(input("enter a number:"))
    print(f"Your entered number is {num}.")

    restart=input("Enter number again? 'yes' or 'no'").lower()
    if restart=="yes":
        main()
    else:
        exit()
main()

# rerun the program using condition 'while':
is_restart=True
while is_restart:
    num=int(input("enter a number:"))
    print(f"Your entered number is {num}.")
    restart=input("Enter number again? 'yes' or 'no'").lower()
    if restart=="no":
        is_restart=False