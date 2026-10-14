def high(x):
    all_letters = list(enumerate(list("abcdefghijklmnopqrstuvwxyz")))
    all_letters_dict = {}
    score = 0
    scores_list = []
    words_list = x.split(" ")
    
    for index, letter in all_letters:
        all_letters_dict[letter] = index + 1;
    
    for letter in x:
        if letter == " ":
            scores_list.append(score)
            score = 0
            #scores_list.append(-1)
            continue
        score = score + all_letters_dict[letter]
    
    scores_list.append(score)
    score = 0
    
    max_score = max(scores_list)
    
    for i in range(0, len(scores_list)):
        if scores_list[i] == max_score:
            return words_list[i]


x = "man i need a taxi up to ubud"
high_score_word = high(x)
print(high_score_word)

"""

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""
