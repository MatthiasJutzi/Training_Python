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
    