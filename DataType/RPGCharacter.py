# Character builder function in python 

def create_character(name, strength, intelligence, charisma):

    # Name validation
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"
    
    # Stats validation
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or  intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    # function for doted line and undoted line out of 10 base on the stat value
    def stat_bar(label, value):
        filled = '●' * value
        empty = '○' * (10 - value)
        return f"{label} {filled}{empty}"
    
    # If all validations pass, return the character information
    # Building character sheet with name and stats in a nice format

    result = "\n".join([
        name, 
        stat_bar("STR", strength),
        stat_bar("INT", intelligence),
        stat_bar("CHA", charisma)
    ])
    
    return result

# Example usage
character = create_character("Aragorn", 3, 2, 2)
print(character)