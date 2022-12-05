f = open("C:\\Users\\Admin\\Desktop\\coding tryout\\Day 1\\day1 AOC dataset.txt", "r")
dataset = f.read().split("\n\n")

newList = []

for x in dataset:
     sum_of_group = 0

     b = x.split("\n")

     for a in b:
        sum_of_group += int(a)

     newList.append(sum_of_group)  
      
newList.sort(reverse = True)

def my_sum(*args):
    total = 0
    for val in args:
        total += val
    print(total)

my_sum(newList[0], newList[1], newList[2])
 