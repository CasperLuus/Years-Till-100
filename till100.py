def get_user():
    name = ""
    while not verify_name(name):
        name = input("What is your name? ")
    return name

def verify_name(name):
    if len(name.strip()) < 1:
        return False
    else:
        return True

def get_user_age():
    age = input("How old are you? ")
    while not verify_age(age):
        print("Invalid age. Please Try Again.")
        age = input("How old are you? ")
    return int(age)

def verify_age(age):
    if len(age.strip()) < 1 or not age.isnumeric():
        return False
    else:
        if int(age) <= 0:
            return False
        return True

def calculate_years_till_100(age):
    return 100 - age

def age_results(name, years_till_100):
    if years_till_100 == 0:
        return "You're' already 100! Congrats on the long life " + name + "."
    elif years_till_100 < 0:
        return "WOW! You've really lived a long time. Guess I gotta make a new calculator just for you " \
            + name + ". What your next milestone?"
    else: 
        return "You will turn 100 in " + str(years_till_100) \
        + " years. Hope you enjoy these precious years of your life " + name + "!"

def main():
    print("Welcome! This is a simple app that tells you how many years it will take till you turn 100!")
    print("To start us off, please give me your name and age :).")
    name = get_user()
    age = get_user_age()
    print(age_results(name, calculate_years_till_100(age)))

if __name__ == "__main__":
    main()