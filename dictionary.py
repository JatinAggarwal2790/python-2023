# working with dictionaries

std = {"040":"Hyderabad",
       "080":"Bangalore",
       "022":"Mumbai"}

print(type(std))
print(len(std))
print(std.keys())
print(std.values())

# how to lookup

print(std["040"])
print(std.get("080"))

# how to add an item
std["044"] = "Chenni"
print(len(std))

# how to delete an item

std.pop("022")
print(len(std))

# how to update an item
std["044"] = "Chennai"
print(std)


