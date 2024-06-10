
# Remove all occurrences a given element from the list

characters_na = ["Naruto", "Hinata", "Sasuke", "Sai", "Kakashi", "Hinata", "Itachi", "Hinata"]

not_requried = "Hinata"

new_character = [x for x in characters_na if x != not_requried]

print(new_character)