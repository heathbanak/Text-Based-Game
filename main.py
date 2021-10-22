# Heath Banak
# fix display info
# text-based game

placeholder = 'coming soon...'

# dictionary of rooms
rooms = {
    'Cotton Candy Stand': {'North': 'Ticket Booth', 'West': 'Midway'},
    'Darts': {'South': 'Tilt-A-Whirl', 'East': 'Midway'},
    'Entrance': {'North': 'Lemonade Stand'},
    'Ferris Wheel': {'West': 'Fun House'},
    'Fun House': {'South': 'Midway', 'East': 'Ferris Wheel', 'West': 'Pirate Ship'},
    'Lemonade Stand': {'North': 'Midway', 'South': 'Entrance', 'West': 'Tilt-A-Whirl'},
    'Midway': {'North': 'Fun House', 'South': 'Lemonade Stand', 'East': 'Cotton Candy Stand', 'West': 'Darts'},
    'Pirate Ship': {'East': 'Fun House'},
    'Ticket Booth': {'South': 'Cotton Candy Stand'},
    'Tilt-A-Whirl': {'North': 'Darts', 'East': 'Lemonade Stand'}
}

# dictionary of items
item_locations = {
    'Cotton Candy Stand': 'Cotton Candy',
    'Darts': 'Dart',
    'Entrance': 'Hammer',
    'Fun House': 'Mirror',
    'Lemonade Stand': 'Lemonade',
    'Pirate Ship': 'Sword',
    'Ticket Booth': 'Keys',
    'Tilt-A-Whirl': 'Grease'
}

boundaries = {
    'Cotton Candy Stand': {'South': 'milk jugs', 'East': 'trash can'},
    'Darts': {'North': 'fish bowl', 'West': 'bumper cars'},
    'Entrance': {'South': 'road', 'East': 'road', 'West': 'road'},
    'Ferris Wheel': {'North': 'crane game', 'South': 'balloons', 'East': 'lake'},
    'Fun House': {'North': 'wall of mirrors'},
    'Lemonade Stand': {'East': 'petting zoo'},
    'Pirate Ship': {'North': 'meadow', 'South': 'basketball', 'West': 'road'},
    'Ticket Booth': {'North': 'parade', 'East': 'picnic grounds', 'West': 'restrooms'},
    'Tilt-A-Whirl': {'South': 'coaster', 'West': 'residential area'}
}

lost_game_outcomes = {
    'no_food': '\nYou are so tired from your efforts that you fall flat on your face in front of Nooli.',
    'no_dart': 'Your lack of weapon gives Nooli a boost of confidence. They sidestep you easily and you crash face'
               'first into the Ferris Wheel.',
    'no_keys': 'While Nooli is distracted with their arm, you try to fix the Ferris Wheel. Without the CCK, you look '
               'for another way to access the controls. This gives Nooli a chance to recover, sneak up behind you, '
               'and knock you out with a well-placed punch.',
    'no_sword': 'Without any way to cut your friends free, you look around for something sharp. This gives Nooli a '
               'chance to recover, sneak up behind you, and knock you out with a well-placed punch.',
    'no_drink': 'Your pals are in rough shape after being tied up for so long with no food or water. They can barely '
                'pick themselves up, and don\'t have the strength to warn you when Nooli sneaks up behind you and '
                'knocks you out with a well-placed punch.',
    'no_mirror': 'You turn around to see Nooli running straight towards you. You don\'t have time to move and they '
                 'crash into you, knocking you out in the process.',
    'no_grease': 'Nooli picks up some broken glass from the mirror and lunges at you. You start bleeding and while '
                'the Carnies tend to your wounds, Nooli sneaks out the door and runs to freedom!',
    'no_hammer': 'Coated in grease, Nooli gets up and runs towards the door. The carnies all try to grab Nooli but '
                'the grease makes them impossible to stop. Nooli runs to freedom!'
}

