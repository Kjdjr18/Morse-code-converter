from MORSE_CODE_DICT import MORSE_CODE_DICT

print(
    "Welcome to my morse code conversion app. The app will remain open until you close it down, and will continue to "
    "ask you for a new word or phrase. Spaces between words are identified by '|'.\n type 'exit!' to exit the "
    "application")

is_app_open = True

while is_app_open:
    user_list = []
    converted_list = []
    user_input = input("Input a phrase you would like to convert into morse code: ").upper()
    if user_input != "EXIT!":
        for letter in user_input:
            user_list.append(letter)

        for key in user_list:
            if key in MORSE_CODE_DICT:
                converted_list.append(MORSE_CODE_DICT[key])
            else:
                print("At least one of the characters in your word is not found in the dictionary.")
        joined_morse_code = ' '.join(converted_list)
        print(f"Here is your converted word in morse code!\n{joined_morse_code}")
    else:
        is_app_open = False
