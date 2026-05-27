#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    
#odd    
if n % 2 != 0:
    print("Weird")

#even    
if n % 2 == 0:
    
    if 2<= n and n <=5:     # range of 2 to 5
        print("Not Weird")
        
    if 6<= n and n <=20:    # range of 6 to 20
        print("Weird")
        
    if n>20:                # grater than 20
        print("Not Weird")        
        
        