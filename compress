# Complete the function below.
# Given string "aaabbrtuggggss" compress it as "a3b2rtug4s2"
# Input is str and assume all are smallercase 

def  compress(str):
    flag = 0
    result = ‘’ 
    counter = 0
    for i in range(len(str)-1):
        # Ensure the first pass has values populated
        if i==0:
            flag = str[i]
        result = result + str[i]

        #Check for repeatition 
        if flag == str[i+1]:
            counter = counter+1
        else:
            flag = str[i+1]
	       if counter != 0:
                result = result + counter.__str__()
            counter = 0 
            # Take care of last char in str
            if i == len(str)-2:
                result = result + str[i]
    return result
