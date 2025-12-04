# Part 1
# You cannot re arrange the joltage
# Batteries are arranged into banks; each line of digits in your input
# Exactly two batteries

def joltage_1():
  with open("input.txt", "r") as f:
    batteries = f.read().split('\n')
    jol = []
    for i in range(0, len(batteries)):
      hash = {}
      battery = list(batteries[i])
      for j in range(0, len(battery)):
        for k in range(j + 1, len(battery)):
          kv = battery[j] + battery[k]
          if kv not in hash:
            hash[kv] = int(kv)
      jol.append(max(hash, key=hash.get))
    print(sum(int(val) for val in jol))

# Part 2
# Exactly 12 batteries
def joltage_2():
  with open("input.txt", "r") as f:
    batteries = f.read().split('\n')
    jol = []
    for i in range(0, len(batteries)):
      items = list(batteries[i])
      n = len(items)
      k = 12
      stack = []
      removals_left = n - k
      for digits in items:
        while stack and removals_left > 0 and stack[-1] < digits:
          stack.pop()
          removals_left -= 1
        stack.append(digits)
      jol.append(int(''.join(stack[:12])))
    print(sum(jol))

if __name__ == "__main__":
  joltage_2()