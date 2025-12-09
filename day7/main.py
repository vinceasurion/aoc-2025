
from typing import List, Set

"""
Part 1

The tachyon beams always move downward. 
It pass freely through empty space

"""
def part_1():
  with open("input.txt", "r") as f:
    data = f.read().strip().split('\n')
    grid = []
    for row in data:
      grid.append(list(row))

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # find starting column (S) on the top row
    top = grid[0]
    try:
        start_col = top.index('S')
    except ValueError:
        raise ValueError("No 'S' found on the first row")

    # set of columns that currently have at least one beam
    active: Set[int] = {start_col}
    print(active)
    splits = 0

    # process each row from row 0 down to last row-1 (beam moves to next row)
    for r in range(rows):
        next_active: Set[int] = set()

        for c in active:
            # beam at (r, c)
            # if outside bounds skip
            if c < 0 or c >= cols:
                continue

            cell = grid[r][c]

            if cell == '^':
                # beam hits a splitter: original beam stops, counts as one split,
                # and two new beams start on next row at columns c-1 and c+1
                splits += 1
                left = c - 1
                right = c + 1
                # Only add if they are inside the grid horizontally and next row exists
                if r + 1 < rows:
                    if 0 <= left < cols:
                        next_active.add(left)
                    if 0 <= right < cols:
                        next_active.add(right)
                # beam does NOT continue straight down from this cell
            else:
                # not a splitter ('.' or 'S' or other) -> just go straight down (same column)
                if r + 1 < rows:
                    next_active.add(c)

        active = next_active

        # early exit: if there are no active beams left, we can stop
        if not active:
            break

    print(splits)

if __name__ == "__main__":
  part_1()