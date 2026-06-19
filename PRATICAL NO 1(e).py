sentence = input("Enter a sentence: ")

word_count = len(sentence.split())

char_count = len(sentence)

lower_case = sentence.lower()

upper_case = sentence.upper()

modified_sentence = sentence.replace(" ", "_")

print("\nResults:")
print("Number of words      :", word_count)
print("Number of characters :", char_count)
print("Lowercase sentence   :", lower_case)
print("Uppercase sentence   :", upper_case)
print("Sentence with '_'    :", modified_sentence)
