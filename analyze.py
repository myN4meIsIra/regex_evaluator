# analyze
"""
analyze a regex expression
"""

import re

class Analyze:

    def __init__(self):

        pass


    # analyze regex
    '''
        analyze the regex string
        @regex a string containing the string to be analyzed
    '''
    def analyzeRegex(self, regex):
        print(f'regex: {regex}')

        # split the regex string into an array of individual characters
        regex_char_array = list(regex)
        print(f"regex char array: {regex_char_array}")

        # run through the characters
        for i in range(len(regex)):
            print(f'char {i} = {regex[i]}')