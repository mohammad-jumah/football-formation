import random
position = ["GK", "Left Back", "Centre Back", "Right Back", "Centre1", "Centre2", "Striker", "Forward" ]
random.shuffle(position)
input_string = input("Enter players ")
player_list = input_string.split(" ")
for name in player_list:
    print(name)
for name in position:
    print(position)
