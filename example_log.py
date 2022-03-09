#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Solution to Customization 01"""

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0 # total times we see pattern, "-] Authorization failed"
fail_record = {}  # 'ip.add.re.ss': 'total fails (int)


# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            #print(line.split(" ")[-1]) # isolate the IP address
            ip = line.split(" ")[-1].rstrip('\n') # this is the failed IP
            if ip in fail_record:  # if the IP is already in the dict, we just increase its value by one
                fail_record[ip] = fail_record[ip] + 1
            else: # this is the first time we saw this IP with a failure
                fail_record[ip] = 1

        # the following elif agumentation MUST be AFTER we check for a fail
        # this statement assumes the if statement above it tested false
        elif "-] Authorization failed" in line:  # can ONLY be true if the "if" was false!
            successful += 1 # this is the total number of times we see this pattern

# display the number of failed log in attempts
print("The number of failed log in attempts is:")
# to discover total fails
print(fail_record)
for entry in fail_record:
    print(f'{entry} failed to log in {fail_record.get(entry)} times')

# display the number of successful log in attempts
print("The number of successful log ins is", successful)

