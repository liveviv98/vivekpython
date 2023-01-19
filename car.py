thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x,y in thisdict.items():
    print(x,y)
for x in thisdict.values():
    print(x)
    
thisdict["color"]="red"
print(thisdict)
thisdict.pop("model")
print(thisdict)
