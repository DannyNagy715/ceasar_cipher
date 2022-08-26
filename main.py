
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_on = True
while is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(text, shift):
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the 
        #shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"
        result = ""
        for char in text:
            position = alphabet.index(char)
            new_position = position + shift
            new_char = alphabet[new_position]
            result += new_char
        
        print(f"Your encoded message is {result}")

    def decrypt(text, shift):
        original = ""
        for char in text:
            position = alphabet.index(char)
            new_position = position - shift
            new_char = alphabet[new_position]
            original += new_char
        
        print(f"Your original message is {original}")

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


    if direction == "encode":   
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    wanna_go_on = input("Do tou want to continue? (yes or no)\n")
    if wanna_go_on == "yes":
        is_on = True
    elif wanna_go_on == "no":
        is_on = False
    else:
        print("Not in the spectrum")