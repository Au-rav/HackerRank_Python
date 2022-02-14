import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    i = 1
    while(i<=10):
        result = n*i
        print(n,'x',i,'=',result)
        i+=1