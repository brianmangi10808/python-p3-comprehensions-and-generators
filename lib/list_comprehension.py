#!/usr/bin/env python3

#!/usr/bin/env python3

def return_evens(num_list):
    '''Returns a list containing only the even numbers from num_list.'''
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    '''Adds an exclamation mark to the end of each sentence in sentence_list.'''
    return [sentence + "!" for sentence in sentence_list]

if __name__ == "__main__":
    num_list = range(10)
    print(return_evens(num_list))

    sentence_list = [
        "I like computers",
        "I require coffee",
        "Live long and prosper",
    ]
    print(make_exclamation(sentence_list))
