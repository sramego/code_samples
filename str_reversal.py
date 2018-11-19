# Code to Reverse an array without affecting special characters

import sys
 
def doReverse(test):
    teststr = list(test)
    j = len(teststr) -1
    i = 0
    while (i<j):
        if teststr[i].isalpha():
            while (not(teststr[j].isalpha())):
                j = j-1
            if j<i:   
                break
            item = teststr[i]
            teststr[i] = teststr[j]
            teststr[j] = item
            j= j-1
        i = i + 1	
    return ''.join(teststr)

if __name__ == '__main__':
    '''
    Given a string, that contains special character together with alphabets 
    (a to z and A to Z), reverse the string in a way that special 
    characters are not affected. 
    Sample: "Ab,c,de!$" should return "ed,c,bA!$"
    '''
    iString = sys.stdin.readline().strip('\n')
    print "Converted string is %s " % doReverse(iString)
