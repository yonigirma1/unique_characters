#checking if a string has unique characters

#First method
def unique_character1(str):
    return len(set(str)) == len(str)

#Second Method
def unique_character2(str):

    unique = set()
    for item in str:
        if item in unique:
            return false:
        else:
            unique.add(item)
    return True


                            
