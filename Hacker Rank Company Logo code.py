

#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    #Sorted will sort the list of characters in descending order and places the characters in alphabetical order
    #Most_common will give the to most number of occurances of characters from the stringe/input
    answer = Counter(sorted(s)).most_common(3)
    for key, value in answer:
        print(key, value)
        