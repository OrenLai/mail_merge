# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as namelist:
    names = namelist.readlines()

with open("Input/Letters/starting_letter.txt") as mail:
    mail_text = mail.read()
    for name in names:
        stripped_name = name.strip()
        new_mail = mail_text.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as new_mail_file:
            new_mail_file.write(new_mail)
