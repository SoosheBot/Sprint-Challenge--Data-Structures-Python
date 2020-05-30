import time
from binary_search_tree import BSTNode


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
WORKING CODE TO REDUCE THE TIME THAT I WROTE INITIALLY -- BUT I IMPROVED THE TIME WITH THE STRETCH GOAL, BELOW, SO CHECK IT OUT!
"""
nodes = BSTNode('')

for name_1 in names_1:
    nodes.insert(name_1)

for dupe_names in names_2:
    if nodes.contains(dupe_names):
        duplicates.append(dupe_names)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


print(f"{len(set(names_1) & set(names_2))} duplicates using built-in-tool set: {set(names_1) & set(names_2)}")
print (f"runtime: {end_time - start_time} seconds, which is super faster compared to the previous code's runtime: 0.1678149700164795 seconds, and the original code's runtime: 11.417479038238525 seconds")

"""
TO *NOTE* -- With the code from the previous version commented out, we get:
runtime: 0.0035440921783447266 seconds using the set built-in-tool
"""