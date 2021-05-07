"""
This program prompts a user for words to fill in a madlib of Smelly Cat (Phoebe`s Song).
"""

def main():
    animal1 = input("Please type an animal and press enter. ")
    verb_ending_ing1 = input("Please type a verb ending in 'ing' and press enter. ")
    noun1 = input("Please type a noun and press enter. ")
    verb1 = input("Please type a verb and press enter. ")
    occupation = input("Please type an occupation and press enter. ")
    adjective1 = input("Please type an adjective and press enter. ")
    animal2 = input("Please type an animal and press enter. ")
    noun2 = input("Please type a noun and press enter. ")
    noun_plural = input("Please type a plural noun and press enter. ")
    relationship = input("Please type a relationship and press enter. ")
    body_part_plural = input("Please type a plural body part and press enter. ")
    verb_ending_ing2 = input("Please type a verb ending in 'ing' and press enter. ")
    noun3 = input("Please type a noun and press enter. ")

    print("Smelly", animal1, "smelly", animal1, "\n"
        "What are they", verb_ending_ing1, "you?\n"
        "Smelly", animal1, "smelly", animal1, "\n"
        "It`s not your", noun1 + ".\n"
        "They won`t", verb1, "you to the " + occupation + ".\n"
        "You`re obviously not their", adjective1, animal2 + ".\n"
        "You may not be a", noun2, "of", noun_plural, "\n"
        "And you`re no", relationship, "to those with", body_part_plural + ".\n"
        "Smelly", animal1, "smelly", animal1, "\n"
        "What are they", verb_ending_ing2, "you?\n"
       "Smelly", animal1, "smelly", animal1, "\n"
        "It`s not your", noun3 + ".\n")


if __name__ == "__main__":
    main()
