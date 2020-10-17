import time
import numpy as np
import random


''' Use binary search?
    This will make the array sorted from lowest to higest value
    0 = false and 1 = true '''
askbinary = input("Do you want to use binary search? If you choose no linear search will be used. y/n: ")
if askbinary[0].lower() == 'y':
    usebinary = 1
else:
    usebinary = 0

''' Use random array? Only works with linear search
    0 = false and 1 = true'''
askrandom = input("Do you want to randomize the input? If you choose no a sorted array will be used. y/n: ")
if askrandom[0].lower() == 'y':
    userandom = 1
else:
    userandom = 0

''' Different array types and SIZES ''' 
# define size of arrays
while True:
    try:
        MAX = int(input("What is the maximum size of the array you want?: "))
    except ValueError:
        print("Please enter integer only.")
        continue
    if MAX < 2:
        print("Please make a bigger array, select for example 100..")
        continue
    else:
        break
# Search for this value
while True:
    try:
        soek = int(input("What number do you want to search for in the arrays?: "))
    except ValueError:
        print("Please enter integer only.")
        continue
    if soek < 0:
        print("Please select a positive number to search for")
        continue
    else:
        break

####################################################
####################################################
if MAX >= 1000000 and usebinary == 0:
    answer = input("Running over 1 million in linear search will take quite some time. Do you want to run this in a binary search instead? y/n: ")
    if answer[0].lower() == 'y':
        usebinary = 1

# if using binary search we need a sorted array
if usebinary == 1 or userandom == 0:
    # sorted array
    a = np.arange(MAX)
elif userandom == 1:
    # random array
    # binary search wont work
    a = [random.randint(1,MAX) for _ in range(MAX)]


# search entire array for matching values
def linearsearch():
    count = 0
    for i in range(len(a)):
        if i == soek:
            count = count + 1
    return(count)

def binarysearch():  
    first = 0
    last = len(a)-1
    index = -1
    found = 0
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if a[mid] == soek:
            index = mid
            found = found + 1
        else:
            if soek<a[mid]:
                last = mid -1
            else:
                first = mid +1
    return found

if usebinary == 1:
    # start measuring time in ms
    startbinary = int(round(time.time() * 1000))
    # binary search
    matchesbinary = binarysearch()
    endbinary = int(round(time.time() * 1000))
    print("[BINARY] Found {} occurences in the array for {}. Time taken: {} ms. Array size: {}".format(matchesbinary,soek,endbinary-startbinary,len(a)))
else:
    #start measuring time in ms
    startlinear = int(round(time.time() * 1000))
    # linear search
    matcheslinear = linearsearch()
    endlinear = int(round(time.time() * 1000))
    print("[LINEAR] Found {} occurences in the array for {}. Time taken: {} ms. Array size: {}".format(matcheslinear,soek,endlinear-startlinear,len(a)))
