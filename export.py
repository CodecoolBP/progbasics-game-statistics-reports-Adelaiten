from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title

answers = [count_games(file_name), decide(file_name, year),get_latest(file_name),count_by_genre(file_name, genre), get_line_number_by_title(file_name, title)]

with open(export_file, 'w') as export:
    for answer in answers:
        export.write(str(answer) + '\n')

# Export functions
