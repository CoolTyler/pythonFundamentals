# isinstance(object, classinfo) - returns true if object argument is an instance of the corresponding classinfo argument
# type(object) - when only one argument, "type()" returns the type of object given.  isinstance is recommended when testing type of object

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


def types(object):
  if isinstance(object, int):
    if object >= 100:
      print "That's a big number!"
    elif object < 100:
      print "That's a sumall number, lol"
  elif isinstance(object, str):
    if len(object) >= 50:
      print "Long sentence"
    elif len(object) < 50:
      print "That's a small sentence"
  elif isinstance(object, list):
    if len(object) >= 10:
      print "Big ol' list!"
    elif len(object) < 10: 
      print "Very short list"
types(aL)
types(sS)
types(bI)
types(eL)