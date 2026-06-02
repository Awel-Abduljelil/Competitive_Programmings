def modify_word(word):
  upper_count = 0
  lower_count = 0
  for char in word:
    if char.isupper():
      upper_count += 1
    elif char.islower():
      lower_count += 1
  if upper_count > lower_count:
    return word.upper()
  else:
    return word.lower()
if __name__ == "__main__":
  word = input()
  result = modify_word(word)
  print(result)
