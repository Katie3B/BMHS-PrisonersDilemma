####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team6' # Only 10 chars displayed.
strategy_name = 'Team6 strategy'
strategy_description = 'How does this strategy decide?'

def move(my_history, their_history, my_score, their_score):
    theirLast = their_history[len(their_history) - 1]
    if(theirLast == "b"):
        return "c"
    else: 
            return "b"