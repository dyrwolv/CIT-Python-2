# Dakota Ford Password Validator
# The Foxiest password validator of 'em all


def create_pass():

    # ask user to enter a password
    sPassword = input("Enter new password: ")
    return sPassword

def name_input():
    sName = input("Enter Full Name such as John Smith: ")
    return sName


def get_initials(sName):
    # Expected Name Format a 2 part string with a single space separating the parts
    # get the initials by taking first index and str.find to get the last name start index
    sInitials = str(sName[0] + sName[sName.find(" ") + 1]).upper()
    return sInitials


def check_pwd_start(sPassword):
    prefixes = ('pass', 'pas', 'pwd', 'pa$$')
    if sPassword.lower().startswith(prefixes):
        print("Password must not start with 'pass', 'pas', 'pwd', or 'pa$$'")
        return False
    return True


def check_pwd_length(sPassword):
    # checks if the password length is between 8 and 12 character inclusively
    bIsValid = 8 <= len(sPassword) <= 12
    if not bIsValid:
        print("Password must be between 8 and 12 characters")
        return False
    return bIsValid


def zero_counter(lCounter):
    # Zeros out the list
    for i in range(len(lCounter)):
        lCounter[i] = 0

def contains_initials(sPassword, sInitials):
    # check if the initials are anywhere in the password regardless of case
    bIsValid = sInitials.lower() not in sPassword.lower()

    if not bIsValid:
        print("Password must not contain user initials")

    return bIsValid

def get_counter_values(sPassword, asciiCounters):
    # iterate through the password to fill the counters

    for char in sPassword:
        asciiCounters[ord(char)] += 1


def check_one_of_each(asciiCounters):
    bHasNumber = False
    bHasUpper = False
    bHasLower = False
    bHasSpecial = False

    """
    we're going to use the sum of the list slices for
    numbers 48 -> 57
    upper 65 -> 90
    lower 97 -> 122
    the special character are a bit complicated, because its spread out
    123 -> 126
    91 -> 96
    58 -> 64
    32 -> 47
    if the sum of either of these is great than 1
    we can assume theres at least 1 of them
    """

    # check for numbers
    if sum(asciiCounters[48:58]) > 0:
        bHasNumber = True
    else:
        print("Password must contain at least one number")

    # check for upper alphanumeric
    if sum(asciiCounters[65:91]) > 0:
        bHasUpper = True
    else:
        print("Password must contain at least one uppercase letter")

    # check for lower alphanumeric
    if sum(asciiCounters[97:123]) > 0:
        bHasLower = True
    else:
        print("Password must contain at least one lowercase letter")

    # check for special character
    if sum(asciiCounters[123:] + asciiCounters[91:97] + asciiCounters[58:65] + asciiCounters[32:48]) > 0:
        bHasSpecial = True
    else:
        print("Password must contain at least one special character")

    bIsValid = bHasNumber and bHasSpecial and bHasUpper and bHasLower

    return bIsValid


def check_more_than_one(asciiCounters, sPassword):
    for char in sPassword:
        count = asciiCounters[ord(char)]
        if count > 1:
            char_counter_msg(asciiCounters, sPassword)
            return True
    else:
        return False


def char_counter_msg(asciiCounters, sPassword):
    alreadyChecked = []
    for char in sPassword:
        if asciiCounters[ord(char)] > 1 and char not in alreadyChecked:
            print(f"{char}: appeared {asciiCounters[ord(char)]} times")
            alreadyChecked.append(char)



def fox_password_validator(sInitials):
    # array used for indexing the ASCII value and how many times it appears.
    asciiCounters = [0] * 128 # creates an empty array of 0's that we can use to counter the chars

    while True:
        # reset counters
        zero_counter(asciiCounters)

        sPassword = create_pass()
        get_counter_values(sPassword, asciiCounters)
        # start our validation checks
        if not check_pwd_length(sPassword):
            continue
        if not check_pwd_start(sPassword):
            continue
        if not check_one_of_each(asciiCounters):
            continue
        if not contains_initials(sPassword, sInitials):
            continue
        if not check_more_than_one(asciiCounters, sPassword):
            break
    print("your password is valid")

def main():
    sName = name_input()
    sInitials = get_initials(sName)
    print(f"Name {sName} Initials {sInitials}")
    fox_password_validator(sInitials)

main()
