"""
Part 1

I need to determine if the specific value is inclusive in the range and if yes and mark as fresh
Loop thru the range and print into hash map to check whether if ift's in that range?
"""
  
def part_1():
  fresh = 0
  ranges = []
  with open('ranges.txt', "r") as f:
      for line in f:
        start, end = map(int, line.strip().split('-'))
        ranges.append((start, end))

  fresh_ids = set()
  with open("input.txt", "r") as f:
    for line in f:
      num = int(line.strip())
      for start, end in ranges:
         if start <= num <= end:
           fresh_ids.add(num) 
  
  print(len(fresh_ids))

"""
Part 2
How many Ingredients ids can be fit in in the ranges..

Solution:

Is to create a range and insert each Ingredient IDs into the hash
"""
def part_2():
    ranges = []
    with open('ranges.txt', "r") as f:
        for line in f:
            start, end = map(int, line.strip().split('-'))
            ranges.append((start, end))
    
    ranges.sort()
    merged = [ranges[0]]
    
    for start, end in ranges[1:]:
        if start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    sum = 0
    for start, end in merged:
      sum += ((end - start) + 1)

    print(sum)

if __name__ == '__main__':
  part_2()