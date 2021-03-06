import random 

team_name = 'Sicko Mo-Bamba'
strategy_name = 'Victory Royal'
strategy_description = 'Choose a random response, but if your partner betrays, betray the next time. If they collude, collude.'


def move(my_history,their_history,my_score,their_score):
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
    choices = ['c','b']
    if len(my_history) == 0:
      return random.choice(choices)
    elif len(my_history) >=1 and their_history[-1] == 'b':
      return 'b'
    elif their_history == my_history:
      return 'c'
