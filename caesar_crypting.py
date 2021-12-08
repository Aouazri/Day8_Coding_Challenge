from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in range(len(start_text)):
    if start_text[char] not in alphabet:
      end_text+= start_text[char]
    else:
      position = alphabet.index(start_text[char])
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)
 
answer= "yes"
while answer == "yes":
   
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
#in case the user inputs a shift over 26
  if shift > 26: 
    shift= shift %26 

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  answer= input('Do you want to continue, type "yes" or "no" ')