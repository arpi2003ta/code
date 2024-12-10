from copy import copy, deepcopy
stdinfo = ("Linda", 18, ["Math", "Physics", "History"])
stdprofile = copy(stdinfo)
print(stdinfo)
print(stdprofile)
stdprofile[2][1] = "Chemistry"
print(stdinfo)
print(stdprofile)
stdprofile = deepcopy(stdinfo)
print(stdinfo)
print(stdprofile)
stdprofile[2][2] = "Computer Science"
print(stdinfo)
print(stdprofile)
