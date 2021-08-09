#!/usr/bin/python
import random
numbers = list(range(1,10))
def shuffler():
    random.shuffle(numbers)
    print(numbers)

shuffler()
