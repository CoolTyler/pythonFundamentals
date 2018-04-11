def drawstars(list):
  for i in list:
    # val_i = list[i]
    print '*' * i
    # if isinstance(val_i, int):      # apparently I was trying to do both functions in the first function, so this code isn't useful here
    # # elif isinstance(val_i, str):
    # #   print str[0] * val_i
    # else:
    #   continue
drawstars([8, 8, 8, 8, 8, 8])

def draw2(tup):
  for i in tup:
    if isinstance(i, int):
      print '*' * i
    elif isinstance(i, str):
      length = len(i)
      letter = i[0].lower()
      # print i[0] * len(i)
      # if i-1 == " ":        # first attempt to capitaize the first letter of each string, but I couldn't figure out how to compare "i" with a possible empty space before it.
      #   print i * len(i)
      print letter * length

test = (2, "Hello", 5, "Tommy Two Times")
draw2(test)