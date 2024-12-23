from Numerology import Numerology

def main():
    # Input: Get user details
    name = input("Enter your full name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your full name: ").strip()

    dob = input("Enter your birth date (MM/DD/YYYY): ").strip()
    while not dob or len(dob) != 10 or not all(c.isdigit() or c in "-/" for c in dob):
        dob = input("Invalid format. Please enter your birth date in MM/DD/YYYY format: ").strip()

    dob = dob.replace('/', '-')  # Standardize date format

    # Create Numerology instance
    numerology = Numerology(name, dob)

    # Compute numbers
    life_path = numerology.getLifePath()
    birth_day = numerology.getBirthDay()
    attitude = numerology.getAttitude()
    soul = numerology.getSoul()
    personality = numerology.getPersonality()
    power_name = numerology.getPowerName()

    # Display results
    print("\nNumerology Results:")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Life Path Number: {life_path}")
    print(f"Birth Day Number: {birth_day}")
    print(f"Attitude Number: {attitude}")
    print(f"Soul Number: {soul}")
    print(f"Personality Number: {personality}")
    print(f"Power Name Number: {power_name}")

if __name__ == "__main__":
    main()
