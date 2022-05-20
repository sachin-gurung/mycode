#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
post = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as postFile:

    # loop over the file
    for line in postFile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] POST" in line:
            post += 1 # this is the same as loginfail = loginfail + 1

print("The number of successful POST attempts is", post)


