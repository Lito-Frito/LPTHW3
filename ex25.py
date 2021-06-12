def break_words(stuff): #you need to 'break' the words first so f(x)'s like sorted can work and to spit out the var 'words'
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #calls back to line 1
    return sort_words(words) #calls back to line 6

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) #calls back to line 1
    print_first_word(words) #calls back to line 10
    print_last_word(words) #calls back to line 15

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) #calls back to line 20
    print_first_word(words) #calls back to line 10
    print_last_word(words) #calls back to line 15
