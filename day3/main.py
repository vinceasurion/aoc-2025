# Part 1
# You cannot re arrange the joltage
# Batteries are arranged into banks; each line of digits in your input
# Exactly two batteries

def joltage():
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

if __name__ == "__main__":
  joltage()