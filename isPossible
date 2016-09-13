# Complete the function below.
# constraint: 1 <= a,b,c,d <= 1000
# Given (a,b), allowed operations are: 
#   1. (a,b) = (a+b, b)
#   2. (a,b) = (a, a+b)
# Any number of similar operations can be done. 
# Output 'Yes' if (c,d) can be obtained from (a,b) else 'No'
# eg: (a,b) = (1,4). Possible outputs for which return will be 'Yes':
# (1,5) or (5,4) or (5,9) or (5,13) or (13,9) etc 

def  isPossible(a, b, c, d):
    while True:
        diff = max(c,d) - min(c,d)
        # Constraint 1<=a,b,c,d <=1000
        if (diff<=0) or ((a==c and b==d) or (a==d and b==c)):
            break 
        else:
            if c == max(c,d):
                c = max(c,d) - min(c,d)
            else:
                d = max(c,d) - min(c,d)
                
    if((a==c and b==d) or (a==d and b==c)):
        return 'Yes'
    else:
        return 'No'
