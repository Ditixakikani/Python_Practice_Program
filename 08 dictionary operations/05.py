sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
newDict = {k: sample_dict[k] for k in keys}
print(newDict)

# key = dict()
# for k in keys:
#     key.update({k:sample_dict[k]})
# print(key)    