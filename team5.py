####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
# This is a change
####
import random

print ("Starting...")

team_name = 'Team 5 Ben & Dylan' # Only 10 chars displayed.
strategy_name = 'Prediction'
strategy_description = 'Guesses the opponents strategy by weighting patterns!'

#Variables
start = "c"
    
iterationAlwaysCollude = 0
weightAlwaysCollude = 0
    
iterationAlternate = 0
weightAlternate = 0

iterationOpposite = 0
weightOpposite = 0

iterationAlwaysBetray = 0
weightAlwaysBetray = 0

iterationBetrayAfter = 0
iterationBetrayAfterStart = 0
weightBettrayAfter = 0

def lastMove(history):
    return history[-1:]

def opposite(history):
    if(history == "c"):
        return "b"
    else:
        return "c"

def move(my_history, their_history, my_score, their_score):
    
    theirLast = lastMove(their_history)
    myLast = lastMove(my_history)
    
    iterations = len(their_history)
    
    global start
    
    global iterationAlwaysCollude
    global weightAlwaysCollude
    
    global iterationAlternate
    global weightAlternate

    global iterationOpposite
    global weightOpposite
    
    global iterationAlwaysBetray
    global weightAlwaysBetray
    
    global iterationBetrayAfter
    global iterationBetrayAfterStart
    global weightBettrayAfter
    
    if(their_history != ""):
        
        # Opposite
        if(theirLast == opposite(myLast)):
            iterationOpposite += 1.0
        weightOpposite = int((iterationOpposite / iterations) * 100)
                
        #Always Collude
        if(theirLast == "c"):
            iterationAlwaysCollude += 1.0
        weightAlwaysCollude = int((iterationAlwaysCollude / iterations) * 100)
        
        #AlwaysBetray
        if(theirLast == "b"):
            iterationAlwaysBetray += 1.0
        weightAlwaysBetray = int((iterationAlwaysBetray / iterations) * 100)
        
        #Alternate
        if(their_history[len(their_history) - 2] == opposite(theirLast)):
            iterationAlternate += 1.0
        weightAlternate = int((iterationAlternate / iterations) * 100)
        
        #Betray After Point
        if(theirLast == "b"):
            if(iterationBetrayAfterStart != 0):
                iterationBetrayAfterStart = len(theirHistroy)
            iterationBetrayAfter += 1.0
        weightBettrayAfter = int((iterationBetrayAfter / iterations) * 100)
        
        
        print my_history + " | " + their_history + " - " + str(weightBettrayAfter) + "% (" + str(iterationBetrayAfter) + ")"
        
        
        if( weightBettrayAfter > 2):
            return "b"
        else:
            if( weightAlternate > weightAlwaysCollude and weightAlternate > weightAlwaysBetray and weightAlternate >= weightOpposite ):
                return "c"
            elif( weightAlwaysCollude > weightAlwaysBetray and weightAlwaysCollude > weightOpposite):
                return "c"
            elif( weightAlwaysBetray > weightOpposite):
                return "b"
            else:
                return opposite(myLast)
            return theirLast
        
    else:
        #Reset Variables
        iterationAlwaysCollude = 0
        weightAlwaysCollude = 0
    
        iterationAlternate = 0
        weightAlternate = 0

        iterationOpposite = 0
        weightOpposite = 0
        
        iterationAlwaysBetray = 0
        weightAlwaysBetray = 0
        
        iterationBetrayAfter = 0
        iterationBetrayAfterStart = 0
        weightBettrayAfter = 0
        
        return start
