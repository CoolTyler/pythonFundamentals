users = {
 'Students': [ #key[0]?
     {'first_name':  'Michael', 'last_name' : 'Jordan'}, #key[0]
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [ #key[1]?
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

students_list = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def part_one(list):
#   for i in list():
#     for value in list:
#       enumerate(list)
#       print value["first_name"], value["last_name"]

# part_one(students)#

# print students[0]  #prints {'first_name': 'Michael', 'last_name': 'Jordan'}

# def names(list):
#   for dictionary in list:
#     di = dictionary.iteritems()   #.iteritems() and .next(), pretty handy!
#     dn = di.next()
#     print dn[1]
#     dn2 = di.next()
#     print dn2 [1]                              
# names(students)   # This will output each first name accompanied by its matching last name, but they all come out on separate lines.  Not quite what we want.

def studs(list):
  for namies in list:
    print namies["first_name"], namies["last_name"]
studs(students_list)  # Correct output

def user_dicto(dict):
  for key, data in dict.items():
    # print key
    for values in data:
      # print values
      for res in values:
        print values[res] # "values[res] == string"
user_dicto(users)

def show_all(dicty):
    for role in dicty:
        counter = 0
        print role
        for person in dicty[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)
show_all(users)