team_name = 'Matt and Wyatt' # Only 10 chars displayed.
strategy_name = 'Hope for the best'
strategy_description = 'whatever they dont do'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if(their_history != ""):
        theirLast = their_history[len(their_history) - 1]
        
        
        if(theirLast == "b"):
            return "c"
        else:
            return "b"
    else:
        return "c"
    
    