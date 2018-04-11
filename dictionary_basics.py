# tyler = {}
# tyler["first_name"] = "Tyler"
# tyler["age"] = "31"
# tyler["c_o_b"] = "The U.S of A"
# tyler["fav_lang"] = "High Valyrian"

tyler = { 
"info": [
          {"stat": "Tyler", "grt": "My name is"},  
          {"stat": "31", "grt": "My age is"}, 
          {"stat": "The U.S of A", "grt": "My country of birth is"}, 
          {"stat": "High Valyrian", "grt": "My favorite language is"}
  ]
} # at first I had this commented out and planned to use the above dictionary, then I just added some nested dictionaries (and list) until it carried all the info I needed.  The weird indenting was done strictly to look cleaner and work off the first dictionary, but it ended up working when it ran.

# print tyler

def dics(dic):
  for key, data in dic.items():
    for value in data:
      print value["grt"], value["stat"]


dics(tyler)   