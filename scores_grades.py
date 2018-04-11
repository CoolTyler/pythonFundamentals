import random

def grades(reps):
  str_one = 'Your grade is'

  for i in range(0, reps):
    score = random.randint(60, 100)
    if score >= 60 and score < 70:
      print 'Score: ', score, ';', str_one, 'D'
    elif score >= 70 and score < 80:
      print 'Score: ', score, ';', str_one, 'C'
    elif score >= 80 and score < 90:
      print 'Score: ', score, ';', str_one, 'B'
    elif score >= 90:
      print 'Score: ', score, ';', str_one, 'A'
    else:
      print 'Better luck next time chief'

grades(10)