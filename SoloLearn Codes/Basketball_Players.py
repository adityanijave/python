# Statement :
'''
players_heights = [180,172,178,185,190,195,192,200,210,190]
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.
'''

# code :
players_heights = [180,172,178,185,190,195,192,200,210,190]

sum_of_total_players_height = 0
for players_height in players_heights:
    sum_of_total_players_height += players_height
print(f"The SUM of players height is {sum_of_total_players_height}")

N = len(players_heights)
print(f"The size of the players height dataset is {N}")

mean = sum_of_total_players_height / N
print(f"The Value of MEAN is {mean}")

for_variance = 0
for players_height in players_heights:
    as_required_fig = (players_height - mean)**2
    for_variance += as_required_fig

variance = for_variance / (N-1)
print(f"The value of Variance is {variance}")

SD = variance**0.5
print(f"The value of Standard Deviation is {SD}")

for_range = []
lower_limit = mean - SD
print(f"The lower limit is {lower_limit}.")
upper_limit = mean + SD
print(f"The upper limit is {upper_limit}.")

for players_height in players_heights:
    if lower_limit <= players_height <= upper_limit:
        for_range.append(players_height)
print(f"The players having height in range are {for_range} ")
spread_out = len(for_range)
print(f"The SD is spread out to {spread_out} elements in dataset.")
