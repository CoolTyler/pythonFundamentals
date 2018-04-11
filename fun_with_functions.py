def odd_even():
  for i in range (1, 2000):
    if i % 2 == 0:
      print 'Number: ', i, 'This is an even number'
    else:
      print 'Number: ', i, 'This is an odd number'

odd_even()

new_list = []

def mult(num, list):
  for val in list:
    val = val * num
    new_list.append(val)
  return new_list


hello = [1, 2, 3, 4, 5]
test = 10
mult(test, hello)


def layered_multiples(list):
  print list
  new_list2 = []
  for i in list:
    val_list = []
    for x in range (0, i):
      val_list.append(1)
    new_list2.append(val_list)
    print new_list2
  return mult(2,[1,3,5,8])

y = layered_multiples(mult(2,[1,3,5,8]))



