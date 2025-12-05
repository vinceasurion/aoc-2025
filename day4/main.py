"""
Part 1

Explanation
This is 2d grid array where you need to find a roll of paper fewer than four 
rolls of paper in the eight adjacent position.

/  /  /
/  /x/ /
/  /  /
"""

def get_adjacent_input(grid, r, c):
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    num_adj = 0

    for rX in x:
      for cY in y:
        row, col = r+rX, c+cY

        if rX == 0 and cY == 0:
          continue
        if row < 0 or row >= len(grid):
          continue
        if col < 0 or col >= len(grid[row]):
          continue

        if grid[row][col] == '@':
          num_adj += 1

    return num_adj

def part_1():
  with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]
    total = 0
    for row in range(len(grid)):
      for col in range(len(grid[row])):
        if grid[row][col] == '@' and get_adjacent_input(grid, row, col) < 4:
          total += 1
          
    print(total)

"""

Part 2
We need to updated the identified forklift and marked that as removed.
Update the grid and marked as identified
"""
def part_2():
  with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]
    total_removed = 0

    # Keep removing until no more can be removed
    while True:
      to_remove = []
      for row in range(len(grid)):
        for col in range(len(grid[row])):
          if grid[row][col] == '@' and get_adjacent_input(grid, row, col) < 4:
            to_remove.append((row, col))
      
      if not to_remove:
        break

      for row, col in to_remove:
        grid[row][col] = '.'

      total_removed += len(to_remove)
    print(f"Total remove: {total_removed}")
if __name__ == '__main__':
  part_2()