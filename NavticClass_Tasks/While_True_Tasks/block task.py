blocks = int(input("Enter the number of blocks: "))
layer=1
usedblock=0
while blocks>=usedblock+layer:
      usedblock=usedblock+layer
      layer+=1

print("The height of the pyramid:", layer-1)
