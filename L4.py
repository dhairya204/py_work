#***Dictniories in python:-***

# info={
#     "name":"dc",
#     "subjects":["python","c","c++"],  
#     "topics":{"dict","set"},
#     "age" : 35,
#     "is_adult":True,
#     "marks":94.4

# }

# print(info["name"])
# print(type(info))
# info["name"]="kairon"
# print(info)

# student={
#     "name":"dc",
#     "age":"20",
#     "subjects":{
#         "maths":"95",
#         "phy":"98",
#         "chem":"92"
#     }
# }
# print(student["subjects"]["chem"])

# example of:- .format()
# name="dc"
# age="20"
# print("My name is {} and I am {} years old".format(name, age))

#methods of dict:-
# print(student.keys())
# print(len(tuple(student.keys())))
# print(student.values())
# print(student.items())
# print(student.get("subjects").get("chem"))
# student.update({"city":"delhi"})
# print(student)

#***Sets in python:-***

 # collection={1,2,2,2,"dc","aa",3,4}
 # print(collection)
 # print(type(collection))

# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("kairon")
# collection.remove(1)
# collection.add((1,2,3))
#collection.add([1,2,3]) #haseable value
# collection.pop( )
# print(collection)
# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))