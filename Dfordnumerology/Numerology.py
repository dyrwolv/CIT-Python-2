class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName
        self.dob = sDOB

    def getName(self):
        return self.name

    def getBirthdate(self):
        return self.dob

    @staticmethod
    def _reduce_to_single_digit(number):
        while number > 9 and number != 11 and number != 22:
            number = sum(int(digit) for digit in str(number))
        return number

    @staticmethod
    def _convert_char_to_number(char):
        if 'A' <= char <= 'Z':  # Uppercase
            return (ord(char) - 65) % 9 + 1
        elif 'a' <= char <= 'z':  # Lowercase
            return (ord(char) - 97) % 9 + 1
        return 0  # Non-alphabetic characters are ignored

    def getLifePath(self):
        digits = [int(digit) for digit in self.dob if digit.isdigit()]
        return self._reduce_to_single_digit(sum(digits))

    def getBirthDay(self):
        day = int(self.dob.split('-')[1])
        return self._reduce_to_single_digit(day)

    def getAttitude(self):
        month, day = map(int, self.dob.split('-')[:2])
        return self._reduce_to_single_digit(month + day)

    def getSoul(self):
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        soul_total = sum(
            self._convert_char_to_number(char) for char in self.name if char in vowels
        )
        return self._reduce_to_single_digit(soul_total)

    def getPersonality(self):
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        personality_total = sum(
            self._convert_char_to_number(char) for char in self.name if char.isalpha() and char not in vowels
        )
        return self._reduce_to_single_digit(personality_total)

    def getPowerName(self):
        return self._reduce_to_single_digit(self.getSoul() + self.getPersonality())
