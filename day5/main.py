"""
Part 1

I need to determine if the specific value is inclusive in the range and if yes and mark as fresh
Loop thru the range and print into hash map to check whether if ift's in that range?
"""
  
def part_1():
  fresh = 0
  ranges = []
  with open('ranges.txt', "r") as f:
      r = f.read().split('\n')
      for i in r:
        nums = i.split('-')
        ranges.append([int(nums[0]),int(nums[1])])

  with open("input.txt", "r") as f1:
    nums = f1.read().split('\n')
    duplicates = {}
    for i in nums:
      num = int(i)
      for range in ranges:
        if num >= range[0] and num <= range[1] and num not in duplicates:
          duplicates[num] = num
          fresh += 1

  print(fresh)

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