input = input("camelCase: ")
word = ""
word_string_list = []
for c in input:
  if c.islower():
    word = word + c
  if c.isupper():
    word_string_list.append(word)
    word = c
word_string_list.append(word)
print('_'.join(word_string_list).lower())
