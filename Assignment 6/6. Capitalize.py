a_str = input("Input a string: ")

new_sentence = ""
for word in a_str.split():
    new_word = word.title()
    new_sentence += new_word
    new_sentence += " "
print(new_sentence)