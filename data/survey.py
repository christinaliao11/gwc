import json

dict_data = {}
dict_data_list = []

questions = ["type your name: ", "type your age: ", "type your school: ", "type your height: "]

# keys = ["name", "age", "school", "height"]

for k, v in questions.items():
    resp = input(v)
    dict_data[k] = resp
    dict_data_list.append(dict_data)


#for i in range(len(keys)):
 #   resp = input(questions[i])
  #  dict_data[keys[i]] = resp


f = open("data.json", "r")
olddata = json.load(f)
print(olddata)
dic_data_list.extend(olddata)
f.close()

with open("data.json","w+") as outfile:
    json.dump(sur_daa_life, outfile,)

print(dict_data)

#dict_data = {}
#user_name = input("Type your name: ")
#dict_data["name"] = user_name

#user_age = input("Type your age: ")
#dict_data["age"] = user_age

#user_born = input("Where were you born? Type here: ")
#dict_data["place of birth"] = user_born

#user_use = input("What is your favorite social media platofrm? Type here: ")
#dict_data["Fav social media"] = user_use

#user_friend = input("Who is your bestfriend?")
#dict_data["Bestfriend"] = user_friend

#user_frname = input("How long have you known them?")
#dict_data["Bsf name"] = user_frname
