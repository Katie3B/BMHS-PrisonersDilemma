####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'RANKED' # Only 10 chars displayed.
strategy_name = 'The Best Strategy'
strategy_description = 'Our strategy is fairly simple. We based our code off of others past moves to gain the most points and lose the least.'
    
def move(my_history, their_history, my_score, their_score):
    if my_score <= 0:
        return 'b'
    elif their_history[-1] == 'b':
        return 'c'
    elif their_history[-1] == 'c':
        return 'b'
    elif my_score > 0:
        return 'c'
    else:
        return 'b'

        
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    

    
