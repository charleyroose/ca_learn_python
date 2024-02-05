import re

# Your code goes here
find_members = dir(re)
for member in find_members:
    if "find" in member:
        find_members.append(member)

sorted_find_members = sorted(find_members)
print(sorted_find_members)