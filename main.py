import os
print("root", os.listdir("/data"))
print("root/repository", os.listdir("/data/repository"))


print("parent", os.listdir("../"))

for i in os.listdir("../"):
  if os.path.isdir(i):
    print(os.listdir())



