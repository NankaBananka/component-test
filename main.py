import os
print("root", os.listdir("/data"))
print("root/repository", os.listdir("/data/repository"))
list_dir = os.listdir()

for i in list_dir:
  print(os.path.isdir(i), i)

print(os.listdir("/src"))


