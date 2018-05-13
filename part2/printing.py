import reports

file_name = 'game_stat.txt'
title = 'StarCraft'

print(reports.get_most_played(file_name))
print(reports.sum_sold(file_name))
print(reports.get_selling_avg(file_name))
print(reports.count_longest_title(file_name))
print(reports.get_date_avg(file_name))
print(reports.get_game(file_name, title))
# Printing functions
