
from random import randint
#since letter pool should be constant, here I am using a global variable with Capital letters(for easy understanding)to store it.
#I will use this variable in the draw_letters function to draw letters from the pool.
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
SCORE_CHART = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
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
    return hand 
    
def uses_available_letters(word, letter_bank):
    #create a copy of the letter bank to keep track of the letters used
    word = word.upper()
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    #print(letter_bank)
    return True

def score_word(word):
    sum_of_points = 0
    BONUS_POINTS_FOR_LENGTH = 8
    word = word.upper()
    for letter in word:
        sum_of_points += SCORE_CHART[letter]
    if len(word) >= 7 and len(word) <= 10:
        sum_of_points += BONUS_POINTS_FOR_LENGTH
    return sum_of_points       

        

def get_highest_word_score(word_list):
    total_score_chart = {}
    for word in word_list:
        word_score = score_word(word)
        total_score_chart[word] = word_score
    high_score =0
    best_word = ""
    for word,score in total_score_chart.items():
        if score > high_score:
            high_score = score
            best_word = word
        elif len(best_word) == 10:
            return best_word, high_score
        elif high_score == score and len(best_word) > len(word):
            high_score = score
            best_word = word
        elif len(word) == 10 and len(best_word) != 10:
            best_word = word
            high_score = score
    return best_word, high_score