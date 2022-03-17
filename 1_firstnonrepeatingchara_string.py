def first_non_repeating_character(string):
  char_order = []
  dict = {}
  for str in string:
    if str in dict:
      dict[str] += 1
    else:
      dict[str] = 1
      char_order.append(str)
  for c in char_order:
    if dict[c] == 1:
      return c
  return None

a=input("enter a string")

print(first_non_repeating_character(a))

