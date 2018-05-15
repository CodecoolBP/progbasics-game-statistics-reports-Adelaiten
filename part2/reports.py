def open_function(file_name):
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()
    return lines

def splitting_lines(lines):
    splitted_collection = []
    for collection in lines:
        splitted_collection.append(collection.split('\t'))
    return splitted_collection


def get_most_played(file_name):

    most_played_game = []
    lines = open_function(file_name)
    splitted_collection = splitting_lines(lines)
    NAME_INDEX = 0
    SALES_INDEX = 1
        
    
    for collection in splitted_collection:
        try:
            if float(collection[1]) > float(most_played_game[1]):
                most_played_game = []
                most_played_game.append(collection[NAME_INDEX])
                most_played_game.append(collection[SALES_INDEX])
        except IndexError:
                most_played_game.append(collection[NAME_INDEX])
                most_played_game.append(collection[SALES_INDEX])
    return most_played_game[0]


def sum_sold(file_name):
    sum_sold_games = 0
    lines = open_function(file_name)
    splitted_collection = splitting_lines(lines)
    SALES_INDEX = 1

    for collection in splitted_collection:
        sum_sold_games += float(collection[SALES_INDEX])

    return sum_sold_games


def get_selling_avg(file_name):
    games_sum = 0
    sum_sold_games = 0
    SALES_INDEX = 1
    lines = open_function(file_name)
    splitted_collection = splitting_lines(lines)

    for collection in splitted_collection:
        games_sum += 1
        sum_sold_games += float(collection[SALES_INDEX])

    sold_average = sum_sold_games / games_sum

    return sold_average


def count_longest_title(file_name):
    longest_title = ''
    lines = open_function(file_name)
    splitted_collection = splitting_lines(lines)

    for collection in splitted_collection:
        if not longest_title: # or
            longest_title = collection[0]
        if len(collection[0]) > len(longest_title):
            longest_title = collection[0]
    return len(longest_title)


def get_date_avg(file_name):
    games_sum = 0
    years_sum = 0
    lines = open_function(file_name)
    YEAR_INDEX = 2
    splitted_collection = splitting_lines(lines)

    for collection in splitted_collection:
        games_sum += 1
        years_sum += int(collection[YEAR_INDEX])

    years_average = years_sum // games_sum
    years_average += 1
   
    return int(years_average)


def get_game(file_name, title):
    lines = open_function(file_name)
    FIRST_INDEX = 1
    SECOND_INDEX = 2
    splitted_collection = splitting_lines(lines)

    for collection in splitted_collection:
        temp_collection = collection[-1]
        temp_collection = temp_collection[0:-1]
        collection[-1] = temp_collection
        if title in collection:
            properties_collection = collection

    properties_collection[1] = float(properties_collection[FIRST_INDEX])
    properties_collection[2] = int(properties_collection[SECOND_INDEX])

    
    return properties_collection

  

# Report functions
