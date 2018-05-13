def count_games(file_name):
    #counting number of games in file_name
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    number_of_games = 0

    for collection in lines:
        number_of_games += 1

    return number_of_games


def decide(file_name, year):
    #check if year in file_name
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    equal = 0

    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            try:
                if int(item) > 1900:
                    if int(item) == year:
                        equal += 1
            except:
                pass

    if equal > 0:
        return True
    else:
        return False


def get_latest(file_name):
    #get latest developed game
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    game_title_year = []

    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            try:
                if int(item) > 1900:
                    if not game_title_year:
                        game_title_year.append(splitted_collection[0])
                        game_title_year.append(splitted_collection[2])
                    elif int(splitted_collection[2]) > int(game_title_year[1]):
                        game_title_year = []
                        game_title_year.append(splitted_collection[0])
                        game_title_year.append(splitted_collection[2])
                    elif int(splitted_collection[2]) == int(game_title_year[1]):
                        continue
            except:
                pass

    game = game_title_year[0]

    return game


def count_by_genre(file_name, genre):
    #count games by genre
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    games_genre = 0

    for collection in lines:
        splitted_collection = collection.split('\t')
        for item in splitted_collection:
            if item.lower() == genre.lower():
                games_genre += 1
            else:
                continue

    return games_genre

def get_line_number_by_title(file_name, title):
    #looking for game title's line in file_name
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    loop_line = 0
    splitted_collection = []
    title_and_number = []
    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        loop_line += 1

        for item in collection:
            if item.lower() == title.lower():
                title_and_number.append(title)
                title_and_number.append(loop_line)

    try:
        return title_and_number[1]
    except IndexError:
        pass




# Report functions
