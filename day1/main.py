# A position starts with L and R tells the rotation.

# - You turn Left you moved to a lower number
# - You turn Right you moved to a higher number
# - The rotation has a distance value where determine how many clicks you move in that direction.
# If the dial were pointing at 11 and the rotation is R8,
#                                ^   -   -   -   -   -   -   -   ^
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# 50 51 52 54 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76

# The dial starts at point by 50

# The dial is circle if a dial left move click left 1, it moves to 99

# You need to determine how many clicks the dial moved to zero after following a list of rotations.
dialStarts = 50
count = 0

with open("input.txt", "r") as f:
    for line in f:
        str = line.strip()
        direction = str[0]
        distance = int(str[1:])
        
        # Check each position during the rotation
        for step in range(1, distance + 1):
            if direction == 'L':
                position = (dialStarts - step) % 100
            else:  # direction == 'R'
                position = (dialStarts + step) % 100
            
            if position == 0:
                count += 1
                print(f"Crossed zero at step {step} during {str}")
        
        # Update final position
        if direction == 'L':
            point = (dialStarts - distance) % 100
        else:  # direction == 'R'
            point = (dialStarts + distance) % 100
        
        print(f"Initial dial starts {dialStarts} dial moved to {point} by {str}")
        dialStarts = point

print(f"The dial moved to zero {count} times.")