"""
Part 1 

Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. 
The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:
123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
"""
def part_1():
  m = {}
  with open("input.txt", "r") as f:
    for line in f:
      for i, ch in enumerate([x for x in line.strip().split(' ') if x.strip()]):
        m.setdefault(i, []).append(ch)

  total = 0
  for v in m.values():
    if v[-1] == '+':
      total += sum(int(x) for x in v[:-1])
    elif v[-1] == '*':
      product = 1
      for i in v[:-1]:
        product *= int(i)
      total += product
  print(total)
  print(m)

"""

Part 2

The problem now is column is arranged right-to-left. Each number is given in its own column, 
with the most significant digit at the top and the least significant digit at the bottom. 
(Problems are still separated with a column consisting only of spaces, 
and the symbol at the bottom of the problem is still the operator to use.)

Read from right-to-left and top most to the bottom

"""
def part_2():
  with open("input.txt", "r") as f:
    lines = [line.rstrip('\n') for line in f]
  
  max_len = max(len(line) for line in lines)
  
  m, ans = [], []
  for col_idx in range(max_len - 1, -1, -1):
    column = []
    for row in lines:
      if col_idx < len(row) and row[col_idx] != ' ' and row[col_idx] != '+' and row[col_idx] != '*':
        column.append(row[col_idx])
      if row[col_idx] == '+' or row[col_idx] == '*':
        column.append(row[col_idx])

    if len(column) > 0:  # Skip empty columns
      if column[-1] == '+':
        m.append(int("".join(column[:-1])))
        ans.append(sum(m))
        m = []
      elif column[-1] == '*':
        m.append(int("".join(column[:-1])))
        product = 1
        for num in m:
          product *= num
        ans.append(product)
        m = []
      else:
        m.append(int("".join(column)))

  print(sum(ans))

if __name__ == "__main__":
  part_2()