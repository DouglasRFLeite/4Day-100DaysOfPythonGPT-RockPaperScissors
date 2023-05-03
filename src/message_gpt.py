import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from include import gpt

def gen_message(user_choice, computer_choice):
    prompt = f"""
Pretend I'm playing a game of Rock, Paper Scissors against you.
I choose {user_choice} and you choose {computer_choice}.
Create a text that:
1) Tells who won the game.
2) Has a creative message about the game or result of the game we just played.    
    """

    return gpt.get_completion(prompt=prompt)