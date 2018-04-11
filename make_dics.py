name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dics(key_list, value_list):
  new = dict(zip(key_list, value_list))
  print new

  
make_dics(name, favorite_animal)

