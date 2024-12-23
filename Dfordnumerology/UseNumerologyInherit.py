0
from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():
    # Get input for name and date of birth
    while True:
        name = input("Enter your full name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    while True:
        dob = input("Enter your birthdate (MM-DD-YYYY): ").strip()
        if len(dob) == 10 and (dob[2] in "-/" and dob[5] in "-/") and dob.replace("-", "").replace("/", "").isdigit():
            # Normalize date to use dashes
            dob = dob.replace("/", "-")
            break
        print("Invalid date format. Please enter in MM-DD-YYYY format.")

    # Create instance of NumerologyLifePathDetails
    numerology = NumerologyLifePathDetails(name, dob)

    # Display calculated results using properties
    print(f"Name: {numerology.Name}")
    print(f"Birthdate: {numerology.Birthdate}")
    print(f"Attitude Number: {numerology.Attitude}")
    print(f"Birthday Number: {numerology.BirthDay}")
    print(f"Life Path Number: {numerology.LifePath}")
    print(f"Life Path Description: {numerology.LifePathDescription}")
    print(f"Personality Number: {numerology.Personality}")
    print(f"Power Name Number: {numerology.PowerName}")
    print(f"Soul Number: {numerology.Soul}")

if __name__ == "__main__":
    main()
