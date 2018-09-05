import os
print("root", os.listdir("/data"))
print("root/repository", os.listdir("/data/repository"))
print("in", os.listdir("/data/in"))
print("out", os.listdir("/data/out"))


print("parent", os.listdir("../"))

#for i in os.listdir("../"):
#  print(i, os.path.isdir(i))
#  if os.path.isdir(i):
#    print(os.listdir())



#print("parent", os.listdir("../../"))
