# ice = [1,2,5,6,2]
# fire = [1,2,5,6,2]
# alliance = [1,2,5,6,5,16]
# horde = [1,2,5,6,5]
couch = ['celery','carrots','bread','milk']
shoe = ['celery','carrots','bread','cream']

def comp_list(list_a, list_b):
  if list_a == list_b:
    print "The lists are the same."
  else:
    print "The lists are different."

comp_list(couch, shoe)