# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    split_address = s.split("@")
    
    # First stop, check that there is only one @ in the address
    # If there is more, or less, than one, return error.
    if(len(split_address)<2):
        return 1, "This address does not have any @ in it"
    elif(len(split_address)>2):
        return 1, "This address has more than one @ in it"

    # We check that the pre-@ part of the address is composed of 3-6 alphanumeric characters
    if(len(split_address[0])<3):
        return 3, "The pre-@ part of this address has less than 3 characters"
    elif(len(split_address[0])>16):
        return 4, "The pre-@ part of this address has more than 16 characters"
    elif(split_address[0].isalnum() == False):
        return 5, "The pre-@ part of this address is not alphanumeric"

    # We split the post-@ part into domain name and TLD
    split_B = split_address[1].split(".")
    # And we check there is only one .
    if(len(split_B)<2):
        return 6, "The post-@ part of this address does not have any . in it"
    elif(len(split_B)>2):
        return 7, "The post-@ part of this address has more than one . in it"

    # We check the domain name is composed of 2-8 alphanumeric characters
    if(len(split_B[0])<2):
        return 8, "The domain name of this address has less than 2 characters"
    elif(len(split_B[0])>8):
        return 9, "The domain name of this address has more than 8 characters"
    elif(split_B[0].isalnum() == False):
        return 10, "The domain name of this address is not alphanumeric"

    # And finally, we check the TLD is either com, edu, org, or gov.
    if(split_B[1]!="com" and split_B[1]!="edu" and split_B[1]!="org" and split_B[1]!="gov"):
        return 11, "The top-level domain of this address is not {com, edu, org, gov}"

    return None, "Seems legit"



    


    

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
