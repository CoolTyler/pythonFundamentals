def find_items(char, list):
  new_thing = []
  for item in range(0, len(list)):

    if list[item].find(char) != -1:
      new_thing.append(list[item])

  print new_thing


list_example = ['this', 'is', 'the', 'lengthy', 'list', 'i', 'am', 'making']
# char_example = 'i'
find_items('t', list_example)

