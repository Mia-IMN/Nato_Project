import pandas

nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {value.letter:value.code for (key, value) in nato_alphabets.iterrows()}
# print(nato_dictionary.get("E"))

user_input = input("Enter a word: ").upper()
answer = [nato_dictionary.get(word) for word in user_input]
print(answer)
