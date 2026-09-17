from random import randint

""" since letter pool should be constant, here I am using a global variable with Capital letters for 
easy understanding)to store it. I will use this variable in the draw_letters function to draw letters from the pool """

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12,
    'F': 2, 
    'G': 3,
    'H': 2,
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }

SCORE_CHART = {
1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T' ],
2 : ['D', 'G'],
3 : ['B', 'C', 'M', 'P'],
4 : ['F', 'H', 'V', 'W', 'Y'],
5 : ['K'],	
8 : ['J', 'X'],
10 : ['Q', 'Z']
}

def draw_letters():

    """ create a list of letters based on the pool and their frequencies and #create a hand of 10 letters
    by randomly selecting from the list and removing 
    #the selected letter from the list to avoid duplicates """

    list =[]
    for letter,frequency in LETTER_POOL.items(): 

        list += [letter] * frequency
    hand = [] 
    NUM_TILES_ALLOWED_IN_HAND = 10
    for draw_count in range(NUM_TILES_ALLOWED_IN_HAND): 

        random_index = randint(0, len(list)-1)
        hand.append(list[random_index])
        list.pop(random_index)
    return hand 
    
def uses_available_letters(word, letter_bank):

    """ create a copy of the letter bank to keep track of the letters used and
    loop through each letter in the word and check if it is in the letter bank copy, if it is, 
        remove it from the copy, if not, return False
        if all letters found in the letter bank copy, return True """

    word = word.upper()
    letter_bank_copy = letter_bank.copy()
    for letter in word: 

        if letter in letter_bank_copy:
            letter_bank_copy.pop(letter_bank_copy.index(letter))
        else:
            return False
    return True

def score_word(word):

    """ initialize sum of points to 0 and loop through each letter in the word and add the corresponding score 
    from the SCORE_CHART and if the word length is between 7 and 10, add bonus points and return the total score """

    word = word.upper()
    sum_of_points = 0
    for letter in word:
        
        for points,list_of_letters in SCORE_CHART.items():
            if letter in list_of_letters:
                sum_of_points += points
    if len(word) >= 7:
        sum_of_points += 8
    return sum_of_points

def get_highest_word_score(word_list):

    """ initialize high score to 0 and best word to empty string, 
    then loop through the total score chart and compare the scores to find the highest score and the corresponding word,
    taking into account the tie-breaking rules """

    total_score_chart = {}
    for word in word_list:

        word_score = score_word(word)
        total_score_chart[word] = word_score
    high_score = 0
    best_word = ""
    for word,score in total_score_chart.items():

        if high_score < score:
            high_score = score
            best_word = word
        elif len(best_word) == 10:
            return best_word,high_score
        elif len(word) == 10  and len(best_word) != 10:
            best_word = word
            high_score = score
        elif high_score == score and len(best_word)> len(word):
            high_score = score
            best_word = word
    return (best_word, high_score)