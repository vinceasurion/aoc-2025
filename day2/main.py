# Find the sequence of digit that repeated twice
# Part 1
# with open("input.txt", "r") as f:
#     str = f.read().split(',')
#     seq = []
#     for ranges in str:
#         start, end = map(int, ranges.split('-'))
#         for num in range(start, end + 1):
#           s = list("{0}".format(num))
#           size = len(s)
#           half = int(size / 2)
#           if s[half:] == s[:half]:
#              seq.append(num)
#     print(sum(seq))

# Part 2
# At least 2 consecutive same digits
with open("input.txt", "r") as f:
    ranges_list = f.read().split(',')
    seq = []
    for ranges in ranges_list:
        start, end = map(int, ranges.split('-'))
        for num in range(start, end + 1):
            s = str(num)
            is_repeating = False
            
            # Check if the number is made of a repeating pattern
            length = len(s)
            
            print(length // 2)
            # Try all possible pattern lengths (from 1 to half the string length)
            for pattern_len in range(1, length // 2 + 1):
                if length % pattern_len == 0:  # Length must be divisible by pattern length
                    pattern = s[:pattern_len]
                    repetitions = length // pattern_len
                    
                    # Check if repeating the pattern gives us the full number
                    if pattern * repetitions == s and repetitions >= 2:
                        is_repeating = True
                        break
            
            if is_repeating:
                seq.append(num)
    
    
    print(f"Found {seq} numbers with repeated digits")
    print(f"Sum: {sum(seq)}")
            # while tmp 
            # if tmp == 0:
            #    tmp = s[i]
            # elif tmp == s[i]
            # print(s[i])
          # print(str)
            #  if num[i] == tmp:
            #     print(num[i])
            #  tmp = num[i]
            #  print(num[i])
          # size = len(s)
          # half = int(size / 2)
          # if s[half:] == s[:half]:
          #    seq.append(num)
    # print(sum(seq))
    # print(hash)