player_name = 'Rashaad Penny'

rushing_yds = 370

percentile_25 = 20

percentile_75 = 465

if rushing_yds > percentile_75:
    print(player_name, 'is in the 75th percentile of RBs for rushing yards.')
elif rushing_yds < percentile_75 and rushing_yds > percentile_25:
    print(player_name, 'is in the interquartile range of RBs for rushing yards.')
else:
    print(player_name, 'is in the bottom 25th percentile of RBs for rushing yards.')

