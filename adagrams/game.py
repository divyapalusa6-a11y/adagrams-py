
from random import randint
#since letter pool should be constant, here I am using a global variable with Capital letters(for easy understanding)to store it.
#I will use this variable in the draw_letters function to draw letters from the pool.
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
def draw_letters():
    #create a list of letters based on the pool and their frequencies
    list =[]
    for letter,frequency in LETTER_POOL.items(): 
        list += [letter] * frequency
    hand = []
    NUM_TILES_ALLOWED_IN_HAND = 10
    for draw_count in range(NUM_TILES_ALLOWED_IN_HAND):
        random_index = randint(0, len(list)-1)
        hand.append(list[random_index])
        list.remove(list[random_index])
    #print(list)
    #print(hand)
    return hand 
    
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass