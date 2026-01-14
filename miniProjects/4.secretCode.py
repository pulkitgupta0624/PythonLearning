'''
Write a python program to translate a message into a secret code and decode it back to the original message.
Use the rules below  to translate normal english to secret code:

Coding Rules:
if the word contains atlease 3 characters, remove the first letter and append it to the end and now append three random characters at the starting and the end 
else simplye reverse the string

Decoding Rules:
if the word contains less than 3 characters, reverse the string
else remove the 3 random characters from the starting and the end, now remove the last character and append it to the starting of the word
'''

import random
import string

# function to generate 3 random letters
def random_chars():
    return ''.join(random.choices(string.ascii_letters, k=3))


def encode_message(message):
    words = message.split()
    coded_words = []

    for word in words:
        if len(word) >= 3:
            first_letter = word[0]
            new_word = word[1:] + first_letter
            coded_word = random_chars() + new_word + random_chars()
            coded_words.append(coded_word)
        else:
            coded_words.append(word[::-1])

    return " ".join(coded_words)


def decode_message(message):
    words = message.split()
    decoded_words = []

    for word in words:
        if len(word) < 3:
            decoded_words.append(word[::-1])
        else:
            # remove 3 random chars from start and end
            core = word[3:-3]
            # last char comes to the beginning
            decoded_word = core[-1] + core[:-1]
            decoded_words.append(decoded_word)

    return " ".join(decoded_words)


# -------- MAIN PROGRAM --------
print("🔐 Secret Code Translator 🔐")
print("1. Encode Message")
print("2. Decode Message")

choice = input("Enter your choice (1/2): ")

msg = input("Enter your message: ")

if choice == "1":
    print("\n✅ Encoded Message:")
    print(encode_message(msg))
elif choice == "2":
    print("\n✅ Decoded Message:")
    print(decode_message(msg))
else:
    print("❌ Invalid choice")
