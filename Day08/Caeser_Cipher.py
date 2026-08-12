from art import logo
alphabet =[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    if direction == "decode":
        shift *= -1
    print(f"Your {direction}d text is: ")
    
    for letter in text:
        shifted_position = alphabet.index(letter)+shift
        output_text= (alphabet[shifted_position])
        print(output_text,end="")
        if letter not in alphabet:
            output_text += letter
    print("\n")
        
print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    should_continue = input("Type 'yes' if you want to go again. Otherwie type 'no'.")
    caesar(direction,text,shift)
    if should_continue == 'no':
        should_continue = False
        print("Goodbye!")
    


