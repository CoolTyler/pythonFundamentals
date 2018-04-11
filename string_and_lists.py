#.find()
# .replace()
# min()
# max()
# .sort()
# len()

words="It's thanksgiving day.  It's my birthday, too!"
print words.find("day")
print words.replace("day", "month")

x=[2, 54, -2, 7, 12, 98]
print (min(x), max(x))

x=["hello", 2, 54, -2, 7, 12, 98, "world"]
print (x[0], x[-1])

x=[2, 4, 546, 23, 2, 2340]
x.sort()
print x

y=int(len(x)/2)
print y
x[:y]

print (x[:y])

front = x[:y]
back = x[y:]

back.insert(0, front)
print back