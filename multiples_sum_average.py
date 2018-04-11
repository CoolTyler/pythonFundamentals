
num = 1 # our number that increments every loop

for num in range(1, 1000):
  if num % 2 != 0:  # modulo operator, meaning if the number is not even, it will print.
    print num

num = 5
for num in range(5, 1000000): # commas, like in "1,000,000" are not welcome.
  if num % 5 == 0:  # if the number divided by 5 leaves no remainder, it is a multiple of 5.
    print num

sum = 0 # needed for the average
a = [1, 2, 5, 10, 255, 3] # my list of values

for nums in a:
  # print nums
  sum += nums # sum starts at 0, but goes through and adds the current value each loop
print sum # prints the sum of 276

for nums in a:
  avg = sum / len(a) # divides the total sum by amount of indices aka len(a)
print avg  # outputs 46

