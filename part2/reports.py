def get_most_played(file_name):
    splitted_collection = []
    most_played_game = []
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))
    for collection in splitted_collection:
        if not most_played_game:
            most_played_game.append(collection[0])
            most_played_game.append(collection[1])
        if float(collection[1]) > float(most_played_game[1]):
            most_played_game = []
            most_played_game.append(collection[0])
            most_played_game.append(collection[1])
    return most_played_game[0]


def sum_sold(file_name):
    splitted_collection = []
    sum_sold_games = 0
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))
    for collection in splitted_collection:
        sum_sold_games += float(collection[1])

    return sum_sold_games


def get_selling_avg(file_name):
    games_sum = 0
    sum_sold_games = 0
    splitted_collection = []
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        games_sum += 1
        sum_sold_games += float(collection[1])

    sold_average = sum_sold_games / games_sum

    return sold_average


def count_longest_title(file_name):
    longest_title = ''
    splitted_collection = []

    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        if not longest_title:
            longest_title = collection[0]
        if len(collection[0]) > len(longest_title):
            longest_title = collection[0]
    return len(longest_title)


def get_date_avg(file_name):
    games_sum = 0
    years_sum = 0
    splitted_collection = []
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        games_sum += 1
        years_sum += int(collection[2])

    years_average = years_sum / games_sum
    years_average += 1
    temp = str(years_average)
    dot = temp.find(".")
    years_average = temp[0:dot]

    return int(years_average)


def get_game(file_name, title):
    splitted_collection = []
    with open(file_name) as gamesFile:
        lines = gamesFile.readlines()

    for collection in lines:
        splitted_collection.append(collection.split('\t'))

    for collection in splitted_collection:
        temp = collection[-1]
        temp = temp[0:-1]
        collection[-1] = temp
        if title in collection:
            properties_collection = collection
    
    properties_collection[1] = float(properties_collection[1])
    properties_collection[2] = int(properties_collection[2])

    try:
        return properties_collection

    except UnboundLocalError:
        print("There is no such game as " + title)


# Report functions