win_game_outcomes = {
    'has_food': '\nFull of energy from the cotton candy, you rush towards Nooli in a blind rage.',
    'has_dart': 'When Nooli tries to sidestep you, you throw a dart at them, hitting them in the arm.',
    'has_keys': 'While Nooli is distracted with their arm, you use the CCK to unlock the Ferris Wheel controls '
                'and lower the carnies to safety.',
    'has_sword': 'You quickly use the sword to cut your friends loose.',
    'has_drink': 'You give the carnies lemonade to help revive them -- Nooli hasn\'t given them any food\n'
                 'or water since he tied them up. As they gain their strength back, they give you a signal\n'
                 'that they\'re ready to help you take down Nooli.',
    'has_mirror': 'You turn around to see Nooli running straight towards you. You quickly hold the\n'
                  'carnival mirror up in front of you and Nooli crashes into it.',
    'has_grease': 'Nooli stumbles back from the shattered mirror and one of the carnies pours\n'
                  'the grease on the ground behind Nooli, causing them to slip.',
    'has_hammer': 'As Nooli falls, another carny hits Nooli in the head with the hammer, knocking him out.'
}

possible_moves = ['North', 'South', 'East', 'West']
current_room = 'Midway'
inventory = []
rooms_reached = []


def get_name():
    print('Welcome to [country carnival madness castle and friends].')
    print('Type \'quit\' at any time to quit.\n')

    name = input('Please enter your name: ').title()
    return name


def display_intro(name):
    print('\n\
       Hello, {}. Your evil twin, Nooli, has come back to town, and this time not just to steal your \
carnival--'.format(name))
    print('but your identity too! Nooli snuck in overnight, kidnapped your carnies and is holding them tied up at \
the'.center(123))
    print('top of the Ferris wheel! On top of that, Nooli got into the controls for the wheel and seems to have \
broken'.center(123))
    print('it...again. You are the only one who can save the carnival, your friends, yourself, and the world \
from'.center(123))
    print('Nooli\'s rampage.'.center(123))
    print()
    print('Luckily, you know exactly what to do.'.center(123))
    print('\n')
    print('*     *     *'.center(123))
    print('\n')
    print('Here\'s what you\'ll need:')
    print('     1) A hammer from the high striker for protection')
    print('     2) Ice cold lemonade to revitalize the carnies')
    print('     3) Cotton candy to sustain yourself')
    print('     4) The Carnival CKey (CCK) to get to the Ferris Wheel controls')
    print('     5) Grease for some repairs')
    print('     6) A carnival mirror to take down Nooli, in combination with the dart')
    print('     7) A dart to take down Nooli, in combination with the mirror')
    print('     8) A sword to cut your carny pals loose')

    print('\nGo through each area of the carnival and collect each item before you get to the Ferris wheel,')
    print('otherwise, Nooli could get away!')

    print('\nYou\'ll start at Midway. To move, enter North, South, East, or West.')
    print('Enter quit at any time to end game.')

    print('\nGood luck!')
    print('\n*     *     *\n')


def display_info(room, value=0):
    local_list = ['You are now in {}.'.format(room), '\nYou have {}.'.format(inventory), 'Enter {} to \
move,'.format(possible_moves), 'or quit to quit.']
    if value == 1:
        print('\n{}'.format(local_list[0]))
    else:
        local_copy = local_list.copy()
        local_copy.pop(0)
        print('\n'.join(local_copy))


def get_move(room):
    print('You are in {}.'.format(room))
    print('Which way would you like to go?')


def invalid_move(room):
    print('\nI don\'t know that command, try again.\n')
    display_info(room)


def wrong_way(room, move):
    print('\nYou hit a {}!'.format(boundaries[room][move]))
    display_info(room)


def move_room(room, completed_move):
    new_room = rooms[room][completed_move]
    return new_room


def empty_room(room):
    display_info(room, 1)
    print('\nThis room is empty.')
    display_info(room)
    new_move = input().title()
    return new_move


def room_contains_item(room):
    item = item_locations[room]
    # item is in inventory
    if item in inventory:
        print('\nThis room is empty.')
    # item is not in inventory
    else:
        display_info(room, 1)
        print('\nYou found the {}!'.format(item))
        print('Do you want to pick up {}? Enter Y or N'.format(item))
        choice = input().title()
        return choice


