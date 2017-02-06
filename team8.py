####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Guambabwe' # Only 10 chars displayed.
strategy_name = 'Blitzkrieg'
strategy_description = 'Destroying the other teams with full force.'


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
   
    '''first five rounds'''
    if my_history == '': # This block will add variables and initialize their values for the first turn
        number_of_turns = 0
        my_score = 0
        enemy_betray_streak = 0
        enemy_collude_streak = 0
        
    if their_history == 'b': #Adds the streak function
        enemy_betray_streak += 1
        enemy_collude_streak = 0
        
    if their_history == 'c':
        enemy_collude_streak += 1
        enemy_betray_streak = 0
        
    if (number_of_turns % 5 == 0):
        rando_choice = random.randint(1,2)
        if rando_choice == 1:
            return 'b'
        elif rando_choice == 2:
            return 'c'
        else:
            return 'b'
    elif their_history == 'b' and enemy_betray_streak > 2:
        number_of_turns += 1
        return 'b'
    elif their_history == 'c' and enemy_collude_streak > 3:
        number_of_turns += 1
        return 'b'
    else:
        number_of_turns += 1
        return 'b' 
        
        
        
    if number_of_turns == 1 or number_of_turns == 2: #First five turns
        number_of_turns +=1
        return 'b'
    elif number_of_turns == 3 or number_of_turns == 4:
        number_of_turns += 1
        return 'c'
    if their_history == '':
        number_of_turns += 1
        return 'b'
        
    
        
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
