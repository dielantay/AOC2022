f = open("C:\\Users\\Admin\\Desktop\\coding tryout\\Day 1\\day1 AOC dataset.txt", "r")
dataset = f.read().split("\n\n")

newList = []

for x in dataset:
     sum_of_group = 0

     b = x.split("\n")

     for a in b:
        sum_of_group += int(a)

     newList.append(sum_of_group)  
      
finalList = max(newList)
print(finalList)     






