new_list = ["magical unicorns", 19, "hello", 98.98, "world"]
interger_list = [1, 2, 3, 4, 5]
string_list = ["hey", "hi", "ho"]

def list_type(lst):
  new_str = ""
  sum = 0

  for value in lst:
    if isinstance(value, int) or isinstance(value, float):
      sum += value
    elif isinstance(value, str):
      new_str += `value`
  if new_str and sum:
    print "You got a mixed thingy there"
    print "Sum:  " + `sum`
    print "String", new_str

  elif new_str:
    print "The array you entered was a string"
    print "String", new_str
  
  else:
    print "The string you entered is all numbers"
    print "Sum:  " + `sum`

list_type(new_list)