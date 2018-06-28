import pdb
def game_dict():
    game_dictionary = {
        'home': {
        'team_name': 'Brooklyn Nets',
        'colors':['Black', 'White'],
        'players': {
            'Alan Anderson': {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12,
                                'assists': 12, 'steals':3, 'blocks':1, 'slam_dunks':1},
            'Reggie Evans': {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12,
                                'assists': 12, 'steals':12, 'blocks':12, 'slam_dunks':7},
            'Brook Lopez': {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19,
                                'assists': 10, 'steals':3, 'blocks':1, 'slam_dunks':15},
            'Mason Plumlee': {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12,
                                'assists': 6, 'steals':3, 'blocks':8, 'slam_dunks':5},
            'Jason Terry': {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2,
                                'assists': 2, 'steals':4, 'blocks':11, 'slam_dunks':1}
                    }
                },
        'away': {
            'team_name': 'Charlotte Hornets',
            'colors':['Turquoise', 'Purple'],
            'players': {
                'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1,
                                'assists': 1, 'steals': 2, 'blocks': 7, 'slam dunks': 2},
                'Bismack Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4,
                                'assists': 7, 'steals': 7, 'blocks': 15, 'slam dunks': 10},
                'DeSagna Diop':{'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12,
                                'assists': 12, 'steals': 4, 'blocks': 5, 'slam dunks': 5},
                'Ben Gordon':{'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3,
                                'assists': 2, 'steals': 1, 'blocks': 1, 'slam dunks': 0},
                'Brendan Haywood':{'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12,
                                'assists': 12, 'steals': 22, 'blocks': 5, 'slam dunks': 12}
                        }
                }
            }
    return game_dictionary

game_dictionary = game_dict()

# creates list containing dictionaries for each team
teams = [v['players'] for k,v in game_dictionary.items()]

# creats one dictionary with all players, not separated by teams
players = {}
for team in teams:
    players.update(team)

# Raise 'must pass through a string' if not type(name) == str
# Coerce
# Act
# Return

def num_points_scored(player_name):
    return players[player_name]['points']
    ##### ALT METHOD ####
        # points_scored = 0
        # for player in players.keys():
        #     if player == player_name:
        #         points_scored += players[player]['points']
        #return points
#print(num_points_scored('Ben Gordon'))

def shoe_size(player_name):
    return players[player_name]['shoe']
    ##### ALT METHOD ####
        # shoe_size = 0
        # for player in players.keys():
        #     if player == player_name:
        #         shoe_size += players[player]['shoe']
        # return shoe_size
#print(shoe_size('Ben Gordon'))

def team_colors(team_name):
    return [color for k,v in game_dictionary.items() if v['team_name'] == team_name for color in v['colors']]
            # team_colors = [['Turquoise', Purple]]
        # could also use the flattened_colors loop to remove the outer list
        # flattened_colors = [color for colors_pair in team_colors for color in colors_pair]
    ##### ALT METHOD ####
        # team_colors = []
        # for location in game_dictionary.keys():
        #     if game_dictionary[location]['team_name'] == team_name:
        #         team_colors.extend(game_dictionary[location]['colors'])
        # return team_colors
#print(team_colors('Charlotte Hornets'))

def team_names():
    return [v['team_name'] for k,v in game_dictionary.items()]
    ##### ALT METHOD ####
        # team_names = []
        # for location in game_dictionary.keys():
        #     team_names.append(game_dictionary[location]['team_name'])
        # return team_names
#print(team_names())

def player_numbers(team_name):
    player_numbers = []
    for location in game_dictionary.keys():
        if (game_dictionary[location]['team_name']) == team_name:
            for player in (game_dictionary[location]['players']):
                player_numbers.append(players[player]['number'])
    return player_numbers
#print(player_numbers('Charlotte Hornets'))

def player_stats(player_name):
    return players[player_name]
#print(player_stats('Ben Gordon'))

def big_shoe_rebounds():
    shoe_list = [v['shoe'] for k, v in players.items()]
    biggest_shoe = max(shoe_list)
    player_largest_shoe = [k for k, v in players.items() if v['shoe'] == biggest_shoe]
    largest_shoe_rebound = [v['rebounds'] for k, v in players.items() if v['shoe'] == biggest_shoe]
    player_largest_shoe_rebound = list(zip(player_largest_shoe, largest_shoe_rebound))
    return player_largest_shoe_rebound
#print(big_shoe_rebounds())

def player_with_highest_stat(stat):
    selected_stat = [v[stat] for k,v in players.items()]
    largest_stat = max(selected_stat)
    player_with_max_stat = [k for k,v in players.items() if v[stat] == largest_stat]
    return player_with_max_stat
#print(player_with_highest_stat('steals'))

def most_points_scored():
    return player_with_highest_stat('points')
#print(most_points_scored())

def winning_team():
    team_dict = game_dictionary
    home_info = game_dictionary['home']['players']
    away_info = game_dictionary['away']['players']
    home_points = [v['points'] for k,v in home_info.items()]
    away_points = [v['points'] for k,v in away_info.items()]
    sum_home_points = sum(home_points)
    sum_away_points = sum(away_points)
    if sum_home_points > sum_away_points:
        return game_dictionary['home']['team_name']
    else:
        return game_dictionary['away']['team_name']
#print(winning_team())

def player_with_longest_name():
    player_names = [k for k, v in players.items()]
    name_length = []
    longest_named_player = []
    for name in player_names:
        length = len(name)
        name_length.append(length)
    for name in player_names:
        if len(name) == max(name_length):
            longest_named_player.append(name)
    #longest_named_player.append(max(name_length))
    return longest_named_player
#print(player_with_longest_name())

def long_name_steals_a_ton():
    for player in player_with_highest_stat('steals'):
        if player in player_with_longest_name():
            return True
#print(long_name_steals_a_ton())

# def good_practices():
#   for location, team_stats in game_dict().items():
#     # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
#     import pdb; pdb.set_trace()
#     for stats, data in team_stats.items():
#         # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
#         import pdb; pdb.set_trace()
#         # what is 'data' at each level of the for loop block? when will we be able to iterate through a list?
#         # When would the following line of code break?
#         for item in data:
#             print(item)
#
# good_practices()
