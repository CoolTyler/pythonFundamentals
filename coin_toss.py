import random
def toss(reps):
  # attempt = "Attempt #"
  # throw = "Throwing a coin..."
  # head = "It's a head!  ... Got"
  # tail = "It's a tail :( ... Got"
  # so_far = "so far and"
  ac = 1
  hc = 0
  tc = 0



  for i in range(1, reps + 1):
    result = random.randint(0,1)
    result_rounded = round(result)
    if result_rounded == 0:
      hc += 1
      print "Attempt #", i, ":  Throwing a coin... It's a head! ... Got ", hc, "head(s) so far and", tc, "tail(s) so far"
      ac += 1
    else:
      tc += 1
      print "Attempt #", i, ":  Throwing a coin... It's a tail! ... Got ", tc, "tail(s) so far and", hc, "head(s) so far"
      ac += 1
      
toss(10)