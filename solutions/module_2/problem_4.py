def calculate_advanced_rushing_stats(rushing_dict):

    yards_per_carry = rushing_dict['rushing_yards'] / rushing_dict['rushing_attempts']

    touchdowns_per_carry = rushing_dict['rushing_touchdowns'] / rushing_dict['rushing_attempts']

    return {
        'yards_per_carry': yards_per_carry,
        'touchdowns_per_carry': touchdowns_per_carry
    }

#made up rushing stats
rushing_dict = {
    'rushing_yards': 1000,
    'rushing_touchdowns': 12,
    'rushing_attempts': 240
   }

print(
    calculate_advanced_rushing_stats(rushing_dict)
)