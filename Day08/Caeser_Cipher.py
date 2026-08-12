from art import logo
alphabet =[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(direction,text,shift):
    output_text = ""
    if direction == "decode":
            shift *= -1
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter)+shift
            output_text= (alphabet[shifted_position])
            print(output_text,end="")
    print("\n")     
    print(f"Your {direction}d text is: ")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    caesar(direction,text,shift)
    should_continue = input("Type 'yes' if you want to go again. Otherwie type 'no'.")

    if should_continue == 'no':
        should_continue = False
        print("Goodbye!")
    


