

import random

dungeon1 = {
    'treasure' : [1], # Room 1 contains treasure
    'adventurer': 0, # The adventurer starts in room 0
    'troll': 2, # The troll starts in room 2
    'network': [[1], #Room zero connects to room 1
                [0,2], #Room one connects to rooms 0 and 2
                [1] ] #Room 2 connects to room 1
}

def random_move(network, current_loc):
    targets=network[current_loc]
    return random.choice(targets)

def update_dungeon(dungeon):
    dungeon['adventurer']=random_move(dungeon['network'], dungeon['adventurer'])
    dungeon['troll']=random_move(dungeon['network'], dungeon['troll'])

update_dungeon(dungeon1)

{'treasure': [1], 'adventurer': 1, 'troll': 1, 'network': [[1], [0, 2], [1]]}


def outcome(dungeon):
    if dungeon['adventurer']==dungeon['troll']:
        return -1
    if dungeon['adventurer'] in dungeon['treasure']:
        return 1
    return 0

import copy

def run_to_result(dungeon):
    dungeon=copy.deepcopy(dungeon)
    max_steps=1000
    for _ in range(max_steps):
        result= outcome(dungeon)
        if result != 0:
            return result
        update_dungeon(dungeon)
    # don't run forever, return 0 (e.g. if there is no treasure and the troll can't reach the adventurer)
    return result

dungeon2 = {
    'treasure' : [1], # Room 1 contains treasure
    'adventurer': 0, # The adventurer starts in room 0 
    'troll': 2, # The troll starts in room 2
    'network': [[1], #Room zero connects to room 1
                [0,2], #Room one connects to rooms 0 and 2
                [1,3], #Room 2 connects to room 1 and 3
                [2]] # Room 3 connects to room 2
    
}

run_to_result(dungeon2)

def success_chance(dungeon):
    trials=10000
    successes=0
    for _ in range(trials):
        outcome = run_to_result(dungeon)
        if outcome == 1:
            successes+=1
    success_fraction = successes/trials
    return success_fraction

print(success_chance(dungeon2))
