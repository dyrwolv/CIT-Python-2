# Constants for flag indices
HAS_NUMBER = 10
MULTIPLE_NUM = 11

HAS_UPPER = 26
MULTIPLE_UPPER = 27

HAS_LOWER = 26
MULTIPLE_LOWER = 27

HAS_SPECIAL = 6
MULTIPLE_SPECIAL = 7

# ord Constants
ORD_A = ord('A') - 1
ORD_a = ord('a') - 1
ORD_0 = ord('0') - 1

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
    #TODO need to implement this
    bIsValid = sPassword.lower().startswith('pass' or 'pas' or 'pwd' or 'pa$$')
    return True


def check_pwd_length(sPassword):
    # checks if the password length is between 8 and 12 character inclusively
    bIsValid = 8 <= len(sPassword) <= 12
    if not bIsValid:
        print("Password must be between 8 and 12 characters")
    return bIsValid


def zero_counter(lCounter):
    # Zeros out the list
    for i in range(len(lCounter)):
        lCounter[i] = 0


def get_counter_values(sPassword, countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha):
    # Precompute constants

    for char in sPassword:
        if 'A' <= char <= 'Z':
            # convert uppercase letter to index (A = 0, B = 1, C = 2 ... Z = 23)
            index = ord(char) - ORD_A
            countOfUpperAlpha[index] += 1
            if countOfUpperAlpha[HAS_UPPER] == 0: # check if flag is set
                countOfUpperAlpha[HAS_UPPER] = 1 # if not set, set the flag
            elif countOfUpperAlpha[index] == 2 and countOfUpperAlpha[MULTIPLE_UPPER] == 0:
                countOfUpperAlpha[MULTIPLE_UPPER] = 1
        elif 'a' <= char <= 'z':
            # convert lowercase letter to index (a = 0, b = 1, c = 2 ... z = 23)
            index = ord(char) - ORD_a
            countOfLowerAlpha[index] += 1
            if countOfLowerAlpha[HAS_LOWER] == 0:
                countOfLowerAlpha[HAS_LOWER] = 1
            elif countOfLowerAlpha[index] == 2 and countOfLowerAlpha[MULTIPLE_LOWER] == 0:
                countOfLowerAlpha[MULTIPLE_LOWER] = 1
        elif '0' <= char <= '9':
            # convert numbers to index ( 0 = 0,  1 = 1, 2 = 2.... 9 = 9)
            index = ord(char) - ORD_0
            countOfNumbers[index] += 1
            if countOfNumbers[HAS_NUMBER] == 0:
                countOfNumbers[HAS_NUMBER] = 1
            elif countOfNumbers[index] > 1 and countOfNumbers[MULTIPLE_NUM] == 0:
                countOfNumbers[MULTIPLE_NUM] = 1
        elif char in "!@#$%^":
            # convert special characters to index (! -> 0, @ -> 1, etc.)
            countOfSpecials["!@#$%^".index(char)] += 1
            if countOfSpecials[HAS_SPECIAL] == 0:
                countOfSpecials[HAS_SPECIAL] = 1
            if countOfSpecials["!@#$%^".index(char)] == 2 and countOfSpecials[MULTIPLE_SPECIAL] == 0:
                countOfSpecials[MULTIPLE_SPECIAL] = 1


def check_one_of_each(countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha):
    bHasNumber = False
    bHasUpper = False
    bHasLower = False
    bHasSpecial = False

    # check if there's at least one number
    if countOfNumbers[HAS_NUMBER] > 0:
        bHasNumber = True
    else:
        print("Password must contain at least 1 number")

    # check if theres at least one special
    if countOfSpecials[HAS_SPECIAL] > 0:
        bHasSpecial = True
    else:
        print("Password must contain at least 1 special character: ! @ # $ % ^")

    # check if theres at least one uppercase
    if countOfUpperAlpha[HAS_UPPER] > 0:
        bHasUpper = True
    else:
        print("Password must contain at least 1 uppercase letter")

    # check if theres at least one lowercase
    if countOfLowerAlpha[HAS_LOWER] > 0:
        bHasLower = True
    else:
        print("Password must contain at least 1 lowercase letter")

    bIsValid = bHasNumber and bHasSpecial and bHasUpper and bHasLower

    return bIsValid


