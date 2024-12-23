
from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):
    def __init__(self, sName, sDOB):
        super().__init__(sName, sDOB)

    @property
    def Name(self):
        return self.getName()

    @property
    def Birthdate(self):
        return self.getBirthdate()

    @property
    def Attitude(self):
        return super().getAttitude()

    @property
    def BirthDay(self):
        return super().getBirthDay()

    @property
    def LifePath(self):
        return super().getLifePath()

    @property
    def Personality(self):
        return super().getPersonality()

    @property
    def PowerName(self):
        return super().getPowerName()

    @property
    def Soul(self):
        return super().getSoul()

    @property
    def LifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way",
        }
        return descriptions.get(self.LifePath, "Unknown Life Path")

