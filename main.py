import os
print("root", os.listdir("/data"))
print("root/repository", os.listdir("/data/repository"))


print("parent", os.listdir("../"))

for i in os.listdir("../"):
  print(i, os.path.isdir(i))
  if os.path.isdir(i):
    print(os.listdir())



print("parent", os.listdir("../../"))
