import random

POSSESSIVE_PRONOUNS = ["her", "his", "their", "our"]

PERSONAL_PRONOUNS = ["she", "he", "they"]

LOCATIONS = ["backyard", "small town", "city"]

TIMING = ["time", "summer", "weekend", "next month", "the night"]


def main():
    print("--- welcome to the ceedmedia clickbait generator ----")

    clickbait_category = random.randint(1, 5)

    if clickbait_category == 1:
        result = backyard_discovery()
    elif clickbait_category == 2:
        result = revelation()
    elif clickbait_category == 3:
        result = town_event()
    elif clickbait_category == 4:
        result = town_event()
    else:
        result = celebrity()

    print(result)


def backyard_discovery():
    poss_pronoun = random.choice(POSSESSIVE_PRONOUNS)
    per_pronoun = random.choice(PERSONAL_PRONOUNS)
    location = random.choice(LOCATIONS)
    timing = random.choice(TIMING)
    return f"You won't believe what {per_pronoun} found in {poss_pronoun} {location} just in {timing}"


def revelation():
    poss_pronoun = random.choice(POSSESSIVE_PRONOUNS)
    per_pronoun = random.choice(PERSONAL_PRONOUNS)
    return f"{poss_pronoun} jaw dropped when {per_pronoun} discovered the shocking truth about {poss_pronoun} long-lost possession."


def town_event():
    location = random.choice(LOCATIONS)
    timing = random.choice(TIMING)
    return f"Unbelievable: This {location}'s residents are experiencing a once-in-a-lifetime event this {timing}!"


def celebrity():
    poss_pronoun = random.choice(POSSESSIVE_PRONOUNS)
    per_pronoun = random.choice(PERSONAL_PRONOUNS)
    location = random.choice(LOCATIONS)
    timing = random.choice(TIMING)
    return f"{per_pronoun} were left speechless as {poss_pronoun} favorite celebrity announced a surprise visit to the {location} {timing}."


def midnight():
    poss_pronoun = random.choice(POSSESSIVE_PRONOUNS)
    timing = random.choice(TIMING)
    return f"Is it finally happening? {poss_pronoun} minds are blown by the unexpected turn of events **in the middle of {timing}!"


if __name__ == "__main__":
    main()