def char_counter_msg(countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha):
    #TODO ascii conversion magic message thing

    for char in range(countOfNumbers[HAS_NUMBER]):
        if countOfNumbers[char] > 1:
            number = chr(ORD_0 + char)
            print(f"{number}: {countOfNumbers[number]}")
    for char in range(countOfSpecials[HAS_SPECIAL]):
        if countOfSpecials[char] > 1:
            special = "!@#$%^".index(char)
            print(f"{special}: {countOfSpecials[special]}")
    for char in range(countOfUpperAlpha[HAS_UPPER]):
        if countOfUpperAlpha[char] > 1:
            upper = chr(ORD_A + char)
            print(f"{upper}: {countOfUpperAlpha[upper]}")
    for char in range(countOfLowerAlpha[HAS_LOWER]):
        if countOfLowerAlpha[char] > 1:
            lower = chr(ORD_a + char)
            print(f"{lower}: {countOfLowerAlpha[lower]}")



def check_more_than_one(countOfNumbers, countOfUpperAlpha, countOfLowerAlpha, countOfSpecials):
    bMutipleNum = False
    bMultipleSpecial = False
    bMultipleUpper = False
    bMultipleLower = False

    # check if there's moret than one of the same number
    if countOfNumbers[MULTIPLE_NUM] > 0:
        bMultipleNum = True
    # check if theres more than one of the same special
    if countOfSpecials[MULTIPLE_SPECIAL] > 0:
        bMultipleSpecial = True
    # check if theres more than of the same upperAlpha
    if countOfUpperAlpha[MULTIPLE_UPPER] > 0:
        bMultipleUpper = True
    # check if theres more than one of the same lowerAlpha
    if countOfLowerAlpha[MULTIPLE_LOWER] > 0:
        bMultipleLower = True

    bIsValid = bMutipleNum and bMultipleSpecial and bMultipleUpper and bMultipleLower

    if not bIsValid:
        char_counter_msg(countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha)
    return bIsValid

def contains_initials(sPassword, sInitials):
    # check if the initials are anywhere in the password regardless of case
    bIsValid = sPassword.lower().find(sInitials.lower()) == -1

    if not bIsValid:
        print("Password must not contain user initials")

    return bIsValid

# The Foxiest password validator of 'em all
def fox_password_validator(sInitials):
    # Initialize counters with extra slots for flags
    countOfNumbers = [0] * 12  # Indices 0-9 for counts, 10 for HAS_NUMBER, 11 for MULTIPLE_NUM
    countOfUpperAlpha = [0] * 28  # Indices 0-25 for A-Z, 26 for HAS_UPPER, 27 for MULTIPLE_UPPER
    countOfLowerAlpha = [0] * 28  # Indices 0-25 for a-z, 26 for HAS_LOWER, 27 for MULTIPLE_LOWER
    countOfSpecials = [0] * 8  # Indices 0-5 for specials, 6 for HAS_SPECIAL, 7 for MULTIPLE_SPECIAL

    while True:
        sPassword = create_pass()
        get_counter_values(sPassword, countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha)
        # start our validation checks
        if not check_pwd_length(sPassword):
            continue
        if not check_pwd_start(sPassword):
            continue
        if not check_one_of_each(countOfNumbers, countOfSpecials, countOfUpperAlpha, countOfLowerAlpha):
            continue
        if not contains_initials(sPassword, sInitials):
            continue
        if not check_more_than_one(countOfNumbers, countOfUpperAlpha, countOfLowerAlpha, countOfSpecials):
            print("your password is valid")
            break

        else:
            # reset counters
            zero_counter(countOfNumbers)
            zero_counter(countOfSpecials)
            zero_counter(countOfUpperAlpha)
            zero_counter(countOfLowerAlpha)


#print("Password must be between 8 and 12 characters \n")

def main():
    sName = name_input()
    sInitials = get_initials(sName)
    print(f"Name {sName} Initials {sInitials}")
    fox_password_validator(sInitials)


main()

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
