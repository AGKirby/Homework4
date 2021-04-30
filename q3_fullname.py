def fullname(first, last):
    if(not isinstance(first, str)): #if first name not a string
        return None
    if(not isinstance(last, str)): #if last name not a string
        return None
    return first + " " + last #append the first and last names with a space in between