def invalid_choice():
    print('I don\'t know that command.')
    print('Enter Y or N')
    choice = input().title()
    return choice


def get_item(room):
    inventory.append(item_locations[room])
    del item_locations[room]
    display_info(room)


def lose_game():
    if 'Cotton Candy' not in inventory:
        print(lost_game_outcomes['no_food'])
    else:
        print(win_game_outcomes['has_food'])
        if 'Dart' not in inventory:
            print(lost_game_outcomes['no_dart'])
        else:
            print(win_game_outcomes['has_dart'])
            if 'Keys' not in inventory:
                print(lost_game_outcomes['no_keys'])
            else:
                print(win_game_outcomes['has_keys'])
                if 'Sword' not in inventory:
                    print(lost_game_outcomes['no_sword'])
                else:
                    print(win_game_outcomes['has_sword'])
                    if 'Lemonade' not in inventory:
                        print(lost_game_outcomes['no_drink'])
                    else:
                        print(win_game_outcomes['has_drink'])
                        if 'Mirror' not in inventory:
                            print(lost_game_outcomes['no_mirror'])
                        else:
                            print(win_game_outcomes['has_mirror'])
                            if 'Grease' not in inventory:
                                print(lost_game_outcomes['no_grease'])
                            else:
                                print(win_game_outcomes['has_grease'])
                                if 'Hammer' not in inventory:
                                    print(lost_game_outcomes['no_hammer'])
    print('\nTry to collect all items before rescuing the carnies. Nooli won\'t be able to stop you then!')


def win_game():
    for value in win_game_outcomes.values():
        print(value)
    print('You saved the carnival, your friends, and the world from Nooli!\n')
    print('Congratulations! You win!')


player_name = get_name()
# as long as player does not enter quit
if player_name != 'Quit':
    # display instructions
    display_intro(player_name)
    # prompt move to start gameplay
    get_move(current_room)
    player_move = input().title()
    # as long as player does not enter quit
    while player_move != 'Quit':
        # unknown command
        if player_move not in possible_moves:
            invalid_move(current_room)
            player_move = input().title()
        else:
            # move not available in current room
            if player_move not in rooms[current_room].keys():
                wrong_way(current_room, player_move)
                player_move = input().title()
            else:
                # player moves rooms
                current_room = move_room(current_room, player_move)
                # if player enters villain room
                if current_room == 'Ferris Wheel':
                    if len(inventory) != 8:
                        # lose game if player encounters villain without full inventory
                        # display number of items in inventory
                        if len(inventory) == 1:
                            print('\nYou collected {} item'.format(len(inventory)))
                        if len(inventory) != 1:
                            print('\nYou collected {} items'.format(len(inventory)))
                        # print appropriate story outcome based on items in inventory
                        if len(inventory) == 0:
                            print(lost_game_outcomes['no_food'])
                            print('They steal your identity and have you thrown in jail for crimes you did not commit.')
                        else:
                            lose_game()
                        player_move = 'Quit'
                    else:
                        # win game if player encounter villain with full inventory
                        win_game()
                        player_move = 'Quit'
                # room is empty
                # remove room from item_locations when item is obtained
                elif current_room not in item_locations:
                    player_move = empty_room(current_room)
                else:
                    # add item to inventory
                    collect_item = room_contains_item(current_room)
                    # as long as player does not enter quit
                    if collect_item != 'Quit':
                        # invalid choice
                        while collect_item not in ['Y', 'N', 'Quit']:
                            collect_item = invalid_choice()
                        # player enters quit
                        if collect_item == 'Quit':
                            player_move = collect_item
                        # choose to add item to inventory
                        elif collect_item == 'Y':
                            get_item(current_room)
                            player_move = input().title()
                        elif collect_item == 'N':
                            display_info(current_room)
                            player_move = input().title()
                    else:
                        player_move = collect_item
print('\nGoodbye')
