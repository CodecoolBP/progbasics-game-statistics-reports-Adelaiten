def open_function(file_name):
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()
    return lines


def splitting_lines(lines):
    splitted_collection = []
    for collection in lines:
        splitted_collection.append(collection.split('\t'))
    return splitted_collection


def count_games(file_name):
    #counting number of games in file_name
    lines = open_function(file_name)
    number_of_games = 0

    for collection in lines:
        number_of_games += 1

    return number_of_games


def decide(file_name, year):
    #check if year in file_name
    lines = open_function(file_name)
    equal = 0
   
    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            try:
                if int(item) > 1900 and int(item) == year:
                        equal += 1
            except:
                print("There is no game made in " + str(year))

    if equal > 0:
        return True
    else:
        return False


def get_latest(file_name):
    #get latest developed game
    lines = open_function(file_name)
    game_title_year = []
    FILE_NAME_INDEX = 0
    FILE_YEAR_INDEX = 2
    LIST_YEAR_INDEX = 1
    LIST_NAME_INDEX = 0

    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            try:
                if int(item) > 1900:
                    if not game_title_year:
                        game_title_year.append(splitted_collection[FILE_NAME_INDEX])
                        game_title_year.append(splitted_collection[FILE_YEAR_INDEX])
                    elif int(splitted_collection[FILE_YEAR_INDEX]) > int(game_title_year[LIST_YEAR_INDEX]):
                        game_title_year = []
                        game_title_year.append(splitted_collection[FILE_NAME_INDEX])
                        game_title_year.append(splitted_collection[FILE_YEAR_INDEX])

            except:     # ???
                pass

    game = game_title_year[FILE_NAME_INDEX]

    return game


def count_by_genre(file_name, genre):
    #count games by genre
    lines = open_function(file_name)
    games_genre = 0

    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            if item.lower() == genre.lower():
                games_genre += 1

    return games_genre

def get_line_number_by_title(file_name, title):
    #looking for game title's line in file_name
    lines = open_function(file_name)
    loop_line = 0
    splitted_collection = []
    title_and_number = []
    LINE_INDEX = 1
    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        loop_line += 1

        for item in collection:
            if item.lower() == title.lower():
                title_and_number.append(title)
                title_and_number.append(loop_line)
    if title_and_number:
        return title_and_number[LINE_INDEX]
    else:
        print("There is no such game as " + title)





# Report functions
