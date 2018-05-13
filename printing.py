from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
file_name = 'game_stat.txt'
print(count_games(file_name))
print(decide(file_name, '2012'))
print(get_latest(file_name))
print(count_by_genre(file_name, 'RPG'))
print(get_line_number_by_title(file_name, 'Terraria'))
# Printing functions