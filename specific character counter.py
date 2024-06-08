#create counter that counts number of specific characters in a word

def count_char_x(word, x):
  char_counter = 0
  for char in word:
    if char == x:
      char_counter += 1
  return char_counter

print(count_char_x("mississippi", "s"))

print(count_char_x("mississippi", "m"))
